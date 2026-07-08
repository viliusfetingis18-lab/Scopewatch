# Commercial Scope & Revenue Recovery Agent

**Skill Definition for Anthropic Agent Skills Protocol**

---

## Skill Metadata

```yaml
name: commercial-scope-revenue-agent
version: 1.0.0
author: Vilius Fetingis
description: AI skill for detecting revenue leakage, quantifying commercial exposure, and strategically recovering out-of-scope work in professional services organizations
target_platforms:
  - Professional services and consulting organizations
  - Engagement and project management teams
use_cases:
  - Scope compliance auditing
  - Revenue exposure quantification
  - Strategic change request generation
  - Contract clause referencing
  - Resource gap analysis
  - Commercial health dashboarding
```

---

## Function 1: `/audit`

### Description
Scans inbound client communications and compares them against the signed SOW baseline to determine if requests are in-scope, out-of-scope, or partially in scope.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "client_message": {
      "type": "string",
      "description": "The client request, email, or communication to audit"
    },
    "sow_document": {
      "type": "string",
      "description": "Relevant SOW sections or summary baseline"
    },
    "project_context": {
      "type": "object",
      "description": "Optional project metadata",
      "properties": {
        "phase": {"type": "string"},
        "contract_type": {"type": "string"},
        "client_tier": {"type": "string"}
      }
    }
  },
  "required": ["client_message", "sow_document"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "audit_result": {
      "type": "string",
      "enum": ["IN_SCOPE", "OUT_OF_SCOPE", "PARTIAL_SCOPE"],
      "description": "Scope determination result"
    },
    "scope_category": {
      "type": "string",
      "enum": ["Deliverables", "Support", "Enhancement", "New Request"],
      "description": "Category of the request"
    },
    "confidence_level": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Confidence score (0-1) for the audit determination"
    },
    "sow_reference": {
      "type": "string",
      "description": "Specific SOW section reference (e.g., 'Section 4.1 - Deliverables List')"
    },
    "risk_flag": {
      "type": "boolean",
      "description": "Whether this request poses commercial risk"
    },
    "recommendation": {
      "type": "string",
      "description": "Recommended action (e.g., 'Requires formal change control')"
    },
    "explanation": {
      "type": "string",
      "description": "Detailed explanation of the audit result"
    }
  },
  "required": ["audit_result", "confidence_level", "risk_flag", "recommendation"]
}
```

### Example Usage
```json
{
  "client_message": "Can you add a real-time dashboard for inventory tracking? This was mentioned in our kick-off but I don't see it in the SOW.",
  "sow_document": "Section 4.1 - Deliverables: Core reporting suite, API integrations, user access management. Real-time features listed as Phase 2 enhancement (not included).",
  "project_context": {
    "phase": "Q2 2026 delivery",
    "contract_type": "Enterprise",
    "client_tier": "Platinum"
  }
}
```

### Example Output
```json
{
  "audit_result": "OUT_OF_SCOPE",
  "scope_category": "Enhancement",
  "confidence_level": 0.95,
  "sow_reference": "Section 4.1 - Deliverables List",
  "risk_flag": true,
  "recommendation": "Requires formal change control",
  "explanation": "Real-time inventory dashboard feature not listed in signed SOW Section 4.1. Aligns with Enhancement category in Section 7.2 (Phase 2 features)."
}
```

---

## Function 2: `/recover`

### Description
Calculates lost revenue exposure if out-of-scope work is performed without formal amendment. Quantifies cost of delivery, margin impact, and commercial risk.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string",
      "default": "GBP",
      "description": "The currency code or symbol for financial output (e.g., GBP, £, EUR, USD)"
    },
    "scope_item": {
      "type": "string",
      "description": "Description of the requested work"
    },
    "hourly_rate_matrix": {
      "type": "object",
      "description": "Billable rates by resource role",
      "properties": {
        "senior_architect": {"type": "number"},
        "senior_engineer": {"type": "number"},
        "devops_engineer": {"type": "number"},
        "qa_engineer": {"type": "number"}
      }
    },
    "project_margin_target": {
      "type": "number",
      "minimum": 0,
      "maximum": 100,
      "description": "Target margin percentage (e.g., 35)"
    },
    "resource_availability": {
      "type": "boolean",
      "description": "Whether existing team can execute without external resource hiring"
    }
  },
  "required": ["scope_item", "hourly_rate_matrix", "project_margin_target"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "revenue_exposure": {
      "type": "object",
      "properties": {
        "estimated_effort_hours": {"type": "number"},
        "estimated_effort_days": {"type": "number"},
        "billable_rate_avg": {"type": "number"},
        "lost_revenue_if_free": {"type": "number"},
        "margin_impact": {"type": "string"},
        "schedule_impact_days": {"type": "number"}
      }
    },
    "cost_of_delivery": {
      "type": "object",
      "properties": {
        "resource_salary_allocation": {"type": "number"},
        "infrastructure_costs": {"type": "number"},
        "tools_licenses": {"type": "number"},
        "total_cost": {"type": "number"}
      }
    },
    "net_impact_if_free": {"type": "number"},
    "recommendation": {"type": "string"}
  },
  "required": ["revenue_exposure", "cost_of_delivery", "net_impact_if_free"]
}
```

