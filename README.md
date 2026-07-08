# Scopewatch
### Commercial Scope & Revenue Recovery Agent

A Claude Agent Skill that audits client requests against a signed Statement of Work (SOW) to catch scope creep before it becomes unbilled work.

**Built for:** aspiring and practicing PMs, Engagement Managers, Commercial Leads
**Works with:** Claude.ai Projects

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
| **recover** | Calculates financial exposure | Scope item + hourly rates | Lost revenue: $33K |
| **upsell** | Drafts a change-request email | Client tier + tone | Ready-to-review email |
| **clause** | Pulls contract language to back up scope boundaries | "Change Control", AICPA | "Per SOW Section 4.2..." |
| **bench** | Flags resources and effort needed | Work description | Sr. Engineer (12d), DevOps (4d) |
| **dashboard** | Executive-level scope/revenue rollup | Project ID + pending requests | TCV snapshot + recommendations |

Full input/output schemas for each function are in `skill.md`.

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
Senior engineer at $350/hr, DevOps at $300/hr, QA at $200/hr.
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

---

## How This Was Built

Designed the function specs and scope logic myself, using Claude to help draft and refine the skill definition, while studying PMI Agile and GitHub Foundations. This is a PM-driven use of AI tooling to spec a solution to a real commercial problem: detecting revenue leakage from scope creep in professional services delivery.

---

## License

MIT

---

**Author:** Vilius Fetingis

---

**Author:** Vilius Fetingis
