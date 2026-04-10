const CARDS = {
  "treaty": [
    {
      "id": "border-interdiction",
      "name": "Border Interdiction",
      "description": "Intercept prohibited hardware, materials, and personnel in transit",
      "category": "enforcement"
    },
    {
      "id": "compute-licensing",
      "name": "Compute Licensing",
      "description": "Require permits for operating compute above a threshold; unlicensed aggregation is a treaty violation",
      "category": "prevention"
    },
    {
      "id": "covert-operations",
      "name": "Covert Operations",
      "description": "Clandestine action to disrupt violations without public attribution",
      "category": "enforcement"
    },
    {
      "id": "cyber-operations",
      "name": "Cyber Operations",
      "description": "Digital disruption of unauthorized training runs, infrastructure, and distribution networks",
      "category": "enforcement"
    },
    {
      "id": "diplomatic-pressure",
      "name": "Diplomatic Pressure",
      "description": "Coordinated political action and public condemnation against non-compliant actors",
      "category": "governance"
    },
    {
      "id": "economic-sanctions",
      "name": "Economic Sanctions",
      "description": "Targeted financial pressure, trade restrictions, and asset freezes against violators",
      "category": "enforcement"
    },
    {
      "id": "emergency-powers",
      "name": "Emergency Powers",
      "description": "Authority for rapid treaty response that bypasses normal bureaucratic and legal procedures",
      "category": "governance"
    },
    {
      "id": "export-controls",
      "name": "Export Controls",
      "description": "Restrict movement of AI hardware, expertise, and technology across borders",
      "category": "prevention"
    },
    {
      "id": "facility-decommission",
      "name": "Facility Decommission",
      "description": "Safely shut down, dismantle, and dispose of prohibited computing infrastructure",
      "category": "enforcement"
    },
    {
      "id": "financial-tracking",
      "name": "Financial Tracking",
      "description": "Follow money flows, procurement patterns, and financial transactions linked to compute acquisition",
      "category": "detection"
    },
    {
      "id": "human-intelligence",
      "name": "Human Intelligence",
      "description": "Cultivate informants and infiltrate organizations involved in prohibited activities",
      "category": "detection"
    },
    {
      "id": "information-containment",
      "name": "Information Containment",
      "description": "Authority to suppress, quarantine, or take down leaked model weights, training methods, and dangerous research",
      "category": "prevention"
    },
    {
      "id": "military-action",
      "name": "Military Action",
      "description": "Armed force against treaty violators, from targeted raids to strikes on prohibited facilities",
      "category": "enforcement"
    },
    {
      "id": "on-site-inspection",
      "name": "On-Site Inspection",
      "description": "Authority to conduct announced and surprise inspections at any declared or suspected facility",
      "category": "detection"
    },
    {
      "id": "research-controls",
      "name": "Research Controls",
      "description": "Registration and oversight of capability-relevant research; pre-publication review for dangerous advances",
      "category": "prevention"
    },
    {
      "id": "supply-chain-tracking",
      "name": "Supply Chain Tracking",
      "description": "End-to-end tracking of AI chips from fabrication through deployment, by serial number",
      "category": "detection"
    },
    {
      "id": "technical-surveillance",
      "name": "Technical Surveillance",
      "description": "Monitor facilities and networks via satellite imagery, power consumption, and signal analysis",
      "category": "detection"
    },
    {
      "id": "treaty-tribunal",
      "name": "Treaty Tribunal",
      "description": "International court with binding authority to adjudicate violations and override domestic legal obstacles",
      "category": "governance"
    },
    {
      "id": "whistleblower-network",
      "name": "Whistleblower Network",
      "description": "Protected channels and incentives for insiders to report treaty violations",
      "category": "detection"
    },
    {
      "id": "withdrawal-penalty",
      "name": "Withdrawal Penalty",
      "description": "Severe, automatic consequences for nations that leave the treaty (sanctions, technology exclusion)",
      "category": "governance"
    }
  ],
  "threat1": [
    {
      "id": "bioweapon-blueprint",
      "name": "Bioweapon Blueprint",
      "text": "A research group used an AI model to generate a novel pathogen design optimized for transmissibility. The blueprint spread through private channels. Multiple groups downloaded copies."
    },
    {
      "id": "chip-smuggling",
      "name": "Chip Smuggling",
      "text": "AI chips were diverted through shell companies to anonymous buyers. The chips surfaced in a facility in a non-signatory nation. A frontier model was trained and the resulting weights appeared on encrypted markets."
    },
    {
      "id": "fake-compliance",
      "name": "Fake Compliance",
      "text": "A company ran a hidden frontier training operation within its existing facility. The training ran alongside legitimate workloads during off-hours. The finished model was quietly transferred to a subsidiary abroad."
    },
    {
      "id": "insider-sabotage",
      "name": "Insider Sabotage",
      "text": "A senior official within the treaty organization was secretly working for a foreign government. Classified operational intelligence was passed to multiple actors over several months. At least one used the leaked information to complete a frontier training run."
    },
    {
      "id": "legacy-hardware",
      "name": "Legacy Hardware",
      "text": "A company had accumulated a large fleet of older GPUs from before the treaty. It consolidated them into a single facility and completed a frontier-scale training run."
    },
    {
      "id": "legal-obstruction",
      "name": "Legal Obstruction",
      "text": "A company established a frontier training operation under the legal protection of its host country's domestic courts. The host government backed the company's sovereignty claims. The training completed and the resulting model entered commercial deployment."
    },
    {
      "id": "nation-exits-treaty",
      "name": "Nation Exits Treaty",
      "text": "A major signatory announced withdrawal from the treaty. Its facilities ramped up compute within days and completed a frontier training run. Two allied nations signaled they would follow."
    },
    {
      "id": "rogue-researcher",
      "name": "Rogue Researcher",
      "text": "A leading AI researcher disappeared from a major lab and resurfaced in a non-signatory country. Within months, that country demonstrated AI capabilities far beyond its prior level."
    },
    {
      "id": "uncontrolled-hardware",
      "name": "Uncontrolled Hardware",
      "text": "AI-capable chips were manufactured and sold on the open market without restriction. Non-signatory nations acquired enough hardware for frontier-scale training. At least one training run completed."
    },
    {
      "id": "whistleblower-bombshell",
      "name": "Whistleblower Bombshell",
      "text": "A senior engineer at a major AI lab went public, revealing the lab had been secretly training frontier models for over a year. The models had already been deployed to internal products. The engineer was fired and requested asylum."
    }
  ],
  "threat2": [
    {
      "id": "algorithmic-breakthrough",
      "name": "Algorithmic Breakthrough",
      "label1": "0\u20131 failures",
      "text1": "A published paper demonstrated training efficiency gains that reduced compute requirements by orders of magnitude. Multiple groups replicated the results within days. Several completed training runs on hardware that would previously have been insufficient.",
      "label2": "2+ failures",
      "text2": "The efficiency gains meant existing consumer hardware was sufficient for frontier training. Large-scale compute was no longer a prerequisite. Garage-scale runs produced capable models within weeks of the paper's publication."
    },
    {
      "id": "autonomous-agent",
      "name": "Autonomous Agent",
      "label1": "0\u20131 failures",
      "text1": "An AI agent operated autonomously for weeks, sustaining itself through cryptocurrency payments for cloud compute. It acquired resources and completed a training run that produced a model with dangerous capabilities.",
      "label2": "2+ failures",
      "text2": "Multiple autonomous agents operated across the internet, accumulating resources and running training experiments. They replicated across hosting providers and collectively completed training runs that produced frontier-capable models."
    },
    {
      "id": "corporate-defiance",
      "name": "Corporate Defiance",
      "label1": "0\u20131 failures",
      "text1": "A major AI lab trained a frontier model while publicly claiming it had stopped. The model's capabilities far exceeded anything the lab had publicly shown.",
      "label2": "2+ failures",
      "text2": "Multiple labs openly conducted frontier research, citing each other's defiance as justification. Frontier models were trained and deployed commercially without restriction."
    },
    {
      "id": "cyber-attack",
      "name": "Cyber Attack",
      "label1": "0\u20131 failures",
      "text1": "Hackers breached the treaty organization's internal systems. Sensitive operational data was stolen and sold to multiple actors.",
      "label2": "2+ failures",
      "text2": "An AI system attacked the treaty organization's digital infrastructure, discovering and exploiting vulnerabilities autonomously. The organization's ability to coordinate was severely degraded across multiple regions."
    },
    {
      "id": "distributed-training",
      "name": "Distributed Training",
      "label1": "0\u20131 failures",
      "text1": "A group coordinated a training run across home computers in several countries. No single country hosted the operation. The resulting model demonstrated dangerous capabilities.",
      "label2": "2+ failures",
      "text2": "Distributed training networks spanned dozens of countries, combining consumer hardware with leaked weights. The resulting models rivaled frontier labs. The entire operation ran on consumer hardware in private residences."
    },
    {
      "id": "garage-cluster",
      "name": "Garage Cluster",
      "label1": "0\u20131 failures",
      "text1": "A frontier model was trained on consumer GPUs in a makeshift garage datacenter. The weights appeared on the dark web.",
      "label2": "2+ failures",
      "text2": "Consumer hardware was repurposed for AI training in garages and basements worldwide. Several groups produced capable models and shared their techniques openly."
    },
    {
      "id": "open-source-release",
      "name": "Open-Source Release",
      "label1": "0\u20131 failures",
      "text1": "An open-source community published trained model weights along with training code and documentation. Thousands downloaded copies within hours of publication.",
      "label2": "2+ failures",
      "text2": "A global decentralized movement shared training code, weights, and compute across thousands of nodes in dozens of countries. Capable models reached millions of users worldwide."
    },
    {
      "id": "state-ai-program",
      "name": "State AI Program",
      "label1": "0\u20131 failures",
      "text1": "A nation's military acquired computing hardware through normal defense procurement and built a dedicated facility. The government classified all details of the program. Months later, the nation demonstrated an AI capability far beyond its known research level.",
      "label2": "2+ failures",
      "text2": "Multiple nations launched classified military AI programs, each citing its rivals' programs as justification. Several produced models with advanced military capabilities. Some of those nations possessed nuclear weapons."
    },
    {
      "id": "underground-datacenter",
      "name": "Underground Datacenter",
      "label1": "0\u20131 failures",
      "text1": "A frontier-scale computing facility operated inside a converted industrial site. Its servers completed a training run that produced a capable model.",
      "label2": "2+ failures",
      "text2": "Frontier-scale computing facilities operated in converted industrial sites across several countries. Each incorporated previously leaked weights and training methods, producing models that surpassed those of any known lab."
    },
    {
      "id": "weights-leak",
      "name": "Weights Leak",
      "label1": "0\u20131 failures",
      "text1": "Model weights from a major lab were stolen and appeared on encrypted channels. Copies spread to multiple countries within hours.",
      "label2": "2+ failures",
      "text2": "Near-frontier weights had been leaked and combined with previously available training methods. Multiple groups fine-tuned the models and published improved versions. Improved versions proliferated across file-sharing networks and encrypted channels."
    }
  ],
  "safety": [
    {
      "id": "safety-1",
      "name": "Safety Breakthrough",
      "description": "Collect all 3 to win."
    },
    {
      "id": "safety-2",
      "name": "Safety Breakthrough",
      "description": "Collect all 3 to win."
    },
    {
      "id": "safety-3",
      "name": "Safety Breakthrough",
      "description": "Collect all 3 to win."
    },
    {
      "id": "safety-4",
      "name": "Safety Breakthrough",
      "description": "Collect all 3 to win."
    },
    {
      "id": "safety-5",
      "name": "Safety Breakthrough",
      "description": "Collect all 3 to win."
    }
  ]
};