### Example Usage
```json
{
  "scope_item": "Real-time inventory dashboard with alerts, API integration, database optimization",
  "hourly_rate_matrix": {
    "senior_engineer": 350,
    "devops_engineer": 300,
    "qa_engineer": 200
  },
  "project_margin_target": 35,
  "resource_availability": true
}
```

### Example Output
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
  "cost_of_delivery": {
    "resource_salary_allocation": 12750,
    "infrastructure_costs": 2100,
    "tools_licenses": 450,
    "total_cost": 15300
  },
  "net_impact_if_free": -25650,
  "recommendation": "ESCALATE - Commercial threshold exceeded. Formal change control required."
}
```

---

## Function 3: `/upsell`

### Description
Generates a strategically framed, tone-perfect change request response that positions out-of-scope work as a premium add-on while maintaining client trust and relationship quality.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "client_context": {
      "type": "string",
      "description": "Client name, relationship tier, communication style"
    },
    "scope_item": {
      "type": "string",
      "description": "The out-of-scope request"
    },
    "commercial_data": {
      "type": "object",
      "description": "Revenue and cost data from /recover function"
    },
    "tone_profile": {
      "type": "string",
      "enum": ["Trusted Advisor", "Enterprise Partner", "Solution Vendor"],
      "description": "Communication tone to apply"
    }
  },
  "required": ["client_context", "scope_item", "tone_profile"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "email_subject": {"type": "string"},
    "email_body": {"type": "string"},
    "key_positioning": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Key commercial positioning points"
    },
    "tone_guardrails_applied": {
      "type": "array",
      "items": {"type": "string"}
    }
  },
  "required": ["email_subject", "email_body"]
}
```

### Example Usage
```json
{
  "client_context": "Acme Corp - Platinum Tier, CFO is cost-conscious, VP Ops is innovation-focused",
  "scope_item": "Real-time inventory dashboard with alerts, API integration",
  "commercial_data": {
    "estimated_effort_days": 15,
    "lost_revenue_if_free": 33000,
    "gross_margin": 47.7
  },
  "tone_profile": "Trusted Advisor"
}
```

### Example Output
```json
{
  "email_subject": "RE: Real-Time Inventory Dashboard – Enhancement Proposal",
  "email_body": "Hi [Client Name],\n\nThank you for raising this during our review call. We love your thinking on real-time inventory visibility—it's a powerful addition to the core delivery.\n\nOur Statement of Work (SOW, Section 4.1) covers the foundational reporting suite through Q3. The real-time dashboard sits in the enhancement tier, and we want to ensure we can deliver it with the quality and support you deserve.\n\nHere's how we recommend moving forward:\n\nWe can scope this as a Formal Change Request (typically 2–3 weeks to amendment approval):\n- Scope: Real-time inventory dashboard with alerts, API integration\n- Estimated Effort: 15 engineering days + 4 DevOps days\n- Investment: £33,000 (inclusive of 12-month support tier)\n- Timeline: Delivery by [Date], post-amendment execution\n\nWhy the formal route?\n- Ensures your project has the dedicated senior talent (not context-switching from core delivery)\n- Protects both teams' capacity planning\n- Establishes clear SLAs and support boundaries\n- Enables us to resource this optimally\n\nNext Steps:\nI'll connect you with [Commercial Lead Name] to finalize the Change Request by [Date]. Once approved, you'll have full visibility into resource allocation and delivery milestones.\n\nIn the meantime, we can discuss interim reporting options that fit within scope—no obligation.\n\nLooking forward to expanding this partnership.\n\nBest regards,\n[Your Name]",
  "key_positioning": [
    "Enhancement positions as premium add-on",
    "Formal process frames as mutual protection",
    "Interim workaround maintains goodwill",
    "Resource quality emphasis builds confidence"
  ],
  "tone_guardrails_applied": [
    "Positions as enhancement not rejection",
    "Acknowledges client value",
    "References SOW authority",
    "Uses trusted advisor language"
  ]
}
```

