# Scopewatch
### Commercial Scope & Revenue Recovery Agent

An AI agent that audits client requests against a signed Statement of Work (SOW) to catch scope creep before it becomes unbilled work. Built as a Claude Agent Skill, with a Python implementation for direct API use.

**Built for:** aspiring and practicing PMs, Engagement Managers, Commercial Leads
**Works with:** Claude.ai (via skill.md), Claude API (via agent.py)

---

## What It Does

A client asks for something. This checks it against the SOW and tells you, with numbers, whether it's in scope:

```
Client Email: "Can you build a real-time dashboard?"
           ↓
AUDIT      → Out of scope, not listed in SOW Section 4.1
RECOVER    → $33K revenue at risk if delivered for free
UPSELL     → Drafts a change-request email you can review and send
CLAUSE     → Cites the SOW section that backs up the scope boundary
BENCH      → Flags the resources and effort days needed to deliver it
DASHBOARD  → Rolls it up into a TCV / at-risk revenue snapshot
```

Six functions, each independent, each callable on its own or in sequence.

---

## Quick Start: Use It Inside Claude.ai

1. Download this repo (Code → Download ZIP) or clone it.
2. Go to claude.ai, create or open a Project.
3. Upload `skill.md` as a project file.
4. Ask Claude something like: *"Audit this client request against our SOW: [paste email and SOW section]"*

Claude reads the function definitions in `skill.md` and follows them when you ask it to audit, calculate impact, draft a change request, and so on.

---

## Quick Start: Use It as a Python Library

### Prerequisites
```bash
Python 3.10+
An Anthropic API key
```

### Setup
```bash
git clone https://github.com/YOUR_USERNAME/scopewatch.git
cd scopewatch
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
```

### Run the demo
```bash
python example_usage.py
```
This walks through a full scenario end to end: a client requests a real-time dashboard, the agent audits it against a sample SOW, calculates revenue at risk, and drafts a change-request email.

### Use it directly
```python
from agent import audit, recover

result = audit(
    client_message="Can you add inventory tracking dashboard?",
    sow_document="Section 4.1: Core reporting only. Real-time = Phase 2.",
    project_context={"phase": "Q2 2026", "client_tier": "Platinum"}
)

impact = recover(
    scope_item="Real-time dashboard + API + DB optimization",
    hourly_rate_matrix={"senior_engineer": 350, "devops": 300, "qa": 200},
    project_margin_target=35
)
```

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

## Sample Prompts (for use inside Claude.ai)

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
- `agent.py` — Python implementation of the 6 functions for direct API use
- `example_usage.py` — a working end-to-end demo you can run
- `requirements.txt` — Python dependencies
- `README.md` — this file

---

## How This Was Built

Prototyped using Claude and GitHub Copilot while studying PMI Agile and GitHub Foundations. I scoped the problem, directed the build, tested the output, and fixed what didn't work. I'm not a software engineer, this is a PM-driven use of AI tooling to solve a real commercial problem: detecting revenue leakage from scope creep in professional services delivery.

---

## What's Not Built Yet

This does not currently connect to Jira, Salesforce, or any other platform automatically. Output from `upsell`, `bench`, and `dashboard` is meant to be reviewed by a human before it's sent or acted on. Platform integrations may come later; they're not part of this version.

---

## License

MIT

---

**Author:** Vilius Fetingis
