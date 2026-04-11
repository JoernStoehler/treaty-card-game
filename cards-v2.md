# Card Definitions — v2

Card list for the redesigned Treaty Stress Test. Cards are story elements — short titles that prompt discussion. The game should be playable from titles alone; descriptions are disambiguation for non-obvious concepts.

## Capability Threats (black border, count toward extinction)

Things that directly advance someone's ability to train superintelligence.

### Compute

| Title | Description | Notes |
|-------|-------------|-------|
| Chip Theft | — | Hardware stolen from tracked supply chain |
| Chip Smuggling | — | Illegal movement across borders |
| Chip Sales | AI chips sold legally to buyers outside the monitoring regime | The point: if it's legal, players have to accept higher compute availability or restrict legal commerce |
| Legacy Hardware Stockpile | — | Pre-treaty hardware consolidated. Also covers chips produced before treaty tightening |
| Repurposed Consumer Chips | Commodity hardware made usable for AI training via community-built tools | NOT new chips getting better — old GPUs with community-made drivers, networking via soldering, etc. |
| Distributed Training | Training split across home computers in multiple countries | No single facility to shut down. Tests whether the treaty's facility-based monitoring architecture works |
| Independent Chip Factory | AI chip fabrication outside the monitored supply chain | Someone builds a fab, bypassing the TSMC/ASML chokepoint the treaty relies on |

### Knowledge

| Title | Description | Notes |
|-------|-------------|-------|
| Algorithmic Breakthrough | — | Usually from ML research by labs, universities, hobbyists, or companies. Pure theory also valid over a 20-year horizon |
| Stolen Model Weights | — | Trained model exfiltrated and proliferating |

### Training run events

| Title | Description | Notes |
|-------|-------------|-------|
| Corporate Defiance | — | A major lab secretly completes a training run |
| Signatory Races to Train | A treaty member secretly begins training using existing monitored infrastructure | Distinct from Country Exits Treaty: they haven't left, they're cheating with infrastructure that's supposed to be monitored |

### Structural

| Title | Description | Notes |
|-------|-------------|-------|
| Novel Compute Substrate | New hardware paradigm that FLOP-based monitoring cannot measure | Quantum, neuromorphic, photonic — 20-year horizon card |
| Recursive Self-Improvement | A discovered fact about technology — an AI improves itself faster than humans can intervene | Unpreventable. No treaty provision addresses a property of the universe. Mechanically: means fewer events needed to reach extinction |

## Context Threats (no extinction count, but change the landscape)

Things that degrade the treaty's political/operational environment without directly providing training capability.

### Geopolitical

| Title | Description | Notes |
|-------|-------------|-------|
| Country Exits Treaty | — | Political fracture, cascade risk |
| Invasion of Taiwan | — | Chip supply chain disruption, geopolitical crisis consuming diplomatic bandwidth |
| Anti-Treaty Government | A major signatory elects a government hostile to the treaty | Covers elections, coups, whatever — the mechanism doesn't matter |

### Operational

| Title | Description | Notes |
|-------|-------------|-------|
| Treaty Inspector Detained | — | Obstruction of verification |
| AI-Powered Cyber Attack | AI systems attack faster than human defenders can respond | Not just conventional hacking — AI-speed offense vs. human-speed defense |
| Bribery and Blackmail | — | Corruption of treaty officials, inspectors, or government decision-makers |
| Underground Datacenter | A hidden computing facility, shielded from inspections and surveillance | Context, not capability — a bunker without chips is just a building. Whether it's dangerous depends on what else has happened |

### Political legitimacy

| Title | Description | Notes |
|-------|-------------|-------|
| Whistleblower Reveals Surveillance | The treaty's own monitoring methods become a political scandal | The treaty's surveillance apparatus gets exposed, causing public backlash. Not a whistleblower reporting cheating — that's good for the treaty |
| Pro-AI Terrorists | — | Accelerationists, people who actively sabotage treaty enforcement. Violence, disruption, funding illegal training |
| Anti-AI Terrorists | — | People so afraid of AI they bomb datacenters and attack researchers. Helps the treaty's goals superficially but undermines legitimacy and creates chaos |
| Treaty Rot | After years, enforcement weakens through budget cuts, staff turnover, and complacency | 20-year card. Nobody actively opposes the treaty — they just stop caring |
| Legal Challenge to Treaty Authority | — | Domestic courts block enforcement. Sovereignty claims override treaty obligations |