---

## Function 4: `/clause`

### Description
References industry-standard SOW/MSA contract clauses that provide legal and commercial backing for scope boundaries and change control procedures.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "clause_type": {
      "type": "string",
      "enum": ["Change Control", "Scope Boundary", "Resource Limitation", "Support Tier", "SLA"],
      "description": "Type of contract clause needed"
    },
    "contract_template": {
      "type": "string",
      "enum": ["AICPA", "APPM", "IPA", "Custom Enterprise"],
      "description": "Contract template standard"
    }
  },
  "required": ["clause_type", "contract_template"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "relevant_section": {"type": "string"},
    "standard_language": {"type": "string"},
    "alternative_language": {"type": "string"},
    "how_to_reference": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Ways to cite this in client communications"
    }
  },
  "required": ["relevant_section", "standard_language"]
}
```

### Example Usage
```json
{
  "clause_type": "Change Control",
  "contract_template": "AICPA"
}
```

### Example Output
```json
{
  "relevant_section": "Section 4.2 – Change Control Procedure",
  "standard_language": "Any request to expand, modify, or add deliverables beyond the scope defined in Section 4.1 (Deliverables) shall constitute a 'Change Request' and requires: (a) Written Submission to Project Sponsor and Delivery Lead (within 5 business days of identification); (b) Scope Impact Assessment including revised timeline, resource allocation, and cost; (c) Formal Amendment executed by both parties with revised pricing and delivery milestones; (d) No Work Commencement prior to amendment execution (risk allocation clause). Rationale: Protects both parties' profitability, timeline certainty, and resource planning.",
  "alternative_language": "Scope Baseline: All work is bounded by the Deliverables list in the Statement of Work dated [SOW Date]. Requests for additional scope or resources require a Change Request submitted in writing to [Sponsor Role]. The Service Provider shall notify the Client within two (2) business days if a request falls outside the signed baseline, and shall not commence work until formal amendment is approved.",
  "how_to_reference": [
    "Direct SOW Reference: Per our SOW Section 4.2, changes require a formal amendment.",
    "Risk Framing: Our change control process protects both teams—ensuring your project has dedicated resources and we maintain delivery certainty.",
    "Authority Delegation: I'm connecting you with our Commercial Lead, who manages all change amendments per SOW Section 4.2."
  ]
}
```

---

## Function 5: `/bench`

### Description
Identifies specific resource profiles needed to fulfill out-of-scope requests and outlines resource allocation in delivery-standard format (RACI, effort tracking, availability assessment).

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "scope_item": {
      "type": "string",
      "description": "Description of work required"
    },
    "project_delivery_team": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "role": {"type": "string"},
          "current_allocation": {"type": "number"}
        }
      }
    },
    "available_bench": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "role": {"type": "string"},
          "skills": {"type": "array"},
          "availability": {"type": "number"}
        }
      }
    }
  },
  "required": ["scope_item"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "resource_gap_analysis": {
      "type": "object",
      "properties": {
        "scope_requirement": {"type": "string"},
        "estimated_duration_days": {"type": "number"},
        "resource_profiles_required": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "role": {"type": "string"},
              "seniority": {"type": "string"},
              "skills": {"type": "array"},
              "effort_days": {"type": "number"},
              "hourly_rate": {"type": "number"},
              "availability": {"type": "string"},
              "allocation_flag": {"type": "string"}
            }
          }
        }
      }
    },
    "resource_allocation_request_format": {"type": "object"},
    "commercial_implications": {
      "type": "object",
      "properties": {
        "internal_bench_cost": {"type": "number"},
        "external_resource_cost": {"type": "number"},
        "total_delivery_cost": {"type": "number"},
        "billable_amount": {"type": "number"},
        "gross_margin": {"type": "number"},
        "recommendation": {"type": "string"}
      }
    }
  },
  "required": ["resource_gap_analysis", "commercial_implications"]
}
```

