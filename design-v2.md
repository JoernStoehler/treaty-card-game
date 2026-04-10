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

- **Treaty cards** (~15-20): enforcement mechanisms available to include in the treaty. Examples: "On-Site Inspections," "Export Controls," "Military Strikes," "Chip Serial Tracking." Each has a bold title and a short description phrased as what it lets the treaty do.

- **Threat cards** (~15-20, shuffled): story elements representing things that could challenge the treaty over the decades it must hold. Each has a bold title (readable at table distance), optional short description for disambiguation, and an illustration.
  - **Capability cards** (subset, ~6-8): threats that directly advance someone's ability to train superintelligence. Visually marked with a black border and corner icon. Examples: "GPU Theft," "Algorithmic Breakthrough," "Stolen Model Weights."
  - **Context cards** (the rest): threats that degrade the treaty's political/operational environment without directly providing training capability. Examples: "Chinese Invasion of Taiwan," "Treaty Inspector Assassinated," "Country Exits Treaty."

## Table layout

Four regions, organized as a 2x2 grid:

|  | Left (not active) | Right (in effect) |
|--|---|---|
| **Treaty cards** | Ideas pool (available provisions) | Active treaty (committed provisions) |
| **Threat cards** | Handled threats (resolved) | Unresolved threats (lingering) |

Right side = "what's currently true." Left side = "what's settled / not yet needed."

## Setup

1. Read rules aloud (short — see Rules section).
2. Split treaty cards into roughly equal hands among players. Each player reads their cards and becomes the expert on those provisions.
3. All treaty cards go face-up into the ideas pool (left side). Players retain knowledge of what they read.
4. Shuffle threat deck. Optionally set aside some cards face-down to vary game length (draw N of M).
5. One player takes the threat deck and becomes the reader.

## Game loop

1. **Reveal threat.** Reader draws the top threat card, reads the title aloud (big, everyone sees it), reads the description if any. Card goes to the unresolved area (right side).

2. **Discuss.** Players argue: does our current treaty handle this? They can reference any treaty card in the active treaty (right side). They can also propose moving new treaty cards from the ideas pool into the active treaty to handle it.

3. **Commit.** Players move treaty cards from ideas → active treaty as needed. Treaty cards committed in previous rounds cannot be removed. Cards committed this round can still be pulled back until the group finalizes.

4. **Resolve.** Group decides:
   - **Handled:** Threat card moves to handled pile (left side). The treaty addresses this.
   - **Unresolved:** Threat card stays on the right side. The treaty doesn't (or shouldn't, or can't) deal with this. If it's a capability card (black border), it counts toward the extinction threshold.
   - Players can also resolve previously unresolved threats if a newly committed treaty provision covers them. Move those threats from right → left.

5. **Check extinction.** If 3 (or N — playtest to determine) capability cards are unresolved on the right side, the game ends. Someone somewhere had enough resources to train superintelligence. Everyone dies.

6. **Next card.** Return to step 1.

## Game end

The game ends when:
- **Extinction:** 3+ capability cards unresolved. Loss.
- **Deck exhausted:** All threat cards drawn and resolved/unresolved. Proceed to reflection.

## Post-game reflection

Guided questions (printed on a reference card):
- Look at the active treaty. Would you sign it? Would China? Would a libertarian democracy?
- Which provision felt most necessary? Which felt hardest to justify?
- How close did you get to extinction? Did you get lucky, or is the treaty robust?
- (If applicable) Could you have won with fewer provisions?

## Card format: Threat cards

- **Border:** Black border with corner icon for capability cards. Non-black border (or neutral) for context cards.
- **Front:** Full-bleed illustration as background. Bold title across the card, large enough to read from across a table, clearly separated from background. Optional 1-2 sentence description below title for disambiguation (readable when card is picked up).
- **Back:** Uniform for all threat cards (cannot distinguish capability from context by looking at the back — suspense preserved).

Cards are story elements. They're short phrases that prompt discussion, not narrated scenarios. The card doesn't explain implications — players figure those out.

