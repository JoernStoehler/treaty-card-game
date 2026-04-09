I created a new empty repo for a new project (1h planning so far).
The README.md should cover the project components — it is the project manifest/spec.
My first spontaneous guess is that the following aspects go into the repo/project:

* basic infrastructure:
   * install gh and other development / software dependencies in the claude code startup hook
   * in the same hook alert claude code when FAL_KEY envvar is not provided by the environment
   * CLAUDE.md with the project conventions and general knowledge for agents
      * the README.md is the project manifest/spec — the single source of truth for what the project is, what it contains, and how the pieces fit together
      * we KISS & YAGNI - never create something prematurely just bc somebody *may* need it in the future - not even if that's already scheduled - wait until "first use" to nail down what is needed and implement it then
      * use subagents (sonnet) for implementing, testing, refactoring, analyzing writing etc ; no reason to wait for slower opus subagents or waste valuable content window yourself ; aggressively clean/refactor code & writing to be focused, maintainable and high quality ; subagents can analyze a code file for you and fix minor things on the go that don't require your whole-picture-based decision
      * never write the FAL_KEY secret envvar down anywhere
      * standard flat repo layout - no reason to hide things from agents ; put everything into the standard location where you'd look (or even actually looked) for something first
      * quick commands section that is later filled up more (once scripts etc exist - not prematurely)
      * escalate whenever something is too surprising to be straightforwardly dealt with (e.g. no api key in environment, assumption that Jörn made is wrong, ...) since it can affect (to you surprising) other parts of the project
   * this very prompt goes into "initial-prompt.md" 1:1 for posterity / for future agents to have a headstart / context
* text-to-image capabilities: a script
   * look up the syntax for the FAL api, probably curl is sufficient here, and wrap it in a script (python? bash? node? your call, depending on what's available - ask a subagent to compare the different approaches and pivot early on trouble/complexity)
   * we will need to control model, prompt, aspect, output path , other parameters are *afaik* not needed yet - and per YAGNI that means you should just pick static values for them that are recommended by the api guides as robust & best practice - or inform me when no such static value is available (escalate!)
   * avoid default values that aren't static values - better if agents explicitly set what can/should be set
   * useful --help instructions - don't spam CLAUDE.md:quickstart with subcommands, just mention "--help" and the script's purpose and that's good enough
   * format: i recommend (but don't demand) png, with metadata for later analysis written into the png ; pngs should be committed to be shared across agent sessions and not require expensive regeneration ; maybe an images/ folder ?
* a script that takes a card definition (see next point) and turns it into a print-ready (see next-next point) image ; definitions go into definitions/ and the rendered card fronts into rendered/ ; e.g. "images/swat-raid.png, definitions/swat-raid.json, rendered/swat-raid-f.png"
* different templates for different layout variants of cards - we don't want to support something flexible here, so I suggest sth as the DSL for card definitions like json with a "type": string tag and then the other fields depend on what type that is. For now 3 card types are enough: "event-flat" | "treaty-flat" | "safety-flat" ; I suggest you don't overcomplicate things - maybe just define for each layout type a html template string that gets interpolated with the card's data ? and then refactoring has to touch each template string - but that's still KISS and YAGNI. We will later maybe go up to ~6 types, not more.
* a script that takes the rendered cards and arranges them for printing ; for now focus on playtesting not professional printing, so A4 paper in color OR greyscale (--greyscale XOR --color as options; your call what is the standard way to flip between two values without having a default). Color is more expensive for me than paper, but simplicity and standardness matters here more (get things done, agents must be able to reason cheaply about things they already are familiar with from training).
* target deck size is 20-55 cards total across all types. print layout should handle this range (that's 4-10 A4 pages at 6 cards/page).
* finally let's aim for 2 demo cards for each of the 3 types, including 1 generated image for each card (the illustration). For playtesting I don't print backgrounds, so per YAGNI the rendering script outputs only "rendered/<card>-f.png" for the front. The -f suffix convention exists because card backs (-b) will come later — don't hardcode single-side assumptions too deep.
   * demo cards: "swat-raid", "research-ban" (treaty); "garage-cluster", "rogue-researcher" (event); "interpretability-solved", "formal-verification" (safety)
   * ask Jörn for the card definitions/content once the rendering pipeline works — he has the full card list ready
   * the image generation prompt is part of each card's definition json ("prompt" field). The image gen script reads definitions/, checks which images/ are missing, and generates them. Jörn hand-writes the prompt strings since image model prompting requires human iteration.

The game spec below goes into the README.md as part of the project manifest (not a separate file).

---

## Game Spec: Treaty Stress Test v0.1

A verbal card game for 1-5 players where players collectively defend a global ban on superintelligence against a deck of crisis scenarios. The game teaches real enforcement mechanisms from compute governance and arms control literature. Designed for rationalist meetups; rules explainable in 30 seconds.

### Components

- **Treaty clause cards** (~20-32): enforcement mechanisms players hold in hand and play onto crises
- **Event/crisis cards** (~15-20): scenarios that stress-test the treaty
- **Safety breakthrough cards** (3): interspersed in the event deck; collect all 3 to win

**Card dimensions:** 70×120mm (tarot size). Chosen for table visibility — players flash cards without passing them. Print layout: 6 cards per A4 page (2 columns × 3 rows).

### Core loop

1. Each player receives a hand of treaty clause cards (total pool divided among players)
2. Shuffle crisis cards + 3 safety cards into one event deck
3. Draw top card, read aloud
4. If safety card → set aside, celebrate. Collect 3 = win.
5. If crisis card → group argues whether their played/held treaty clauses handle it
6. Vote: handled (clause cards used move to "active treaty" on table) or failed (card goes to failure pile)
7. Some crisis cards have escalation tiers keyed to current failure count — only the matching tier is read aloud
8. Players have 3 retcons total: spend one to play a clause card from hand retroactively onto a past failure, flipping it to handled (must articulate why the clause would have prevented it)
9. Loss: crisis card whose active tier says "EXTINCTION"
10. Win: 3 safety breakthroughs collected, or survive the entire deck

**5-minute mode:** ~10 cards (8 crisis + 2 safety), smaller clause hand
**15-minute mode:** ~21 cards (18 crisis + 3 safety), full clause hand

### Card types and schemas

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

### Layout per card type

- **treaty-flat:** Category color as left border stripe (wide, ~5mm). Name in bold at top. Illustration fills upper ~60%. Description below illustration. Category label small at bottom corner.
- **event-flat:** Dark/red-tinted frame. Name at top over illustration. Scenario text in middle section. Tier boxes stacked at bottom — each box has failure-range label on the left and escalation text on the right. Boxes must be visually distinct from each other (e.g. increasing intensity of red/warning styling at higher failure counts).
- **safety-flat:** Green-tinted card, visually distinct from other types (players should spot these instantly when drawn from the deck). Name at top. Illustration fills upper portion. Description below.

### Print notes

- Front only for playtesting (backs come later)
- Color preferred but greyscale must remain legible (category colors should differ enough in value/lightness)
- No background texture for playtesting (YAGNI)
