# Treaty Stress Test — Card Game

A verbal card game for 1-5 players where players collectively defend a global ban on superintelligence against a deck of crisis scenarios. Designed for rationalist meetups; rules explainable in 30 seconds.

## Project Components

| Component | Purpose |
|---|---|
| `generate-image.py` | Generate card illustrations via FAL API (flux-schnell). Reads `definitions/`, checks which `images/` are missing, generates them. |
| `render-card.py` | Render card definitions into print-ready front PNGs. Reads `definitions/*.json` + `images/`, outputs `rendered/<id>-f.png`. |
| `print-layout.py` | Arrange rendered cards into a print-ready PDF. Requires `--color` or `--greyscale` (no default). Outputs `print/cards.pdf`. |
| `playtest.py` | Manage playtest runs with per-run state. Subcommands: `new`, `deal`, `draw`, `status`. Enables parallel playtests. |
| `playtest-web/` | Mobile-first solo playtest web app. Static site (html + js), deployed to Cloudflare Pages. Draw events, select treaty cards, resolve, copy transcript. |

## Directory Layout

```
definitions/       Card definition JSON files (e.g. swat-raid.json)
images/            Generated card illustrations (committed, not regenerated)
rendered/          Rendered card front PNGs (output of render-card.py)
print/             Print-ready PDF (output of print-layout.py, gitignored)
playtests/         Playtest run logs, state files, card snapshots, and synthesis
playtest-web/      Solo playtest web app (index.html, app.js, cards.js)
```

## Quick Commands

```bash
python3 generate-image.py --help    # Generate missing card illustrations
python3 render-card.py --help       # Render card definitions to PNGs
python3 print-layout.py --help      # Arrange cards into print-ready PDF
python3 playtest.py --help          # Manage playtest runs (new/deal/draw/status)
```

---

## Game Spec: Treaty Stress Test v0.1

A verbal card game for 1-5 players where players collectively defend a global ban on superintelligence against a deck of crisis scenarios. The game teaches real enforcement mechanisms from compute governance and arms control literature. Designed for rationalist meetups; rules explainable in 30 seconds.

### Components

- **Treaty clause cards** (34): enforcement mechanisms players hold in hand and play onto crises
- **Event/crisis cards** (16): scenarios that stress-test the treaty
- **Safety breakthrough cards** (3-4): interspersed in the event deck; collect 3 to win

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

**Treaty clause card** (`treaty`):
```json
{
  "type": "treaty",
  "name": "SWAT Raid",
  "description": "Armed law enforcement raids suspected sites",
  "category": "enforcement",
  "color": "#c0392b",
  "image-prompt": "...",
  "image": "images/swat-raid.png"
}
```

Categories and border colors:
- enforcement: #c0392b (red) — kinetic and physical responses, from raids to airstrikes
- intelligence: #8e44ad (purple) — information gathering, surveillance, infiltration
- monitoring: #27ae60 (green) — institutional oversight, tracking, inspections
- legal: #d4a017 (gold) — rules and prohibitions. **Note:** legal cards only make activities illegal. This gives enforcement legal cover but doesn't stop determined violators. Players must argue not just that something is illegal, but that the illegality *matters*.
- institutional: #16a085 (teal) — treaty governance, diplomacy, membership mechanisms
- consolidation: #e67e22 (orange) — bringing pre-existing hardware, companies, and research under treaty control

**Event card, flat** (`event-1`, always a crisis regardless of failure count):
```json
{
  "type": "event-1",
  "name": "Chip Smuggling Ring",
  "text": "AI chips were diverted through shell companies to undeclared buyers. The chips surfaced in a facility in a non-signatory nation. A training run is underway.",
  "image-prompt": "...",
  "image": "images/chip-smuggling.png"
}
```

**Event card, tiered** (`event-2`, tier determined by failure count):
```json
{
  "type": "event-2",
  "name": "Garage Cluster",
  "label1": "1–2 failures",
  "text1": "A frontier model was trained in a makeshift garage data center. The results are on the dark web.",
  "label2": "3+ failures",
  "text2": "Consumer gaming hardware is being repurposed for AI training in garages and basements across the country. Several groups claim to have trained capable models.",
  "image-prompt": "...",
  "image": "images/garage-cluster.png"
}
```

Tier display: each tier box shows its label and text. The currently active tier must be instantly identifiable during play. Design the boxes so a player glancing at the card knows which to read without counting.

