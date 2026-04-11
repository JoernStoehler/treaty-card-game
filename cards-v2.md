# Card Definitions — v2

Card list for the redesigned Treaty Stress Test. Cards are title-only — the game is playable from bold titles that prompt discussion. Notes below are design rationale, not printed on cards.

## Capability Threats (black border, count toward extinction)

Things that directly advance someone's ability to train superintelligence.

### Compute

| Title | Notes |
|-------|-------|
| Chip Theft | Hardware stolen from tracked supply chain |
| Chip Smuggling | Illegal movement across borders |
| Legal Chip Sales | AI chips sold legally to buyers outside the monitoring regime. The point: if it's legal, players have to accept higher compute availability or restrict legal commerce |
| Legacy Hardware Stockpile | Pre-treaty hardware consolidated. Also covers chips produced before treaty tightening |
| Repurposed Consumer Chips | NOT new chips getting better — old GPUs with community-made drivers, networking via soldering, etc. |
| Distributed Training | Training split across many locations. No single facility to shut down. Tests whether the treaty's facility-based monitoring architecture works |
| Independent Chip Factory | Someone builds a fab, bypassing the TSMC/ASML chokepoint the treaty relies on |

### Knowledge

| Title | Notes |
|-------|-------|
| Algorithmic Breakthrough | Usually from ML research by labs, universities, hobbyists, or companies. Pure theory also valid over a 20-year horizon |
| Stolen Model Weights | Trained model exfiltrated and proliferating |

### Training run events

| Title | Notes |
|-------|-------|
| Corporate Defiance | A major lab secretly completes a training run |
| Signatory Races to Train | A treaty member secretly trains using monitored infrastructure. Distinct from Country Exits Treaty: they haven't left, they're cheating |

### Structural

| Title | Notes |
|-------|-------|
| New Computing Paradigm | Quantum, neuromorphic, photonic — hardware that FLOP-based monitoring cannot measure. 20-year horizon card |
| Recursive Self-Improvement | Unpreventable. No treaty provision addresses a property of the universe. Cannot be resolved — sits in unresolved area permanently |
| Inference Scaling | Existing models become dangerous through inference-time compute, bypassing the treaty's training-focused restrictions entirely |

## Context Threats (no extinction count, but change the landscape)

Things that degrade the treaty's political/operational environment without directly providing training capability.

### Geopolitical

| Title | Notes |
|-------|-------|
| Country Exits Treaty | Political fracture, cascade risk |
| Invasion of Taiwan | Chip supply chain disruption, geopolitical crisis consuming diplomatic bandwidth |
| Anti-Treaty Government | A major signatory elects/installs a government hostile to the treaty. Covers elections, coups, whatever — the mechanism doesn't matter |

### Operational

| Title | Notes |
|-------|-------|
| Treaty Inspector Detained | Obstruction of verification |
| AI-Powered Cyber Attack | AI-speed offense vs. human-speed defense. Not just conventional hacking |
| Bribery and Blackmail | Corruption of treaty officials, inspectors, or government decision-makers |
| Underground Datacenter | Context, not capability — a bunker without chips is just a building. Whether it's dangerous depends on what else has happened |
| Weaponized AI | AI used to create dangerous applications (bioweapons, cyberweapons, etc.) below the superintelligence threshold. Increases political urgency for the treaty |

### Political legitimacy

| Title | Notes |
|-------|-------|
| Whistleblower Reveals Surveillance | The treaty's surveillance apparatus gets exposed, causing public backlash. Not a whistleblower reporting cheating — that's good for the treaty |
| Pro-AI Terrorists | Accelerationists who actively sabotage treaty enforcement. Violence, disruption, funding illegal training |
| Anti-AI Terrorists | People so afraid of AI they bomb datacenters and attack researchers. Helps the treaty's goals superficially but undermines legitimacy and creates chaos |
| Treaty Rot | 20-year card. Nobody actively opposes the treaty — they just stop caring. Budget cuts, staff turnover, complacency |
| Legal Challenge to Treaty Authority | Domestic courts block enforcement. Sovereignty claims override treaty obligations |
| AI Prosperity Gap | Non-treaty nations demonstrate beneficial AI, creating domestic political pressure on signatories to weaken restrictions |

### Information

| Title | Notes |
|-------|-------|
| Open-Source Weights Published | Proliferation after the fact. Can't un-publish. Containment problem |
| Rogue Researcher | Key talent moves to non-signatory country. Knowledge transfer, not a training run |

## Treaty Cards

Provisions players can add to the active treaty. Titles should convey what the provision lets the treaty DO.

