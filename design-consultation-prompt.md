# Expert Consultation: Card Game Design for AI Treaty Education

You are an expert in tabletop game design, serious games, and educational game mechanics. You have deep knowledge of cooperative card games (Pandemic, Spirit Island, Hanabi), negotiation games (Diplomacy, Cosmic Encounter), storytelling games (Fiasco, Once Upon a Time, Dixit), puzzle games (Mysterium, Codenames), and the theory behind what makes games fun, educational, and replayable.

## Context

We're designing a card game for small groups (1-5 players, typically 2-3) at rationalist meetups. The game teaches players about a proposed international treaty to ban the development of superintelligent AI. The treaty is modeled on real arms control frameworks (NPT, CWC, IAEA) and includes mechanisms like:

- Compute licensing and chip tracking (serial-number tracking from fabrication to deployment)
- On-site inspections and challenge inspections
- Export controls on AI hardware
- Research restrictions on capability-relevant AI research
- Whistleblower protections
- Enforcement escalation ladder (sanctions → cyber operations → military strikes)
- Chip consolidation into monitored facilities
- Financial tracking of compute procurement
- Treaty tribunal with binding authority

The threat landscape includes: chip smuggling, rogue researchers fleeing to non-signatory countries, underground datacenters, nations exiting the treaty, algorithmic breakthroughs reducing compute requirements, distributed training across consumer hardware, corporate defiance, autonomous AI agents, weight leaks, etc.

**The core educational goal:** Players should come away understanding (a) what treaty mechanisms exist and why each is necessary, (b) what realistic threats the treaty faces, and (c) the political tradeoffs involved (mass surveillance, military strikes, sovereignty violations — is the resulting treaty one anyone would sign?).

The game should be explainable in under a minute and playable in 15-20 minutes.

## Design Space We're Exploring

We have 9 open design axes and we'd like your expert opinion on the tradeoffs. For each axis, tell us what you'd recommend and why, drawing on precedents from existing games. Also tell us if we're missing options or if some of these axes aren't actually independent.

### 1. Card Content: How much does a threat card say?

| Option | Example |
|--------|---------|
| **Full narrative** | 3-4 sentences, complete chain of events with consequences |
| **Headline + brief** | "TAIPEI — 12,000 chips missing from fab inventory" + 1-2 factual details |
| **Headline only** | "War in the Middle East" |
| **Structured prompt** | Short text + explicit "if failed: [consequence]" |

### 2. Threat Card Types: Are cards mechanically uniform or differentiated?

| Option | Description |
|--------|-------------|
| **All uniform** | Every card works the same, failures just accumulate |
| **Two types: resource + narrative** | Resource cards are countable toward extinction; narrative cards add context but don't count mechanically |
| **Spectrum with tags** | Mostly uniform but some tagged "resource" |
| **All uniform, players decide** | Group judges whether a failed card "contributes to training capability" or not |

The reasoning behind "resource" cards: these represent things that directly enable a training run (compute, algorithms, weights, funding). Danger scales roughly exponentially with the count of these — each additional resource makes it more feasible that someone somewhere completes a training run. "Narrative" cards are things like political crises, diplomatic incidents, wars — they make the treaty harder to enforce but don't directly provide training capability.

### 3. Loss Condition: What triggers extinction?

| Option | Description |
|--------|-------------|
| **Fixed failure count** | e.g., 5 failures = loss |
| **Resource count threshold** | e.g., 5 resource-type failures = loss |
| **Explicit extinction cards** | Some cards say "EXTINCTION if [condition]" |
| **Player judgment** | "Could someone train ASI given what's failed?" |
| **No mechanical loss** | Always finish, reflect on how bad things got |
| **Graduated** | At N resource failures enter "red zone," next resource failure = extinction |

### 4. Treaty Selection: How do players get their tools?

| Option | Description |
|--------|-------------|
| **Random deal** | Deal from pool at game start |
| **Draft from full pool** | Players choose which provisions to include |
| **Budget pick** | Choose N of M available provisions |
| **Open pool, no limit** | Use whatever, reflect on political cost afterward |
| **Build as you go** | Start with nothing, add provisions in response to threats |
| **Pre-built + retcon** | Start with default treaty, modify as gaps appear |

### 5. Turn Structure: How are threats revealed?

| Option | Description |
|--------|-------------|
| **Sequential, one at a time** | Draw, discuss, resolve, repeat |
| **All at once** | Reveal all threats, plan treaty, then verify |
| **Sequential with free retcon** | Reveal one by one but treaty is always mutable; changing it might re-open previously resolved threats |
| **Batches** | Reveal 3-5 at a time, discuss, then next batch |

### 6. Time Semantics: What do the cards represent?

| Option | Description |
|--------|-------------|
| **Things that happened** | Timeline progresses, consequences are real |
| **Hypotheticals** | "What if this happened? Does your treaty handle it?" |
| **Ambiguous** | Players decide the framing |

### 7. Treaty Mutability: Can you change your treaty after committing?

| Option | Description |
|--------|-------------|
| **Locked once played** | Commitment has weight |
| **Freely mutable** | Pure optimization |
| **Mutable but risky** | Changing treaty might re-open resolved threats |
| **Limited retcons** | Fixed number of "take-backs" |

### 8. State Tracking: How much is mechanical vs. interpreted?

| Option | Description |
|--------|-------------|
| **Minimal** | Failed cards in a pile, players interpret significance |
| **Count only** | Track number of failures or resource failures |
| **Categorized** | Separate piles/tracks for different failure types |
| **Rich world state** | Failed cards face-up, actively referenced in future discussions |

### 9. Post-Game Reflection: How do you evaluate the treaty you built?

| Option | Description |
|--------|-------------|
| **Pure discussion** | "Would you sign this treaty?" |
| **Mechanical score** | Count provisions used, weight by political cost |
| **Guided questions** | Printed prompts like "which provision was hardest to justify?" |
| **None** | Game just ends |

## What We Want From You

1. For each axis: what would you recommend and why? What existing games inform your reasoning?
2. Are any of these axes not actually independent? (i.e., choosing one option on axis X forces or strongly suggests an option on axis Y)
3. Are we missing any important design axes?
4. Given the educational goal and the constraints (small groups, 15-20 minutes, explainable in under a minute), what combination of choices across these axes would you recommend as a starting point for playtesting?
5. Any creative ideas we haven't considered? Novel mechanics from games we might not know about?
