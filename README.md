# Treaty Stress Test — Card Game

A verbal card game for 1-5 players where players collectively defend a global ban on superintelligence against a deck of crisis scenarios. Designed for rationalist meetups; rules explainable in 30 seconds.

## Project Components

| Component | Purpose |
|---|---|
| `generate-image.py` | Generate card illustrations via FAL API (flux-dev model). Reads `definitions/`, checks which `images/` are missing, generates them. |
| `render-card.py` | Render card definitions into print-ready front PNGs. Reads `definitions/*.json` + `images/`, outputs `rendered/<id>-f.png`. |
| `print-layout.py` | Arrange rendered cards onto A4 pages for printing. Requires `--color` or `--greyscale` (no default). |

## Directory Layout

```
definitions/       Card definition JSON files (e.g. swat-raid.json)
images/            Generated card illustrations (committed, not regenerated)
rendered/          Rendered card front PNGs (output of render-card.py)
```

## Quick Commands

```bash
python3 generate-image.py --help    # Generate missing card illustrations
python3 render-card.py --help       # Render card definitions to PNGs
python3 print-layout.py --help      # Arrange cards for A4 printing
```

---

## Game Spec: Treaty Stress Test v0.1

A verbal card game for 1-5 players where players collectively defend a global ban on superintelligence against a deck of crisis scenarios. The game teaches real enforcement mechanisms from compute governance and arms control literature. Designed for rationalist meetups; rules explainable in 30 seconds.

### Components

- **Treaty clause cards** (~20-32): enforcement mechanisms players hold in hand and play onto crises
- **Event/crisis cards** (~15-20): scenarios that stress-test the treaty
- **Safety breakthrough cards** (3): interspersed in the event deck; collect all 3 to win

**Card dimensions:** 70x120mm (tarot size). Chosen for table visibility -- players flash cards without passing them. Print layout: 6 cards per A4 page (2 columns x 3 rows).

### Core Loop

1. Each player receives a hand of treaty clause cards (total pool divided among players)
2. Shuffle crisis cards + 3 safety cards into one event deck
3. Draw top card, read aloud
4. If safety card -> set aside, celebrate. Collect 3 = win.
5. If crisis card -> group argues whether their played/held treaty clauses handle it
6. Vote: handled (clause cards used move to "active treaty" on table) or failed (card goes to failure pile)
7. Some crisis cards have escalation tiers keyed to current failure count -- only the matching tier is read aloud
8. Players have 3 retcons total: spend one to play a clause card from hand retroactively onto a past failure, flipping it to handled (must articulate why the clause would have prevented it)
9. Loss: crisis card whose active tier says "EXTINCTION"
10. Win: 3 safety breakthroughs collected, or survive the entire deck

**5-minute mode:** ~10 cards (8 crisis + 2 safety), smaller clause hand
**15-minute mode:** ~21 cards (18 crisis + 3 safety), full clause hand

### Card Types and Schemas

**Treaty clause card** (`treaty-flat`):
```json
{
  "type": "treaty-flat",
  "id": "swat-raid",
  "name": "SWAT Raid",
  "description": "Armed law enforcement raids suspected sites",
  "category": "enforcement",
  "color": "#c0392b",
  "prompt": "...",
  "image": "images/swat-raid.png"
}
```

Categories and border colors:
- enforcement: #c0392b (red)
- intelligence: #8e44ad (purple)
- compute: #2980b9 (blue)
- monitoring: #27ae60 (green)
- legal: #d4a017 (gold)

**Event/crisis card** (`event-flat`):
```json
{
  "type": "event-flat",
  "id": "garage-cluster",
  "name": "Garage Cluster",
  "scenario": "A private citizen builds a 20-GPU cluster in their basement. Neighbors report unusual power bills.",
  "tiers": [
    { "max_failures": 1, "text": "Local police investigate." },
    { "max_failures": 99, "text": "They've been training for months undetected." }
  ],
  "prompt": "...",
  "image": "images/garage-cluster.png"
}
```

Tier display: each tier box shows its failure-range label and text. The currently active tier must be instantly identifiable during play. Design the boxes so a player glancing at the card knows which to read without counting.

**Safety breakthrough card** (`safety-flat`):
```json
{
  "type": "safety-flat",
  "id": "interpretability-solved",
  "name": "Interpretability Solved",
  "description": "Researchers can now fully read model intentions before deployment.",
  "prompt": "...",
  "image": "images/interpretability-solved.png"
}
```

### Layout Per Card Type

- **treaty-flat:** Category color as left border stripe (wide, ~5mm). Name in bold at top. Illustration fills upper ~60%. Description below illustration. Category label small at bottom corner.
- **event-flat:** Dark/red-tinted frame. Name at top over illustration. Scenario text in middle section. Tier boxes stacked at bottom -- each box has failure-range label on the left and escalation text on the right. Boxes must be visually distinct from each other (e.g. increasing intensity of red/warning styling at higher failure counts).
- **safety-flat:** Green-tinted card, visually distinct from other types (players should spot these instantly when drawn from the deck). Name at top. Illustration fills upper portion. Description below.

### Print Notes

- Front only for playtesting (backs come later; `-f` suffix convention reserves space for `-b`)
- Color preferred but greyscale must remain legible (category colors should differ enough in value/lightness)
- No background texture for playtesting
- Target deck size: 20-55 cards total across all types (4-10 A4 pages at 6 cards/page)

### Demo Cards

| ID | Type | Category |
|---|---|---|
| swat-raid | treaty-flat | enforcement |
| research-ban | treaty-flat | -- |
| garage-cluster | event-flat | -- |
| rogue-researcher | event-flat | -- |
| interpretability-solved | safety-flat | -- |
| formal-verification | safety-flat | -- |

Card definitions are authored by hand (not generated). Image prompts require human iteration.
