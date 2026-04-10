#!/usr/bin/env python3
"""CLI tool for managing playtest runs with per-run state.

Each run gets its own state file, enabling parallel playtests by multiple agents.

Usage:
    playtest.py new <run-id>          -- initialise a new run
    playtest.py deal <run-id> <N>     -- deal treaty cards to N players
    playtest.py draw <run-id>         -- draw the next threat/safety card
    playtest.py status <run-id>       -- print a run summary
"""
import argparse
import json
import os
import random
import sys

PLAYTESTS_DIR = os.path.join(os.path.dirname(__file__), "playtests")
DEFINITIONS_FILE = os.path.join(os.path.dirname(__file__), "definitions.jsonl")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def state_path(run_id):
    return os.path.join(PLAYTESTS_DIR, f"{run_id}.state.json")

def cards_path(run_id):
    return os.path.join(PLAYTESTS_DIR, f"{run_id}.cards.jsonl")

def load_state(run_id):
    path = state_path(run_id)
    if not os.path.exists(path):
        sys.exit(f"Error: no state file for run '{run_id}' ({path}). Run 'new' first.")
    with open(path) as f:
        return json.load(f)

def save_state(run_id, state):
    with open(state_path(run_id), "w") as f:
        json.dump(state, f, indent=2)

def load_all_definitions():
    cards = []
    with open(DEFINITIONS_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                cards.append(json.loads(line))
    return cards

def load_cards_snapshot(run_id):
    with open(cards_path(run_id)) as f:
        return [json.loads(line) for line in f if line.strip()]


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_new(args):
    os.makedirs(PLAYTESTS_DIR, exist_ok=True)
    spath = state_path(args.run_id)
    if os.path.exists(spath):
        sys.exit(f"Error: run '{args.run_id}' already exists. Choose a unique run-id.")

    all_cards = load_all_definitions()

    # Write snapshot of all cards
    cpath = cards_path(args.run_id)
    with open(cpath, "w") as f:
        for card in all_cards:
            f.write(json.dumps(card) + "\n")

    # Build and shuffle the draw deck (threat + safety cards)
    deck = [c for c in all_cards if c.get("type") in ("threat-1", "threat-2", "safety")]
    random.shuffle(deck)

    state = {
        "remaining_deck": deck,
        "hands": {},
        "active_treaty": [],
        "failures": 0,
        "safety": 0,
        "history": [],
    }
    save_state(args.run_id, state)
    print(f"Run '{args.run_id}' created. Draw deck: {len(deck)} cards. Snapshot: {len(all_cards)} cards total.")


def cmd_deal(args):
    state = load_state(args.run_id)
    if state["hands"]:
        sys.exit("Error: cards have already been dealt for this run.")

    n = args.n
    if n < 1:
        sys.exit("Error: number of players must be at least 1.")

    all_cards = load_cards_snapshot(args.run_id)
    treaty_cards = [c for c in all_cards if c.get("type") == "treaty"]
    random.shuffle(treaty_cards)

    hands = {f"player{i+1}": [] for i in range(n)}
    for idx, card in enumerate(treaty_cards):
        player = f"player{(idx % n) + 1}"
        hands[player].append(card)

    state["hands"] = hands
    save_state(args.run_id, state)

    for player, cards in hands.items():
        print(f"\n{player} ({len(cards)} cards):")
        for c in cards:
            cat = c.get("category", c.get("type", ""))
            print(f"  - {c['name']} [{cat}]: {c['description']}")


def cmd_draw(args):
    state = load_state(args.run_id)
    if not state["remaining_deck"]:
        print(json.dumps({"type": "deck-empty"}))
        sys.exit(0)

    card = state["remaining_deck"].pop(0)
    turn = len(state["history"]) + 1
    state["history"].append({"turn": turn, "card": card["name"], "type": card["type"]})
    save_state(args.run_id, state)
    print(json.dumps(card, indent=2))


def cmd_status(args):
    state = load_state(args.run_id)
    print(f"Run:              {args.run_id}")
    print(f"Failures:         {state['failures']}")
    print(f"Safety count:     {state['safety']}")
    print(f"Remaining deck:   {len(state['remaining_deck'])} cards")
    players = state.get("hands", {})
    if players:
        totals = ", ".join(f"{p}: {len(h)} cards" for p, h in players.items())
        print(f"Hands dealt:      {totals}")
    else:
        print("Hands dealt:      (not yet dealt)")
    active = state.get("active_treaty", [])
    if active:
        print(f"Active treaty:    {', '.join(active)}")
    else:
        print("Active treaty:    (none)")
    history = state.get("history", [])
    if history:
        print(f"\nHistory ({len(history)} turns):")
        for entry in history:
            print(f"  Turn {entry['turn']:>2}: [{entry['type']}] {entry['card']}")
    else:
        print("\nHistory: (no cards drawn yet)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new", help="Initialise a new playtest run")
    p_new.add_argument("run_id", metavar="run-id")

    p_deal = sub.add_parser("deal", help="Deal treaty cards to N players")
    p_deal.add_argument("run_id", metavar="run-id")
    p_deal.add_argument("n", metavar="N", type=int)

    p_draw = sub.add_parser("draw", help="Draw the next threat/safety card")
    p_draw.add_argument("run_id", metavar="run-id")

    p_status = sub.add_parser("status", help="Print a run summary")
    p_status.add_argument("run_id", metavar="run-id")

    args = parser.parse_args()
    {"new": cmd_new, "deal": cmd_deal, "draw": cmd_draw, "status": cmd_status}[args.command](args)


if __name__ == "__main__":
    main()
