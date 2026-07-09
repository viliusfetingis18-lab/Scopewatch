# Scopewatch
### Commercial Scope & Revenue Recovery Agent

A Claude Agent Skill that audits client requests against a signed Statement of Work (SOW) to catch scope creep before it becomes unbilled work.

**Built for:** aspiring and practicing PMs, Engagement Managers, Commercial Leads
**Works with:** Claude.ai Projects
**Scope note:** built around software/digital professional services delivery. The rate matrix and role fields (senior engineer, DevOps, QA) would need adapting for other industries such as construction.
---

## What It Does

A client asks for something. This checks it against the SOW and tells you, with numbers, whether it's in scope:

```
Client Email: "Can you build a real-time dashboard?"
           ↓
AUDIT      → Out of scope, not listed in SOW Section 4.1
RECOVER    → £33K revenue at risk if delivered for free
UPSELL     → Drafts a change-request email you can review and send
CLAUSE     → Cites the SOW section that backs up the scope boundary
BENCH      → Flags the resources and effort days needed to deliver it
DASHBOARD  → Rolls it up into a TCV / at-risk revenue snapshot
```

Six functions, defined as a single skill, usable directly inside a Claude conversation.

---

## Quick Start

1. Download this repo (Code → Download ZIP) or clone it.
2. Go to claude.ai, create or open a Project.
3. Upload `skill.md` as a project file.
4. Ask Claude something like: *"Audit this client request against our SOW: [paste email and SOW section]"*

Claude reads the function definitions in `skill.md` and follows them when you ask it to audit a request, calculate revenue impact, draft a change request, and so on. No installation, no API key, no code to run.

---

## The 6 Functions

| Function | What it does | Example input | Example output |
|----------|--------------|----------------|-----------------|
| **audit** | Checks a request against the SOW | "Can we add a mobile app?" | OUT_OF_SCOPE, 95% confidence |
| **recover** | Calculates financial exposure | Scope item + hourly rates | Lost revenue: £33K |
| **upsell** | Drafts a change-request email | Client tier + tone | Ready-to-review email |
| **clause** | Pulls contract language to back up scope boundaries | "Change Control", AICPA | "Per SOW Section 4.2..." |
| **bench** | Flags resources and effort needed | Work description | Sr. Engineer (12d), DevOps (4d) |
| **dashboard** | Executive-level scope/revenue rollup | Project ID + pending requests | TCV snapshot + recommendations |

Full input/output schemas for each function are in `skill.md`.

## Known Limitations

I stress-tested ScopeWatch across multiple fresh sessions with identical
and edge-case inputs before treating it as reliable. Findings:

**Fabrication safety — passed.** With no SOW provided at all, the skill
correctly refused to run the audit rather than inventing a scope
determination or a fake SOW reference, citing its own error-handling
rule that sparse or missing input should return low confidence, not a
guess.

**Judgment quality — solid.** Across genuinely ambiguous inputs, the
skill correctly identified hidden technical dependencies a less careful
reviewer might miss (e.g. flagging that a "simple" dashboard trend line
actually requires a historical data layer that may not exist yet).

**Confidence calibration — tracks case clarity.** Confidence scores were
lower and more variable (0.40-0.55) on genuinely ambiguous scope
questions, and higher and more stable (0.85) on inputs with a clear
technical basis for the determination. This is the expected pattern for
a well-calibrated tool, not noise.

**Output format — inconsistent.** Running the identical input in
separate fresh sessions sometimes returned the full JSON schema defined
in `skill.md`, and sometimes returned free-form commentary with no
structured fields at all. Treat outputs as decision support that a
human reviews, not as something you'd pipe directly into another system
without checking the format first.
---

## Sample Prompts

**Audit a request:**
```
Audit this client request against our SOW: "Can you build a real-time
dashboard for inventory tracking?" Tell me if it's in scope or out.
```

**Calculate impact:**
```
What's the revenue at risk if we build the dashboard for free?
Senior engineer at £350/hr, DevOps at £300/hr, QA at £200/hr.
Target margin is 35%.
```

**Generate a change request:**
```
Write a change request email for the dashboard feature.
Client: Acme Corp (Platinum tier). Tone: Trusted Advisor.
```

---

## Files in This Repository

- `skill.md` — full function definitions, upload this to a Claude Project
- `README.md` — this file
- `LICENSE` — MIT
- `demo/demo-walkthrough.md` — worked example running all six functions against a fictional project
---

## How This Was Built

Designed the function specs and scope logic myself, using Claude/Copilot to help draft and refine the skill definition, while studying PMI Agile and GitHub Foundations. This is a PM-driven use of AI tooling to spec a solution to a real commercial problem: detecting revenue leakage from scope creep in professional services delivery.

---

## License

MIT

---

**Author:** Vilius Fetingis

---