| Title | Notes |
|-------|-------|
| Compute Ban | The foundational prohibition — everything else enforces this. Threshold regularly tightened as hardware improves |
| Declared Facilities | Force all large computing clusters into registered, monitored, physically accessible sites |
| Chip Tracking | Track every AI-capable chip from fabrication to deployment by serial number |
| Export Controls | Block transfer of AI chips, fab equipment, and related technology to non-treaty nations |
| Routine Inspections | Enter and examine any declared computing facility, announced or scheduled |
| Surprise Inspections | Inspect any site without advance notice, triggered by suspicion or tip-off. Adversarially triggered, no warning |
| Research Restrictions | Ban capability-relevant AI research categories. Pre-publication review for dangerous advances |
| Researcher Monitoring | Track where frontier AI researchers work, travel, and publish |
| Whistleblower Protections | Asylum, financial incentives, and protected channels for insiders who report violations |
| Financial Tracking | Monitor money flows, procurement patterns, and large transactions linked to compute or AI development |
| Remote Monitoring | Detect compute activity remotely via satellite imagery, power grid monitoring, and network analysis. Distinct from inspections: passive, not on-site |
| Economic Sanctions | Trade restrictions, asset freezes, and financial penalties against violating nations or entities |
| Cyber Operations | Digitally disrupt unauthorized training runs, take down leaked weights, sabotage rogue infrastructure |
| Military Strikes | Armed force to disable or destroy prohibited computing facilities |
| Withdrawal Penalty | Automatic severe consequences for leaving the treaty: sanctions, technology exclusion, asset seizure |

## Deleted Cards (from v1)

Cards from the v1 definitions.jsonl that were cut or renamed in v2 and why. Old type in parentheses refers to the v1 card type (flat threat / tiered threat / treaty), not an ID.

| Old card | Why cut |
|----------|--------|
| Bioweapon Blueprint (flat threat) | Replaced by Weaponized AI (context) — broadened to cover all dangerous sub-ASI applications |
| Autonomous Agent (tiered threat) | Subsumed by Recursive Self-Improvement and the general capability accumulation mechanic |
| Fake Compliance (flat threat) | Merged into Corporate Defiance |
| Insider Sabotage (flat threat) | Merged into Bribery and Blackmail |
| Whistleblower Bombshell (flat threat) | The old card was a whistleblower revealing corporate cheating — that's good for the treaty. Replaced by Whistleblower Reveals Surveillance (which is bad for the treaty) |
| Uncontrolled Hardware (flat threat) | Split into Legal Chip Sales and Independent Chip Factory |
| State AI Program (tiered threat) | Covered by Signatory Races to Train (treaty member cheating) and context cards (non-signatory programs) |
| Weights Leak (tiered threat) | Renamed to Stolen Model Weights |
| Garage Cluster (tiered threat) | Merged into Repurposed Consumer Chips and Distributed Training |
| Open-Source Release (tiered threat) | Renamed to Open-Source Weights Published, reclassified as context |
| Cyber Attack (tiered threat) | Renamed to AI-Powered Cyber Attack, reclassified as context |
| Legal Obstruction (threat-1) | Renamed to Legal Challenge to Treaty Authority |
| Nation Exits Treaty (threat-1) | Renamed to Country Exits Treaty |
| Safety Breakthrough x5 | Safety cards removed entirely — game ends when deck subset is exhausted |
| Border Interdiction (treaty) | Folded into Export Controls |
| Covert Operations (treaty) | Folded into Cyber Operations + Military Strikes |
| Human Intelligence (treaty) | Folded into Researcher Monitoring + Whistleblower Protections |
| Information Containment (treaty) | Folded into Research Restrictions + Cyber Operations |
| Compute Licensing (treaty) | Replaced by Compute Ban (the prohibition itself, not the licensing regime) |
| Facility Decommission (treaty) | Covered by Military Strikes + Declared Facilities |
| Diplomatic Pressure (treaty) | Too vague — what does "diplomatic pressure" let you DO? Covered by Economic Sanctions + Withdrawal Penalty |
| Emergency Powers (treaty) | Too vague — what emergency action specifically? Covered by Surprise Inspections + Military Strikes |
| Treaty Tribunal (treaty) | Cut for now — may add back. "Override domestic courts" is important but narrow |
| Supply Chain Tracking (treaty) | Renamed to Chip Tracking |
| Research Controls (treaty) | Renamed to Research Restrictions |
| Whistleblower Network (treaty) | Renamed to Whistleblower Protections |
| Military Action (treaty) | Renamed to Military Strikes |

## Card counts

- **Capability threats:** 14
- **Context threats:** 16
- **Treaty cards:** 15
- **Total threats:** 30 (draw ~half per game = ~15 per session)

## Not yet decided

- Exact extinction threshold: 3 for now (playtest to calibrate)
- Exact subset size per game (playtest to determine)
