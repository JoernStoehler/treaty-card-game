#!/usr/bin/env python3
"""CLI tool for managing v2 playtest runs.

Each run gets its own state file, enabling parallel playtests by multiple agents.

Usage:
    playtest.py new <run-id>                        -- create a new run (subsets threat deck)
    playtest.py draw <run-id>                       -- draw the next threat card
    playtest.py commit-treaty <run-id> <card-id>    -- move treaty card to active treaty
    playtest.py resolve <run-id> <card-id>          -- move threat from unresolved to resolved
    playtest.py unresolve <run-id> <card-id>        -- move threat back to unresolved
    playtest.py status <run-id>                     -- print run summary
"""
import argparse
import json
import os
import random
import sys

PLAYTESTS_DIR = os.path.join(os.path.dirname(__file__), "playtests")
DEFINITIONS_FILE = os.path.join(os.path.dirname(__file__), "definitions.jsonl")

EXTINCTION_THRESHOLD = 3


def state_path(run_id):
    return os.path.join(PLAYTESTS_DIR, f"{run_id}.state.json")


def load_state(run_id):
    path = state_path(run_id)
    if not os.path.exists(path):
        sys.exit(f"Error: no state file for run '{run_id}'. Run 'new' first.")
    with open(path) as f:
        return json.load(f)


def save_state(run_id, state):
    with open(state_path(run_id), "w") as f:
        json.dump(state, f, indent=2)


