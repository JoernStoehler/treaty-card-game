#!/usr/bin/env python3
"""Draw a random card from the event/safety deck.

Maintains deck state in a temp file so cards aren't repeated within a game.
Use --reset to reshuffle (must be called before the first draw of a new game).
"""
import json, os, random, sys

DECK_STATE = "/tmp/treaty-deck.json"

def build_deck():
    """Build and shuffle the event+safety deck."""
    cards = []
    for f in sorted(os.listdir("definitions")):
        if not f.endswith(".json"):
            continue
        with open(f"definitions/{f}") as fh:
            card = json.load(fh)
        if card["type"] in ("event-1", "event-2", "safety"):
            cards.append(card)
    random.shuffle(cards)
    return cards

if "--reset" in sys.argv or not os.path.exists(DECK_STATE):
    deck = build_deck()
else:
    with open(DECK_STATE) as f:
        deck = json.load(f)

if not deck:
    print('{"type": "deck-empty"}')
    sys.exit(0)

card = deck.pop(0)

with open(DECK_STATE, "w") as f:
    json.dump(deck, f)

print(json.dumps(card, indent=2))