### Example Usage
```json
{
  "scope_item": "Real-time inventory dashboard with alerts, API integration, database optimization",
  "project_delivery_team": [
    {"name": "J. Carter", "role": "Senior Engineer", "current_allocation": 90},
    {"name": "R. Nadal", "role": "QA Engineer", "current_allocation": 60}
  ],
  "available_bench": [
    {"name": "S. Okafor", "role": "DevOps Engineer", "skills": ["AWS", "CI/CD", "monitoring"], "availability": 100}
  ]
}
```

### Example Output
```json
{
  "resource_gap_analysis": {
    "scope_requirement": "Real-time inventory dashboard with alerts, API integration, database optimization",
    "estimated_duration_days": 15,
    "resource_profiles_required": [
      {
        "role": "Senior Engineer",
        "seniority": "Senior",
        "skills": ["API integration", "real-time data pipelines"],
        "effort_days": 12,
        "hourly_rate": 350,
        "availability": "Constrained, current allocation at 90%",
        "allocation_flag": "External hire or overtime required"
      },
      {
        "role": "DevOps Engineer",
        "seniority": "Mid-Senior",
        "skills": ["AWS", "CI/CD", "monitoring"],
        "effort_days": 4,
        "hourly_rate": 300,
        "availability": "Available from bench",
        "allocation_flag": "Can be allocated internally"
      }
    ]
  },
  "resource_allocation_request_format": {
    "responsible": "Senior Engineer, DevOps Engineer",
    "accountable": "Engagement Manager",
    "consulted": "Client Technical Lead",
    "informed": "Project Sponsor"
  },
  "commercial_implications": {
    "internal_bench_cost": 4800,
    "external_resource_cost": 16800,
    "total_delivery_cost": 21600,
    "billable_amount": 33000,
    "gross_margin": 34.5,
    "recommendation": "Proceed if formal change request approved. Margin meets target threshold."
  }
}
```

---

## Function 6: `/dashboard`

