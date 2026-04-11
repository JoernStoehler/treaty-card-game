# Treaty Stress Test — Card Game

A cooperative card game for 1-5 players. Players collectively build and defend a treaty banning superintelligent AI development against a deck of threat scenarios. Teaches real enforcement mechanisms from compute governance and arms control literature. Designed for rationalist meetups; explainable in under a minute, playable in 15-20 minutes.

## Project State

The game is being redesigned (v2). The current design and card list are in:

- **`design-v2.md`** — Game mechanics, rules, table layout, card format
- **`cards-v2.md`** — All card definitions with design notes and deleted-card rationale

Tooling (`render-card.py`, `playtest.py`, `playtest-web/`) is from v1 and not yet updated for v2.

## Source Material

| File | Content |
|------|---------|
| `literature/iabied-treaty.md` | Yudkowsky/Soares annotated draft treaty (IABIED) |
| `literature/miri-tech-governance-treaty-2025.md` | Scher et al. arXiv 2511.10783 |
| `literature/iabied-book.md.enc` | Encrypted IABIED book |

## Quick Summary of v2 Design

**Two decks:** Treaty cards (15 provisions) and Threat cards (30 story elements, half used per game).

**Setup:** Players split treaty cards for familiarization, then pool them face-up. Shuffle and set aside half the threat deck unseen.

**Each turn:** Reveal a threat → discuss → commit treaty provisions → resolve threats (any on the table, not just the new one) → check extinction.

**Loss:** 3+ unresolved capability threats (black border) = extinction.
**Win:** Survive the deck subset. Post-game: reflect on whether the treaty is signable.

**Cards are story elements** — short titles that prompt discussion, not narrated scenarios. The game is playable from titles alone.

See `design-v2.md` for full rules and `cards-v2.md` for the card list.

## Legacy (v1)

The `playtests/` directory contains transcripts and synthesis from v1 playtesting (runs 001-004). The `handoffs/` directory contains v1 design synthesis. These informed the v2 redesign but describe the old mechanics (tiers, safety cards, failure count, retcons).

Tooling from v1:

| Component | Purpose | Status |
|---|---|---|
| `generate-image.py` | Generate card illustrations via FAL API | v1 — not yet needed for v2 |
| `render-card.py` | Render card definitions to print-ready PNGs | v1 — needs schema update for v2 |
| `print-layout.py` | Arrange rendered cards into print-ready PDF | v1 — works once render-card updated |
| `playtest.py` | Manage playtest runs with per-run state | v1 — needs mechanic update for v2 |
| `playtest-web/` | Solo playtest web app (treaty-playtest.pages.dev) | v1 — needs full rewrite for v2 |

## Card Dimensions

70x120mm (tarot size). 6 cards per A4 page (2 columns x 3 rows). Digital: 827x1417 pixels @ 300 DPI.
