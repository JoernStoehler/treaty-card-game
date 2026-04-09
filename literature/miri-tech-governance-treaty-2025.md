---
title: "An International Agreement to Prevent the Premature Creation of Artificial Superintelligence"
author: "Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta"
year: 2025
source_url: "https://arxiv.org/abs/2511.10783"
source_format: arxiv-tex
downloaded: 2026-03-12
encrypted: false
notes: "MIRI Technical Governance team proposal for a US-China-led international treaty banning ASI development; proposes FLOP thresholds enforced via chip tracking, challenge inspections, and research restrictions; draws on NPT/IAEA/CWC precedents. Distinct from iabied-treaty.md (the Yudkowsky/Soares annotated draft treaty from ifanyonebuildsit.com)."
---

# An International Agreement to Prevent the Premature Creation of Artificial Superintelligence

**arXiv:** 2511.10783 (cs.CY) — submitted November 13, 2025, revised November 17, 2025

**Authors:** Aaron Scher, David Abecassis, Peter Barnett, Brian Abeyta (MIRI Technical Governance team)

---

## Abstract

The paper proposes a framework for international cooperation to halt ASI development until alignment is demonstrably solved. The authors argue that premature ASI poses catastrophic risks — including extinction from misaligned ASI, geopolitical instability, and misuse by malicious actors. They propose a US-China-led coalition that restricts AI training scale via FLOP thresholds, enforced through chip tracking and multifaceted verification. They acknowledge technical feasibility if enacted immediately, and lack of current political momentum.

---

## Core Risk Assessment

The paper identifies ASI as uniquely catastrophic because:

- **Alignment opacity:** Current deep learning produces behavior that "emerges from automated training processes" rather than being hand-coded, making alignment verification impossible at scale.
- **Timeline uncertainty:** Some experts predict AI systems capable of automating AI research could emerge 2028–2033.
- **Expert estimates cited:** Yoshua Bengio ~20% catastrophic probability; Anthropic's CEO 10–25% civilization-scale failure risk.

The authors distinguish ASI from AGI by emphasizing that superintelligent systems could "plan and successfully execute the destruction of humanity" either intentionally or through misaligned optimization.

---

## Strategic Framework

**Why bilateral is insufficient:** A US-only pause buys ~6 months before China catches up. A US-China bilateral agreement delays other actors ~2 years. Only comprehensive coalition participation prevents capability races.

**Coalition structure:**
- US and China lead through an Executive Council (each holds veto power).
- Other nations incentivized via security benefits and AI infrastructure access.
- Economic sanctions available for non-compliance.
- Supply chain controls: Coalition members restrict AI chip and chip-manufacturing equipment exports to non-parties.

---

## Proposed Agreement: Article-by-Article Structure

### Training Restrictions (Article IV)

Two computational thresholds operationalize capability limits:

| Threshold | FLOP | Status |
|-----------|------|--------|
| Strict (prohibition) | 10^24 FP16 | Completely prohibited |
| Monitored | 10^22 FP16 | Requires pre-approval and monitoring |
| Below monitored | — | Unrestricted |

Post-training (fine-tuning) faces a separate threshold (10^23) below the pre-training prohibition (10^24) because fine-tuning existing models poses lower capability-gain risk.

Contemporary context: DeepSeek-R1 trains at ~4×10^24 FLOP, just above the prohibition line. Thresholds are intended to account for expected algorithmic improvements (~3× per year historically), so future models would be more capable at identical compute.

### Hardware Tracking and Consolidation (Articles V–VII)

**Covered Chip Clusters (CCCs):** Any networked AI hardware exceeding 16 H100-equivalent capacity requires monitoring. The H100 provides a standardized measurement unit across architectures.

**Locating existing stock** — rather than only monitoring future production, the agreement mandates consolidation of existing inventory via:

- Mandatory reporting of CCCs
- Supply chain tracking documentation
- Physical inspections
- Satellite/aerial surveillance
- Power consumption monitoring
- Firmware-based tracking mechanisms
- Sting operations and whistleblower programs

**Staged implementation timeline:**

| Day/Year | Cluster size requiring compliance |
|----------|----------------------------------|
| Day 1 | >10,000 H100-equivalents |
| Day 10 | >1,000 H100-equivalents |
| Day 100 | >100 H100-equivalents |
| Year 2 | All covered clusters |

**Chip-use verification (transitional):** Moving from ongoing physical inspector access toward tamper-resistant on-chip mechanisms that distinguish training from inference, log computational activities, and resist circumvention through firmware updates.

### Research Restrictions (Articles VIII–IX)

Rather than banning AI research broadly, restrictions target methods that "advance toward ASI or endanger the agreement's verifiability." Prohibited research includes:

- Novel architectures or optimization algorithms with outsized capability gains
- Paradigm shifts away from deep learning (if more efficient)
- Hardware designs bypassing monitoring
- Methods enabling inference-based scaling to replace training-based progress

**Verification through human intelligence:** Given only thousands to tens-of-thousands of frontier AI researchers exist globally, verification relies on researcher interviews, whistleblower protections, analysis of publications and conference presentations, monitoring of restricted equipment purchases, and cross-referencing with chip-use data.

Historical precedent: Nuclear weapons agreements successfully restricted research on specific dangerous techniques without preventing all physics research.

### Governance and Verification (Articles X–XIII)