### Description
Generates executive-ready commercial health matrix showing Total Contract Value (TCV) vs. at-risk revenue from unbilled scope creep, pending requests, and recovery recommendations.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string",
      "default": "GBP",
      "description": "The currency code or symbol for the executive dashboard layout (e.g., GBP, £, EUR, USD)"
    },
    "project_id": {
      "type": "string",
      "description": "Project identifier"
    },
    "sow_baseline": {
      "type": "object",
      "properties": {
        "original_value": {"type": "number"},
        "start_date": {"type": "string"},
        "end_date": {"type": "string"}
      }
    },
    "tracked_changes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "description": {"type": "string"},
          "value": {"type": "number"},
          "status": {"type": "string"}
        }
      }
    },
    "pending_scope_requests": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "description": {"type": "string"},
          "estimated_value": {"type": "number"},
          "risk_level": {"type": "string"},
          "days_pending": {"type": "number"}
        }
      }
    },
    "time_period": {
      "type": "string",
      "enum": ["YTD", "QTD", "MTD", "Full Project"]
    }
  },
  "required": ["project_id", "sow_baseline", "pending_scope_requests"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "dashboard_title": {"type": "string"},
    "financial_overview": {
      "type": "object",
      "properties": {
        "sow_baseline": {"type": "number"},
        "approved_changes": {"type": "number"},
        "current_tcv": {"type": "number"},
        "at_risk_revenue": {"type": "number"},
        "adjusted_tcv": {"type": "number"}
      }
    },
    "scope_creep_assessment": {
      "type": "object",
      "properties": {
        "unresolved_requests": {"type": "number"},
        "estimated_effort_impact_days": {"type": "number"},
        "at_risk_percentage": {"type": "number"},
        "commercial_risk_rating": {"type": "string"}
      }
    },
    "revenue_recovery_recommendations": {
      "type": "array",
      "items": {"type": "string"}
    },
    "pending_requests_summary": {
      "type": "array",
      "items": {"type": "object"}
    },
    "financials_projection": {
      "type": "object",
      "properties": {
        "current_tcv": {"type": "number"},
        "projected_recovery": {"type": "number"},
        "projected_tcv": {"type": "number"},
        "improvement_percentage": {"type": "number"}
      }
    },
    "formatted_dashboard": {"type": "string", "description": "ASCII art formatted dashboard for terminal/export"}
  },
  "required": ["financial_overview", "formatted_dashboard"]
}
```

### Example Usage
```json
{
  "project_id": "ACME-2026-Q2",
  "sow_baseline": {
    "original_value": 450000,
    "start_date": "2026-04-01",
    "end_date": "2026-09-30"
  },
  "tracked_changes": [
    {"description": "Phase 1 Enhancements", "value": 45000, "status": "APPROVED"},
    {"description": "Database Optimization", "value": 42500, "status": "APPROVED"}
  ],
  "pending_scope_requests": [
    {"description": "Real-Time Dashboard", "estimated_value": 33000, "risk_level": "HIGH", "days_pending": 12},
    {"description": "API Endpoints", "estimated_value": 8500, "risk_level": "MEDIUM", "days_pending": 5},
    {"description": "Performance Tuning", "estimated_value": 4200, "risk_level": "MEDIUM", "days_pending": 3}
  ],
  "time_period": "QTD"
}
```

### Example Output
```json
{
  "dashboard_title": "ACME-2026-Q2 Commercial Health Dashboard (QTD)",
  "financial_overview": {
    "sow_baseline": 450000,
    "approved_changes": 87500,
    "current_tcv": 537500,
    "at_risk_revenue": 45700,
    "adjusted_tcv": 583200
  },
  "scope_creep_assessment": {
    "unresolved_requests": 3,
    "estimated_effort_impact_days": 22,
    "at_risk_percentage": 8.5,
    "commercial_risk_rating": "MEDIUM-HIGH"
  },
  "revenue_recovery_recommendations": [
    "Escalate Real-Time Dashboard request, pending 12 days, highest value and risk",
    "Bundle API Endpoints and Performance Tuning into a single change request to reduce admin overhead",
    "Set a 5-business-day SLA for change request decisions to reduce days-pending exposure"
  ],
  "pending_requests_summary": [
    {"description": "Real-Time Dashboard", "estimated_value": 33000, "risk_level": "HIGH", "days_pending": 12},
    {"description": "API Endpoints", "estimated_value": 8500, "risk_level": "MEDIUM", "days_pending": 5},
    {"description": "Performance Tuning", "estimated_value": 4200, "risk_level": "MEDIUM", "days_pending": 3}
  ],
  "financials_projection": {
    "current_tcv": 537500,
    "projected_recovery": 45700,
    "projected_tcv": 583200,
    "improvement_percentage": 8.5
  },
  "formatted_dashboard": "ACME-2026-Q2 | QTD\nTCV: £537.5K -> £583.2K (+8.5%)\nAt-Risk: £45.7K across 3 pending requests\nTop priority: Real-Time Dashboard (£33K, HIGH, 12 days pending)"
}
```

---

## Implementation Notes

### Data Handling
- Client communications and financial data used with this skill should be treated as confidential.
- Redact or anonymize real client names and figures where possible when testing or sharing examples.

### Error Handling
- If the SOW document is malformed or too sparse, return confidence_level below 0.5 rather than guessing.
- If the rate matrix is incomplete, ask for the missing roles rather than assuming a rate.
- If the client message is ambiguous, flag it for manual review instead of forcing a scope determination.

### Potential Future Integrations (not currently implemented)
This skill works standalone inside a Claude conversation. It does not currently connect automatically to any external system. Natural extensions would include pulling SOW data from a contract management system or pushing change requests into a project management tool, but none of that exists in this version.

---

## Version History

- **v1.0.0** (2026-07-07): Initial release with 6 core functions

---

## License

MIT License
