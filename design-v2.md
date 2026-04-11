# Treaty Stress Test — v2 Design

## What the game is

A cooperative card game for 1-5 players. Players collectively build and defend a treaty banning superintelligent AI development against a deck of threat scenarios. Designed for rationalist meetups; rules explainable in under a minute, playable in 15-20 minutes.

## Educational goals

Players should come away understanding:
1. What treaty mechanisms exist and why each is necessary
2. What realistic threats the treaty faces
3. The political tradeoffs involved — is the resulting treaty one anyone would sign?

## Components

Two decks:

- **Treaty cards** (15): enforcement mechanisms available to include in the treaty. Each has a bold title. See `cards-v2.md` for the full list.

- **Threat cards** (30 total, half used per game): story elements representing things that could challenge the treaty over the decades it must hold. Each has a bold title (readable at table distance) and an illustration.
  - **Capability cards** (14): threats that directly advance someone's ability to train superintelligence. Visually marked with a black border and corner icon. One card (Recursive Self-Improvement) is unpreventable — no treaty provision can resolve it, and it permanently occupies an extinction slot when drawn.
  - **Context cards** (16): threats that degrade the treaty's political/operational environment without directly providing training capability.
  
  See `cards-v2.md` for the full list with design notes.

## Table layout

Four regions, organized as a 2x2 grid:

|  | Left (not active) | Right (in effect) |
|--|---|---|
| **Treaty cards** | Ideas pool (available provisions) | Active treaty (committed provisions) |
| **Threat cards** | Handled threats (resolved) | Unresolved threats (lingering) |

Right side = "what's currently true." Left side = "what's settled / not yet needed."

## Setup

1. Read the Game Loop and Game End sections aloud to all players.
2. **Familiarize with treaty cards.** Split treaty cards roughly equally among players. Each player reads their cards — they become the group's expert on those provisions. Then place all treaty cards face-up in the ideas pool (left side). Titles are large enough for everyone to see; players ask questions about cards they don't understand, answered by whoever read them.
3. Shuffle threat deck. Set aside half the deck face-down unseen — the game uses roughly half the threat deck. This controls game length and adds uncertainty about which threats appear.
4. One player takes the threat deck and becomes the reader. The reader role can rotate or stay fixed — group's choice.

## Game loop

1. **Reveal threat.** Reader draws the top threat card, reads the title aloud (big, everyone sees it). Card goes directly to the unresolved area (right side).

2. **Discuss and commit.** Players discuss all unresolved threats on the right side — not just the one just drawn. They can move treaty cards from the ideas pool into the active treaty. Treaty cards committed in previous rounds cannot be removed. Cards placed this round can be pulled back until the next threat is drawn, which locks them in.

3. **Resolve.** Players can move any threats from the right side (unresolved) to the left side (handled) if they argue the active treaty addresses them. This includes both the newly drawn threat and any previously unresolved threats. Retroactively resolving a capability card removes it from the extinction count. Decisions are by group consensus.

4. **Check extinction.** If 3 capability cards are unresolved on the right side, the game ends. Someone somewhere had enough resources to train superintelligence. Everyone dies.

5. **Next card.** Return to step 1.

## Game end

The game ends when:
- **Extinction:** 3+ capability cards unresolved. Loss.
- **Deck exhausted:** All cards in the subset drawn and resolved/unresolved. Proceed to reflection.

Surviving the deck without hitting the extinction threshold is a win — but the post-game reflection evaluates how good a win it was.

## Post-game reflection

Guided questions (printed on a reference card):
- Look at the active treaty. Would you sign it? Would China? Would a libertarian democracy?
- Which provision felt most necessary? Which felt hardest to justify?
- How close did you get to extinction? Did you get lucky, or is the treaty robust?
- (If applicable) Could you have won with fewer provisions?

## Card format: Threat cards

- **Border:** Black border with corner icon for capability cards. Non-black border (or neutral) for context cards.
- **Front:** Full-bleed illustration as background. Bold title across the card, large enough to read from across a table. Title only — no description text.
- **Back:** Uniform for all threat cards (cannot distinguish capability from context by looking at the back — suspense preserved).

Cards are story elements. They're short phrases that prompt discussion, not narrated scenarios. The card doesn't explain implications — players figure those out.

See `cards-v2.md` for the full card list with design notes.

## Card format: Treaty cards

- **Border:** Category color (fluff — not mechanically meaningful, just visual grouping).
- **Front:** Bold title, large and readable. Illustration background. Title only — no description text.
- **Back:** Uniform for all treaty cards (distinct from threat card backs so the two decks are never confused — different card layout, size, or back design).

Treaty card titles should convey what the provision lets the treaty DO. Players learn them during the familiarization phase at setup.

## Framing

The game is a **stress test of hypotheticals**, not a timeline. Cards represent "what if this happened?" not "this happened in year 3." This means:
- No world-state bookkeeping beyond the table layout
- Players don't need to worry about temporal coherence between cards
- Retconning / adding provisions feels natural (you're iterating on a treaty draft)
- Post-game reflection works naturally ("would you sign this knowing these are the threats?")

## Design principles for writing cards

### Threat cards
- **Story elements, not scenarios.** A card is a phrase or short concept, not a narrated chain of events.
- **Every word in the title must be decision-relevant.** If a word doesn't affect which treaty mechanisms apply or how the argument goes, cut it.
- **Titles should be self-explanatory** to the target audience (rationalist meetup attendees familiar with AI governance).
- **Capability cards represent direct training-run enablers.** Compute, algorithms, weights, operational infrastructure. Things that get someone closer to completing a training run.
- **Context cards represent political/operational degradation.** Things that make the treaty harder to enforce, weaker politically, or less credible. They don't directly enable a training run but they change the landscape.
- **Some cards are very hard or effectively unpreventable.** This is intentional. Not every threat is worth addressing — players can choose to let threats through if the treaty cost of preventing them is too high.

### Treaty cards
- **Titles say what you CAN DO, not what the mechanism IS.** "Routine Inspections" not "Article VII Verification Protocol."
- **Names should be plain language.** Players learn what each provision means during the familiarization phase at setup.

## Open questions for playtesting

- **Extinction threshold:** Starting at 3. Might need 4 or 5. Playtest to calibrate.
- **Deck subset size:** Is ~15 threat cards the right number for a 15-20 minute game? Depends on discussion time per card.
- **Player count scaling:** With 1-2 players, use all treaty cards. With 4-5, does specialization via hand-splitting scale, or do too many players step on each other?
- **Familiarization phase length:** Does the "read your hand, become the expert" phase take 2 minutes or 10?
- **Retroactive resolution frequency:** How often do players actually clear old threats with new provisions? Is this a satisfying core mechanic or a rare edge case?
