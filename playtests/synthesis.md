# Playtest Synthesis — Runs 001–003

Three AI-simulated playtest runs using the same 3 personas (Mark, Natalie, Josh), the same 34 treaty cards, and varying random event draws. Results: 2 wins (runs 1 and 3, 2 failures each), 1 loss (run 2, 4 failures). Total: 27 turns across all 3 games.

## Card Assessment

### Strong and Reliable Cards

- **Supply Chain Audit** — played in all 3 runs, always effective for hardware tracking (run 1 turn 1, run 2 turn 2, run 3 turn 2). Consistent workhorse.
- **Challenge Inspection** — played in all 3 runs for reactive verification; works well paired with intelligence cards.
- **Withdrawal Penalty** — cleanly resolves treaty-exit scenarios (run 1 turn 4).
- **On-Site Inspectors** — physical presence is resilient to cyber attacks (run 1 turn 3).
- **Chip Seizure** — effective when facility location is known (run 1 turn 9).
- **Chip Registry** — strong hardware tracking when combined with **Supply Chain Audit** (run 1 turns 5–6).

### Overpowered Combos

- **Chip Registry + Supply Chain Audit** — flagged overpowered in runs 1 and 3. Together they cover different parts of the supply chain, making any hardware violation detectable. Consider errata, merging, or event cards that specifically counter this combo.
- **Challenge Inspection + any intelligence card** — too broadly applicable; "unannounced within 48 hours" resolves roughly 40% of physical-site events (flagged in runs 2 and 3).

### Weak and Dead Cards

- **Hardware Amnesty** — never came up in any run. Requires very specific setup (legacy hardware in violation) that no event triggers.
- **Membership Incentives** — no scenario arose organically where recruiting a non-signatory was relevant.
- **Nuclear Strike** — joke card, correctly never used.
- **Satellite Surveillance** — unused entirely in run 1; used in run 3 only as part of an obvious 2-card solution. Card flavor is too narrow (datacenter thermal signatures).
- **SWAT Raid** — run 3's Failed Raid turn was the game's best moment precisely because **SWAT Raid** does NOT address legal obstruction. The card is realistic but punishing when courts block enforcement.

### Unclear and Confusing Cards

- **Research Archive Freeze** — players unsure whether it covers model weights or only research papers and methods (runs 2, 3).
- **Distributed Compute Cap** — "compute-pooling software platforms" is ambiguous; doesn't reach P2P or informal coordination (runs 1, 2).
- **Offensive Cyber Ops** — unclear whether it can be used defensively mid-attack or only as a counterpunch after attribution (run 2).
- **Research Ban** — not retroactive; useless after damage is done (runs 1, 2). Needs a scenario that activates it BEFORE damage occurs.

## Treaty Gaps

No existing card covers these threat categories:

1. **Distributed and informal compute** — P2P home GPU networks, botnet-scale training. FLOP Threshold and Satellite Surveillance can't detect sub-datacenter-scale distributed runs. Failed in runs 1 and 2.
2. **Information proliferation** — can't undo published research or leaked weights. **Research Ban** isn't retroactive; **Research Archive Freeze** doesn't cover already-public material. Failed in all 3 runs (Rogue Researcher, Open-Source Weights Leak events).
3. **Algorithmic capability tracking** — once efficiency improvements are discovered, FLOP Threshold becomes irrelevant. No card tracks capability rather than compute. Failed in run 2.
4. **AI-speed cyberattacks** — a superhuman AI model attacking treaty infrastructure faster than human defenders can respond. No defensive infrastructure cards exist. Failed in run 2.
5. **Legal obstruction of enforcement** — courts blocking treaty operations (72-hour injunction in run 3). **SWAT Raid** doesn't override courts; **Treaty Tribunal** establishes supremacy but must already be part of an active treaty.

## Rules Issues

1. **Loss condition undefined in practice** — the README says "crisis card whose active tier says EXTINCTION" but no event card in the deck has an EXTINCTION tier. The playtester agent substituted "4 failures" as the loss condition. Open decision: implement EXTINCTION tiers on some event-2 cards, or switch to a flat failure threshold.
2. **Event-2 tier labels inconsistent** — most cards use "0–1 failures" / "2+ failures", but Garage Cluster uses "1–2 failures" / "3+ failures", and Algorithmic Breakthrough + Open-Source Weights Leak use "0 failures" / "1+ failures". The variation caused confusion in all 3 runs.
3. **Event-2 discard rule confusing** — "if failure count is below the lowest tier's range, discard and draw again" is hard to parse. Most cards start at 0 so it rarely triggers; Garage Cluster at 0 failures would be discarded. Needs a worked example.
4. **"Illegality must matter" not in printed rules** — the README states that legal cards only make things illegal and players must argue illegality matters, but this isn't in the playtester agent's rules or on the cards. Enforcing it strengthens play significantly.
5. **Active treaty reuse not intuitive** — by turn 7 in run 3, players correctly referenced cards from turn 1 without replaying them, but it wasn't instinctive until then. New players need a reminder mechanism.
6. **Multiple cards per turn removes tension** — run 1 noted that players frequently played 2+ cards simultaneously without hard choices. Suggested: limit to 1 card per player per turn.
7. **Retcon mechanic never tested** — 3 retcons exist in the rules but were never used across 27 total turns in 3 games. Either the mechanic is dead or the scenarios didn't pressure players enough to need retroactive plays.

