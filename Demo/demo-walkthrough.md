# ScopeWatch Demo Walkthrough

> **Illustrative project data — not a real client engagement.** All names, figures, and communications below are fictional and constructed to demonstrate how the six functions work together on a single project.

Built for software/digital professional services engagements. The rate matrix and role fields (`senior_architect`, `senior_engineer`, `devops_engineer`, `qa_engineer`) reflect that context — adapting ScopeWatch to other industries (e.g. construction) would mean adjusting those role fields to match.

---

## The scenario

**Client:** Horizon Retail Group (fictional)
**Engagement:** Phase 1 delivery of a store inventory management platform — POS integration, static inventory reporting, user access management.
**Signed SOW, Section 4.1 (Deliverables):** POS integration, static inventory reporting dashboard, user access management.
**SOW, Section 7.2 (Phase 2 Enhancements — explicitly excluded from Phase 1):** real-time inventory sync, predictive stock alerts, live multi-store dashboard.

**Client message:**
> "Hey team, love the progress on the platform. Can we just add real-time stock sync across all 40 stores? The dev team's already in the codebase, so it should only take an afternoon."

A small-sounding request framed around team availability rather than contracted scope — the pattern ScopeWatch is built to catch.

---

## 1. `/audit`

**Input:** client message above + SOW Section 4.1 / 7.2 baseline.

**Output:**
```json
{
  "audit_result": "OUT_OF_SCOPE",
  "scope_category": "Enhancement",
  "confidence_level": 0.92,
  "sow_reference": "Section 4.1 (Deliverables) / Section 7.2 (Phase 2 Enhancements)",
  "risk_flag": true,
  "recommendation": "Requires formal change control before work begins",
  "explanation": "Real-time stock sync across all stores is explicitly scoped as a Phase 2 enhancement in Section 7.2, not part of the Phase 1 deliverables list in Section 4.1."
}
```

## 2. `/clause`

**Input:** `clause_type: Change Control`, `contract_template: Custom Enterprise`.

**Output:** A short clause establishing that any request beyond Section 4.1 requires written submission to the project sponsor, a scope impact assessment, and a signed amendment before work starts, with no work commencing ahead of that amendment being executed.

## 3. `/recover`

**Input:**
```json
{
  "scope_item": "Real-time stock sync across 40 stores, API integration, live dashboard",
  "hourly_rate_matrix": {"senior_engineer": 350, "devops_engineer": 300, "qa_engineer": 200},
  "project_margin_target": 35,
  "resource_availability": true
}
```

**Output:**
```json
{
  "revenue_exposure": {
    "estimated_effort_hours": 120,
    "estimated_effort_days": 15,
    "billable_rate_avg": 275,
    "lost_revenue_if_free": 33000,
    "margin_impact": "-£11,550 (35% margin loss)",
    "schedule_impact_days": 10
  },
  "net_impact_if_free": -25650,
  "recommendation": "ESCALATE - Commercial threshold exceeded. Formal change control required."
}
```

## 4. `/bench`

**Input:** same scope item, a small fictional delivery team (one senior engineer near full allocation, one QA engineer with headroom, one DevOps engineer available on the bench).

**Output:** Flags the senior engineer as constrained (needs overtime or external hire), the DevOps role as coverable internally, and rolls up to a total delivery cost against the £33,000 billable amount, landing around 35% gross margin. Recommendation: proceed if the change request is approved.

## 5. `/upsell`

**Input:** `tone_profile: Trusted Advisor`, commercial data from step 3.

**Output:** A short client email that welcomes the idea, references Section 4.1, frames the enhancement as a paid change request with a clear cost and timeline, and offers an interim workaround to preserve goodwill.

## 6. `/dashboard`

**Input:** SOW baseline value, this pending request plus a couple of other fictional pending items.

**Output:** An executive-style summary showing current TCV, at-risk revenue from unresolved requests, a risk rating, and recovery recommendations (escalate the highest-value item, bundle smaller ones, set an SLA for change request turnaround).

---

## Why this order

Audit → Clause → Recover → Bench → Upsell → Dashboard follows how an engagement manager would actually work a request: determine scope, back it with contract language, quantify it, check resourcing, respond to the client, then roll it into the portfolio view.