def load_definitions():
    cards = []
    with open(DEFINITIONS_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                cards.append(json.loads(line))
    return cards


def unresolved_capability_count(state):
    return len([t for t in state["unresolved"] if t.get("capability")])


def check_extinction(state):
    count = unresolved_capability_count(state)
    if count >= EXTINCTION_THRESHOLD:
        return True, count
    return False, count


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_new(args):
    os.makedirs(PLAYTESTS_DIR, exist_ok=True)
    spath = state_path(args.run_id)
    if os.path.exists(spath):
        sys.exit(f"Error: run '{args.run_id}' already exists.")

    all_cards = load_definitions()
    threats = [c for c in all_cards if c["type"] == "threat"]
    treaty_cards = [c for c in all_cards if c["type"] == "treaty"]

    # Subset: use roughly half the threat deck
    random.shuffle(threats)
    subset_size = len(threats) // 2
    deck = threats[:subset_size]
    removed = threats[subset_size:]

    state = {
        "deck": deck,
        "unresolved": [],
        "resolved": [],
        "ideas_pool": treaty_cards,
        "active_treaty": [],
        "history": [],
        "removed_unseen": [c["id"] for c in removed],
    }
    save_state(args.run_id, state)

    print(f"Run '{args.run_id}' created.")
    print(f"  Threat deck: {len(deck)} cards (from {len(threats)} total)")
    print(f"  Treaty cards: {len(treaty_cards)} in ideas pool")
    cap_in_deck = len([c for c in deck if c.get("capability")])
    print(f"  Capability threats in deck: {cap_in_deck}")
    print(f"  Extinction threshold: {EXTINCTION_THRESHOLD}")


def cmd_draw(args):
    state = load_state(args.run_id)

    if not state["deck"]:
        extinct, cap_count = check_extinction(state)
        print(json.dumps({
            "event": "deck-empty",
            "unresolved_capability": cap_count,
            "extinct": extinct,
        }, indent=2))
        return

    card = state["deck"].pop(0)
    state["unresolved"].append(card)
    turn = len(state["history"]) + 1
    state["history"].append({"turn": turn, "card_id": card["id"], "card_name": card["name"]})
    save_state(args.run_id, state)

    extinct, cap_count = check_extinction(state)
    output = {
        "turn": turn,
        "card": card,
        "remaining_in_deck": len(state["deck"]),
        "unresolved_capability": cap_count,
        "extinct": extinct,
    }
    print(json.dumps(output, indent=2))


def cmd_commit_treaty(args):
    state = load_state(args.run_id)
    card_id = args.card_id

    pool = state["ideas_pool"]
    match = [c for c in pool if c["id"] == card_id]
    if not match:
        available = [c["id"] for c in pool]
        sys.exit(f"Error: '{card_id}' not in ideas pool. Available: {', '.join(available)}")

    card = match[0]
    state["ideas_pool"] = [c for c in pool if c["id"] != card_id]
    state["active_treaty"].append(card)
    save_state(args.run_id, state)
    print(f"Committed: {card['name']}")
    print(f"  Active treaty: {len(state['active_treaty'])} provisions")
    print(f"  Ideas pool: {len(state['ideas_pool'])} remaining")


def cmd_resolve(args):
    state = load_state(args.run_id)
    card_id = args.card_id

    unresolved = state["unresolved"]
    match = [c for c in unresolved if c["id"] == card_id]
    if not match:
        available = [c["id"] for c in unresolved]
        sys.exit(f"Error: '{card_id}' not in unresolved. Available: {', '.join(available)}")

    card = match[0]
    state["unresolved"] = [c for c in unresolved if c["id"] != card_id]
    state["resolved"].append(card)
    save_state(args.run_id, state)

    _, cap_count = check_extinction(state)
    label = " (capability)" if card.get("capability") else " (context)"
    print(f"Resolved: {card['name']}{label}")
    print(f"  Unresolved capability: {cap_count}/{EXTINCTION_THRESHOLD}")


def cmd_unresolve(args):
    state = load_state(args.run_id)
    card_id = args.card_id

    resolved = state["resolved"]
    match = [c for c in resolved if c["id"] == card_id]
    if not match:
        available = [c["id"] for c in resolved]
        sys.exit(f"Error: '{card_id}' not in resolved. Available: {', '.join(available)}")

    card = match[0]
    state["resolved"] = [c for c in resolved if c["id"] != card_id]
    state["unresolved"].append(card)
    save_state(args.run_id, state)

    extinct, cap_count = check_extinction(state)
    label = " (capability)" if card.get("capability") else " (context)"
    print(f"Unresolved: {card['name']}{label}")
    print(f"  Unresolved capability: {cap_count}/{EXTINCTION_THRESHOLD}")
    if extinct:
        print(f"  EXTINCTION!")


def cmd_status(args):
    state = load_state(args.run_id)
    extinct, cap_count = check_extinction(state)

    print(f"Run: {args.run_id}")
    print(f"Deck remaining: {len(state['deck'])}")
    print(f"Unresolved capability: {cap_count}/{EXTINCTION_THRESHOLD}" +
          (" — EXTINCT" if extinct else ""))
    print()

    if state["unresolved"]:
        print("Unresolved threats:")
        for c in state["unresolved"]:
            label = " [CAP]" if c.get("capability") else ""
            print(f"  {c['name']}{label}")
    else:
        print("Unresolved threats: (none)")

    if state["resolved"]:
        print(f"\nResolved threats ({len(state['resolved'])}):")
        for c in state["resolved"]:
            label = " [CAP]" if c.get("capability") else ""
            print(f"  {c['name']}{label}")

    print(f"\nActive treaty ({len(state['active_treaty'])}):")
    for c in state["active_treaty"]:
        print(f"  {c['name']}")

    print(f"\nIdeas pool ({len(state['ideas_pool'])}):")
    for c in state["ideas_pool"]:
        print(f"  {c['name']}")

    if state["history"]:
        print(f"\nHistory ({len(state['history'])} turns):")
        for entry in state["history"]:
            print(f"  Turn {entry['turn']:>2}: {entry['card_name']}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("new", help="Create a new playtest run")
    p.add_argument("run_id", metavar="run-id")

    p = sub.add_parser("draw", help="Draw the next threat card")
    p.add_argument("run_id", metavar="run-id")

    p = sub.add_parser("commit-treaty", help="Move treaty card to active treaty")
    p.add_argument("run_id", metavar="run-id")
    p.add_argument("card_id", metavar="card-id")

    p = sub.add_parser("resolve", help="Move threat from unresolved to resolved")
    p.add_argument("run_id", metavar="run-id")
    p.add_argument("card_id", metavar="card-id")

    p = sub.add_parser("unresolve", help="Move threat back to unresolved")
    p.add_argument("run_id", metavar="run-id")
    p.add_argument("card_id", metavar="card-id")

    p = sub.add_parser("status", help="Print run summary")
    p.add_argument("run_id", metavar="run-id")

    args = parser.parse_args()
    cmds = {
        "new": cmd_new,
        "draw": cmd_draw,
        "commit-treaty": cmd_commit_treaty,
        "resolve": cmd_resolve,
        "unresolve": cmd_unresolve,
        "status": cmd_status,
    }
    cmds[args.command](args)


if __name__ == "__main__":
    main()