**Safety breakthrough card** (`safety`):
```json
{
  "type": "safety",
  "name": "Safety Breakthrough",
  "image-prompt": "...",
  "image": "images/safety-1.png"
}
```

### Layout Per Card Type

- **treaty:** Category color as left border stripe (wide, ~5mm). Name in bold at top. Illustration fills upper ~60%. Description below illustration. Category label small at bottom corner.
- **event-2:** Dark/red-tinted frame. Name at top over illustration. Tier boxes stacked at bottom -- each box has its label on the left and escalation text on the right. Boxes must be visually distinct from each other (e.g. increasing intensity of red/warning styling at higher failure counts).
- **safety:** Green-tinted card, visually distinct from other types (players should spot these instantly when drawn from the deck). Name at top. Illustration fills upper portion. Description below.

### Print Notes

- Front only for playtesting (backs come later; `-f` suffix convention reserves space for `-b`)
- Color preferred but greyscale must remain legible (category colors should differ enough in value/lightness)
- No background texture for playtesting
- Target deck size: 20-55 cards total across all types (4-10 A4 pages at 6 cards/page)

### Current Deck

**Treaty cards (34):**
- enforcement (8): Airstrike, Border Interdiction, Chip Seizure, Covert Sabotage, Economic Sanctions, Nuclear Strike, Offensive Cyber Ops, SWAT Raid
- intelligence (6): Financial Surveillance, Human Intelligence, Power Grid Monitoring, Satellite Surveillance, Signals Intelligence, Whistleblower Network
- monitoring (5): Challenge Inspection, Chip Registry, Compute Escrow, Network Traffic Analysis, On-Site Inspectors
- legal (7): Algorithm Publication License, Distributed Compute Cap, Fab Plant Licensing, FLOP Threshold, License Revocation, Research Ban, Supply Chain Audit
- institutional (5): Diplomatic Pressure, Export Controls, Membership Incentives, Treaty Tribunal, Withdrawal Penalty
- consolidation (3): Hardware Amnesty, Legacy Decommission, Research Archive Freeze

**Event-1 cards (14):** AI-Assisted Violence, Bioweapon Blueprint, Chip Leverage, Chip Smuggling Ring, Corporate Lobbying Blitz, Economic Entanglement, Failed Raid, Fake Compliance Report, Insider Sabotage, Legacy Hardware, Nation Exits Treaty, Public Backlash, Rogue Researcher, Whistleblower Bombshell

**Event-2 cards (12):** Algorithmic Breakthrough, Autonomous Agent, Cyber Attack, Distributed Training, Garage Cluster, Open-Source Weights Leak, Preprint Cascade, Pro-ASI Movement, Satellite Tip, Underground Datacenter, Weight Heist, Zero-Day Cascade

**Safety cards (5):** Safety Breakthrough x5 (different art, collect 3 to win)

**Event deck:** 26 events + 5 safety = 31 cards.

Card definitions are authored by hand (not generated). Image prompts require human iteration.

### Writing Good Event Cards

Event card text describes a **past-tense chain of events** where each sentence is a point the treaty could have intercepted. Players argue where their treaty would have broken the chain — either by preventing a step ("Chip Registry catches this at step 1") or by responding after the fact ("Challenge Inspection discovers it at step 3").

**Principles:**

1. **Event chains, not situations.** Each sentence is a step that happened. "AI chips were diverted through shell companies. The chips surfaced in a non-signatory nation. A training run is underway." — three interception points.
2. **Never prescribe responses or outcomes.** Don't write "police investigate" or "defenses hold." The card describes what went wrong; players decide how their treaty handles it.
3. **Standalone tiers.** Each tier must be readable without the others. Don't reference other tiers or assume they were read.
4. **Tiers differ in difficulty, not relevance.** Every drawn card is a real decision. Tier 1 at low failures is an easier challenge (most treaties handle it). Tier 2 at high failures is harder because leaked capabilities compound the threat.
5. **No negative statements.** Say what IS happening, not what ISN'T. "Not enough leaked methods" confuses readers.
6. **No slop.** Impressive-sounding details ("500 nodes across 30 countries") that don't help players argue are filler. Every word must earn its place.
7. **Ambiguity is a feature.** "Underground Datacenter" being possibly literal opens creative play. Don't over-specify when vagueness invites interesting arguments.
8. **Failure count = leaked capability.** The narrative meaning of failures: more compute, algorithms, and research are in the wild outside treaty control. Event-2 tiers reflect this — higher failures mean the same category of threat is compounded by prior leaks.