## Balance

- **Results:** 2 wins (runs 1, 3 with 2 failures each), 1 loss (run 2 with 4 failures).
- **Game tends slightly easy** — both wins collected 3 safety cards before serious pressure arrived.
- **Safety card clustering creates tempo swings** — runs 1 and 3 had safety cards cluster in the second half or early middle, releasing pressure at convenient moments.
- **Early failure spiral is brutal** — run 2's 3 consecutive failures caused every subsequent event-2 card to hit the hard tier, creating an unrecoverable snowball.
- **Hand composition matters** — run 1 had a balanced spread across categories; run 2's random deal left gaps that directly contributed to the loss.

## Untested Event Cards

10 event cards were never drawn across all 3 runs (26 total event draws):

- **Event-1 (6):** AI-Assisted Violence, Bioweapon Blueprint, Chip Leverage, Economic Entanglement, Public Backlash, Whistleblower Bombshell
- **Event-2 (3):** Pro-ASI Movement, Weight Heist, Zero-Day Cascade

(Autonomous Agent appeared in run 3.)

## Prioritized Action Items

1. **Resolve loss mechanic** — decide between EXTINCTION tiers on event-2 cards or a flat failure threshold; implement whichever is chosen.
2. **Standardize event-2 tier labels** — pick one convention across all 12 event-2 cards.
3. **Review Chip Registry + Supply Chain Audit power** — consider errata, merging, or event cards that specifically counter this combo.
4. **Clarify card scopes** — **Research Archive Freeze** (weights vs. papers), **Distributed Compute Cap** (platforms vs. P2P), **Offensive Cyber Ops** (defensive mid-attack use).
5. **Add "illegality must matter" to game rules** — explicitly in the README and on the legal-category card template.
6. **Design new cards for treaty gaps** — priority: distributed compute and information proliferation.
7. **Run playtests covering untested cards** — use `playtest.py` tooling for parallel runs targeting the 10 unseen cards.
8. **Diversify personas** — test with different personality combinations and player counts (2 players, 4–5 players).

## Solo Playtest Feedback (Jörn, 2026-04-10)

First mobile playtest via treaty-playtest.pages.dev. Key observations:

### Political-pressure events don't work
**Corporate Lobbying Blitz** and **Public Backlash** model internal treaty politics (council being lobbied, public pressure to weaken treaty). None of the 34 clause cards are designed for this — they're all outward-facing enforcement mechanisms. Result: zero agency, auto-fail. **Decision: cut both cards.** Modeling governments as external actors that change the treaty is fine — that's what institutional cards (Withdrawal Penalty, Diplomatic Pressure) handle.

### Card design process rethink (proposed)
- **Generalize treaty cards?** Some cards (e.g., SWAT Raid) may be too narrow/concrete. More abstract cards could encourage creative argumentation ("armed enforcement response" vs. "SWAT team specifically").
- **Use simplified treaty language** on cards to explain what adding the card to the treaty roughly implies — or leave it to player imagination (often the name is enough).
- **Provide context for non-experts** — e.g., explain the difference between ground troops and espionage, so players unfamiliar with governance mechanisms can still argue effectively.
- **Card count tension** — too few cards harms creativity just as too many do. Overlap between cards can be resolved through discussion, which IS the game. Need to find the sweet spot.
- **Avoid card explosion** — resist adding cards for every gap. Better to have fewer, more versatile cards that players must creatively apply.

These observations suggest a broader card redesign pass, deferred for a future session.

## Methodology Notes

### What Works Well

- Playtester agent with 3 distinct personas generates authentic disagreement.
- `playtest.py` prevents cherry-picking — random draws force genuine responses to difficult situations.
- Honest failures are the most valuable output — runs 1 and 3's best moments were failures that exposed real treaty gaps.
- Post-game design notes capture card-level and rules-level feedback in one place.

### What to Improve

- Run more than 3 games before the next card iteration — n=3 leaves many cards untested.
- Vary persona sets; currently all 3 runs used Mark, Natalie, and Josh.
- Test with 2 and 4–5 players to check hand-size and tension dynamics.
- Use `playtest.py` per-run state to run multiple games in parallel.
- Save card snapshots (`.cards.jsonl`) alongside each run so that definition changes are tracked over time.