Examples of capability cards:
- "GPU Theft" — (no description needed, self-explanatory)
- "Algorithmic Breakthrough" — "Training now requires 100x less compute"
- "Stolen Model Weights"
- "Underground Datacenter"
- "Distributed Training" — "Consumer hardware coordinated across countries"
- "Legacy Hardware Stockpile" — "Pre-treaty GPUs consolidated into one facility"

Examples of context cards:
- "Country Exits Treaty"
- "Chinese Invasion of Taiwan"
- "Treaty Inspector Assassinated"
- "Whistleblower Reveals Surveillance Program"
- "AI Company Lobbying Campaign"
- "War in the Middle East"
- "North Korea Wants Superintelligence"

## Card format: Treaty cards

- **Border:** Category color (fluff — not mechanically meaningful, just visual grouping).
- **Front:** Bold title, large and readable. Illustration background. Description phrased as what the treaty provision lets you do, e.g., "Enter and search any facility without advance notice" rather than "The authority to conduct unannounced inspections." This tells players what argument they can make.
- **Back:** Uniform for all treaty cards (distinct from threat card backs so the two decks are never confused — different card layout, size, or back design).

Treaty cards are also short and concrete. The name should usually be enough; the description is for players unfamiliar with the concept.

## Framing

The game is a **stress test of hypotheticals**, not a timeline. Cards represent "what if this happened?" not "this happened in year 3." This means:
- No world-state bookkeeping beyond the table layout
- Players don't need to worry about temporal coherence between cards
- Retconning / adding provisions feels natural (you're iterating on a treaty draft)
- Post-game reflection works naturally ("would you sign this knowing these are the threats?")

## Design principles for writing cards

### Threat cards
- **Story elements, not scenarios.** A card is a phrase or short concept, not a narrated chain of events. "Bunker Datacenter" not "A group built a hidden datacenter in a converted mine shaft and completed a training run."
- **Every word must be decision-relevant.** If a detail doesn't affect which treaty mechanisms apply or how the argument goes, cut it. No numbers for atmosphere, no city names for flavor.
- **Some cards need no description.** "GPU Theft" speaks for itself. Only add a description when the concept is non-obvious to a general audience.
- **Descriptions disambiguate, not narrate.** One sentence max. It answers "what does this mean?" not "what happened?"
- **Capability cards represent direct training-run enablers.** Compute, algorithms, weights, operational infrastructure. Things that get someone closer to completing a training run.
- **Context cards represent political/operational degradation.** Things that make the treaty harder to enforce, weaker politically, or less credible. They don't directly enable a training run but they change the landscape.
- **Some cards are very hard or effectively unpreventable.** This is intentional. Not every threat is worth addressing — players can choose to let threats through if the treaty cost of preventing them is too high. Life's unfair; the game should reflect that.

### Treaty cards
- **Descriptions say what you CAN DO, not what the mechanism IS.** "Track every AI chip from fabrication to deployment by serial number" not "End-to-end chip supply chain tracking system."
- **More detail than threat cards.** It's more important for players to understand treaty mechanisms correctly than to understand every nuance of a threat scenario. Treaty card descriptions inform player creativity and argument quality.
- **Names should be plain language.** "On-Site Inspections" not "Article VII Verification Protocol."

## Open questions for playtesting

- **Extinction threshold:** Is 3 capability failures right? Might need 4 or 5. Playtest to calibrate.
- **Deck size:** Is 15 threat cards the right number for a 15-20 minute game? Depends on discussion time per card.
- **Treaty card count:** Too few = not enough tools. Too many = analysis paralysis in the ideas pool. 12-16 feels right.
- **Player count scaling:** With 1-2 players, use all treaty cards. With 4-5, does specialization via hand-splitting scale, or do too many players step on each other?
- **Familiarization phase length:** Does the "read your hand, become the expert" phase take 2 minutes or 10?
- **Retroactive resolution frequency:** How often do players actually clear old threats with new provisions? Is this a satisfying core mechanic or a rare edge case?