### Information

| Title | Description | Notes |
|-------|-------------|-------|
| Open-Source Weights Published | — | Proliferation after the fact. Can't un-publish. Containment problem |
| Rogue Researcher | — | Key talent moves to non-signatory country. Knowledge transfer, not a training run |

## Treaty Cards

Provisions players can add to the active treaty. Descriptions say what the provision lets the treaty DO, not what the mechanism IS.

| Title | Description | Notes |
|-------|-------------|-------|
| Compute Ban | Prohibit any training run above a compute threshold. The threshold is regularly tightened as hardware improves. | The foundational prohibition — everything else enforces this |
| Declared Facilities | All large computing clusters must be registered and housed in monitored, physically accessible sites. | Chip consolidation — force compute into places you can inspect |
| Chip Tracking | Track every AI-capable chip from fabrication to deployment by serial number. | Supply chain monitoring |
| Export Controls | Block transfer of AI chips, fab equipment, and related technology to non-treaty nations. | — |
| On-Site Inspections | Enter and examine any declared computing facility, announced or routine. | — |
| Surprise Inspections | Inspect any site without advance notice, triggered by suspicion or tip-off. | Distinct from On-Site: adversarially triggered, no warning |
| Research Restrictions | Ban capability-relevant AI research categories. Pre-publication review for dangerous advances. | — |
| Researcher Monitoring | Track where frontier AI researchers work, travel, and publish. | — |
| Whistleblower Protections | Asylum, financial incentives, and protected channels for insiders who report violations. | — |
| Financial Tracking | Monitor money flows, procurement patterns, and large transactions linked to compute or AI development. | — |
| Technical Surveillance | Detect compute activity remotely via satellite imagery, power grid monitoring, and network analysis. | Distinction from inspections: this is remote/passive, not on-site |
| Economic Sanctions | Trade restrictions, asset freezes, and financial penalties against violating nations or entities. | — |
| Cyber Operations | Digitally disrupt unauthorized training runs, take down leaked weights, sabotage rogue infrastructure. | — |
| Military Strikes | Armed force to disable or destroy prohibited computing facilities. | — |
| Withdrawal Penalty | Automatic severe consequences for leaving the treaty: sanctions, technology exclusion, asset seizure. | — |

### Treaty card open questions

- Financial Tracking vs. Technical Surveillance distinction needs to be clearer — or consolidate
- On-Site Inspections vs. Surprise Inspections distinction may need rethinking
- May be premature to optimize treaty titles and decomposition — playtest first

## Deleted Cards (from v1)

Cards from the v1 definitions.jsonl that were cut or renamed in v2 and why. Old type in parentheses refers to the v1 card type (flat threat / tiered threat / treaty), not an ID.

| Old card | Why cut |
|----------|--------|
| Bioweapon Blueprint (flat threat) | Dangerous AI application below superintelligence — valid scenario but different from what this game tests. May add back as context card. |
| Autonomous Agent (tiered threat) | Subsumed by Recursive Self-Improvement and the general capability accumulation mechanic |
| Fake Compliance (flat threat) | Merged into Corporate Defiance |
| Insider Sabotage (flat threat) | Merged into Bribery and Blackmail |
| Whistleblower Bombshell (flat threat) | The old card was a whistleblower revealing corporate cheating — that's good for the treaty. Replaced by Whistleblower Reveals Surveillance (which is bad for the treaty) |
| Uncontrolled Hardware (flat threat) | Split into Chip Sales (legal) and Independent Chip Factory |
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

- **Capability threats:** 13
- **Context threats:** 14
- **Treaty cards:** 15
- **Total threats:** 27 (draw ~half per game = ~13-14 per session)

## Not yet decided

- Exact extinction threshold (3? 4? playtest to determine)
- Exact subset size per game
- Whether to include a bioweapon/dangerous-AI-application card
- Whether Novel Compute Substrate and Independent Chip Factory should be separate or merged
- Treaty card naming and decomposition — may be premature to finalize