**Executive Council:** All major decisions require consensus; either US or China can veto. Time-sensitive technical modifications (FLOP thresholds, CCC size limits) can be implemented by the Coalition Technical Body Director-General for 30 days before requiring Executive Council approval.

**Challenge inspections:** Drawing from CWC precedent, any Party can request unannounced inspections of suspected violation sites. The CTB (Coalition Technical Body) coordinates with 48–72 hour notice.

**Independent parallel verification:** The agreement explicitly accommodates parallel US and Chinese intelligence efforts rather than requiring exclusive reliance on international mechanisms — reflecting mutual distrust while enabling redundant verification pathways.

---

## Enforcement Mechanisms

Escalating response ladder for violations:

1. Diplomacy and negotiation
2. Economic sanctions
3. Export controls on chip manufacturing equipment
4. Counterproliferation operations (measures short of military action)
5. "Other means at their disposal" (deliberately vague)

---

## Comparison to Existing Treaty Frameworks

| Framework | Element borrowed |
|-----------|-----------------|
| NPT | Board of Governors structure, preamble language, weapons-state vs. non-weapons-state distinction |
| IAEA safeguards | Routine inspections, challenge inspections, access protocols |
| CWC | Research restriction definitions, verification through human intelligence, challenge inspection procedures |
| START treaties | Bilateral verification arrangements, counting rules, implementation timelines |
| Protocol on Blinding Laser Weapons | Precedent for preventing development of dangerous technologies before proliferation |

The authors stress that precedent demonstrates **feasibility**, not effectiveness — existing agreements show similar mechanisms can be implemented, but effectiveness in the ASI context remains unproven.

---

## Duration and Exit Conditions

The agreement persists "until catastrophic risks are mitigated." Conditions for lifting restrictions include:

- Demonstrated AI alignment solution with a years-long successful track record
- Consensus on ASI-alignment method efficacy
- Established misuse and proliferation controls
- Globally-monitored AI development project with appropriate caution protocols
- Resolution of secondary risks (power concentration, unemployment, geopolitical destabilization)

Authors acknowledge this could extend **decades** given alignment research's nascent state.

---

## Implementation Roadmap (Appendix C)

Six staged phases:

1. **Laying Foundation** — initial transparency and confidence-building measures
2. **Enhanced Transparency** — communication infrastructure development
3. **Establishing Commitments** — formal limits and verification foundations
4. **Institutionalization** — full deployment of monitoring
5. **Solving ASI** — concentrated alignment research efforts
6. **Safe Implementation** — conditions for controlled superintelligence development

This mirrors how nuclear nonproliferation evolved incrementally rather than appearing fully formed.

Appendix B identifies immediate steps available today: intelligence agencies establishing communication channels, voluntary chip-manufacturer tracking pilots, academic consensus-building on alignment difficulty, tamper-resistant firmware prototype development, and researcher interview protocols.

---

## Major Objections Addressed

**"Why not less restrictive measures?"** Algorithmic progress compounds the problem. At 3× efficiency gains per year, unmonitored consumer hardware becomes dangerous within years. Major breakthroughs (transformers provided 7.2× gains) could suddenly destabilize the entire regime.

**"Why not wait and pause later?"** Once dangerous AI systems exist, inference control becomes necessary alongside training restrictions — requiring more invasive measures. Further delay risks hardware proliferation making comprehensive tracking impossible, secret state facilities emerging, and supply chain bottlenecks dissolving.

**"Why not defensive systems?"** The paper argues that offense-dominant technologies (potential bioweapons applications, novel cyberattack methods) likely exist among future AI capabilities; defense is initially outpaced.

**"Doesn't this enable authoritarianism?"** Authors acknowledge centralized AI infrastructure creates concentration risks, but argue the status quo is worse: under current trajectories, "perhaps 1–10 individuals" controlling aligned superintelligence poses unprecedented power concentration. The agreement's distributed verification (US/China independent efforts, whistleblower programs, limited-scope authorities) offers more safeguards than private corporate control.

---

## Acknowledged Weaknesses

1. **Political will:** Cannot exist without sustained US-China cooperation during existential threat recognition — currently absent.
2. **Paradigm dependence:** Restrictions assume deep learning dominance; novel paradigms could circumvent the entire regime.
3. **Inference-scaling:** Emerging techniques enabling capability gains through inference rather than training could undermine FLOP-based restrictions.
4. **Breakout risk:** If a Party violates and attempts secret ASI development, existing chip infrastructure enables rapid deployment (months, not the decade new chip production would require).
5. **Verification holes:** Small-scale distributed training, novel algorithms in restricted labs might evade detection despite multifaceted monitoring.

---

## Relevance to Game Design

- The ISIA in the game directly maps to the CTB (Coalition Technical Body) proposed here — an international body enforcing compute thresholds and conducting inspections.
- The FLOP threshold structure (strict prohibition at 10^24, monitored at 10^22) provides concrete game-mechanical grounding for why specific AI training events are treaty violations.
- The US-China bilateral leadership → coalition-building tension maps to the geopolitical pressure cards (nation defection, holdout states, inspection access refusals).
- The verification mechanisms (chip tracking, challenge inspections, satellite surveillance, researcher interviews, whistleblowers) each represent distinct card categories.
- The staged implementation timeline (Day 1 → Day 10 → Day 100 → Year 2) suggests a natural game arc where enforcement difficulty increases over time.
- The "breakout risk" framing (existing chips enable rapid ASI deployment once a party decides to defect) is a strong death scenario.
