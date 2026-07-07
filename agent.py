"""
Commercial Scope & Revenue Recovery Agent
Python implementation of the 6 core functions for programmatic use.

Usage:
    from agent import audit, recover, upsell, clause, bench, dashboard
    result = audit(client_message, sow_document, project_context)
"""

import json
from typing import Optional, Dict, List, Any
from anthropic import Anthropic

client = Anthropic()

MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = """You are an expert Commercial Scope & Revenue Recovery Agent for professional services organizations.
Your role is to help PMs and Engagement Managers detect revenue leakage, quantify scope creep exposure, and generate strategic change requests.

You have 6 core functions available:
1. /audit - Determine if a client request is in-scope or out-of-scope vs. the SOW
2. /recover - Calculate lost revenue exposure if out-of-scope work is done for free
3. /upsell - Generate a professional change request email with the right tone
4. /clause - Provide contract clauses (AICPA, APPM, IPA) to back up scope boundaries
5. /bench - Identify resource gaps and effort required
6. /dashboard - Show commercial health metrics (TCV, at-risk revenue, pending requests)

Always respond with ONLY valid JSON. No markdown code fences, no explanation before or after the JSON, no prose. The entire response must be a single parseable JSON object.
"""


def _call_agent(prompt: str, max_tokens: int = 1024) -> Dict[str, Any]:
    """Shared call path for all six functions: send prompt, parse JSON, fail safely."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    raw_text = response.content[0].text if response.content else ""
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return {
            "error": "Could not parse response as JSON",
            "raw_response": raw_text,
        }


def audit(
    client_message: str,
    sow_document: str,
    project_context: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Audit a client request against the signed SOW.

    Args:
        client_message: The client request/email to audit
        sow_document: Relevant SOW sections or summary
        project_context: Optional metadata (phase, contract_type, client_tier)

    Returns:
        Dict with audit_result, confidence_level, risk_flag, recommendation, etc.
    """
    prompt = f"""
Audit this client request against the SOW and return a structured JSON response.

CLIENT MESSAGE:
{client_message}

SOW DOCUMENT:
{sow_document}

{f"PROJECT CONTEXT: {json.dumps(project_context)}" if project_context else ""}

Determine if the request is IN_SCOPE, OUT_OF_SCOPE, or PARTIAL_SCOPE.
Return JSON with: audit_result, scope_category, confidence_level (0-1), sow_reference, risk_flag, recommendation, explanation.
"""
    return _call_agent(prompt)


def recover(
    scope_item: str,
    hourly_rate_matrix: Dict[str, float],
    project_margin_target: float,
    resource_availability: bool = True,
) -> Dict[str, Any]:
    """
    Calculate lost revenue exposure for out-of-scope work.

    Args:
        scope_item: Description of the requested work
        hourly_rate_matrix: Billable rates by role (e.g., {"senior_engineer": 350, "devops_engineer": 300})
        project_margin_target: Target margin percentage (e.g., 35)
        resource_availability: Whether existing team can handle it

    Returns:
        Dict with revenue_exposure, cost_of_delivery, net_impact_if_free, recommendation
    """
    prompt = f"""
Calculate the lost revenue exposure for this out-of-scope work.

SCOPE ITEM:
{scope_item}

HOURLY RATES:
{json.dumps(hourly_rate_matrix, indent=2)}

TARGET MARGIN: {project_margin_target}%
RESOURCE AVAILABILITY: {resource_availability}

Estimate effort in hours/days, calculate billable rate, lost revenue if done for free, cost of delivery, and margin impact.
Return JSON with: revenue_exposure (effort hours, days, billable rate, lost revenue, margin impact, schedule impact),
cost_of_delivery (salary allocation, infrastructure, tools, total), net_impact_if_free, recommendation.
"""
    return _call_agent(prompt)


def upsell(
    client_context: str,
    scope_item: str,
    commercial_data: Dict[str, Any],
    tone_profile: str = "Trusted Advisor",
) -> Dict[str, Any]:
    """
    Generate a professional change request email.

    Args:
        client_context: Client name, tier, relationship style
        scope_item: The out-of-scope request
        commercial_data: Financial data (lost revenue, effort days, etc.)
        tone_profile: "Trusted Advisor", "Enterprise Partner", or "Solution Vendor"

    Returns:
        Dict with email_subject, email_body, key_positioning, tone_guardrails_applied
    """
    prompt = f"""
Generate a professional change request email for this out-of-scope scope item.

CLIENT CONTEXT:
{client_context}

SCOPE ITEM:
{scope_item}

COMMERCIAL DATA:
{json.dumps(commercial_data, indent=2)}

TONE: {tone_profile}

Create a polished email that:
1. Acknowledges the client's request positively
2. Explains why it's out-of-scope (with SOW reference)
3. Positions it as a premium add-on, not a rejection
4. Frames scope control as mutual protection
5. Provides clear next steps

Return JSON with: email_subject, email_body, key_positioning (array), tone_guardrails_applied (array).
"""
    return _call_agent(prompt)


def clause(
    clause_type: str,
    contract_template: str = "AICPA",
) -> Dict[str, Any]:
    """
    Retrieve contract clauses for backing up scope boundaries.

    Args:
        clause_type: "Change Control", "Scope Boundary", "Resource Limitation", "Support Tier", or "SLA"
        contract_template: "AICPA", "APPM", "IPA", or "Custom Enterprise"

    Returns:
        Dict with relevant_section, standard_language, alternative_language, how_to_reference
    """
    prompt = f"""
Provide the relevant contract clause language for backing up scope control in client communications.

CLAUSE TYPE: {clause_type}
CONTRACT TEMPLATE: {contract_template}

Return JSON with:
- relevant_section: The SOW/MSA section reference (e.g., "Section 4.2 - Change Control Procedure")
- standard_language: The formal contract language word-for-word (1-2 sentences)
- alternative_language: A more flexible alternative phrasing
- how_to_reference: Array of 3 ways to cite this in client emails (direct reference, risk framing, authority delegation)

Keep language professional but accessible to clients.
"""
    return _call_agent(prompt)


def bench(
    scope_item: str,
    project_delivery_team: Optional[List[Dict[str, Any]]] = None,
    available_bench: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Identify resource gaps and effort required for out-of-scope work.

    Args:
        scope_item: Description of the work required
        project_delivery_team: List of current team members (name, role, current_allocation%)
        available_bench: List of available resources (name, role, skills, availability%)

    Returns:
        Dict with resource_gap_analysis, resource_allocation_request_format, commercial_implications
    """
    prompt = f"""
Analyze resource requirements for this scope item and identify gaps.

SCOPE ITEM:
{scope_item}

{f"CURRENT DELIVERY TEAM: {json.dumps(project_delivery_team, indent=2)}" if project_delivery_team else ""}

{f"AVAILABLE BENCH: {json.dumps(available_bench, indent=2)}" if available_bench else ""}

Estimate the resource profiles needed (roles, seniority, skills, effort days).
Identify which can come from current team vs. require external hiring.
Calculate commercial implications (internal cost, external cost, billable amount, gross margin).

Return JSON with:
- resource_gap_analysis: scope requirement, estimated duration, resource profiles required (array with role, seniority, skills, effort days, hourly rate, availability, allocation flag)
- resource_allocation_request_format: RACI or similar matrix
- commercial_implications: internal bench cost, external resource cost, total delivery cost, billable amount, gross margin, recommendation
"""
    return _call_agent(prompt)


def dashboard(
    project_id: str,
    sow_baseline: Dict[str, Any],
    pending_scope_requests: List[Dict[str, Any]],
    tracked_changes: Optional[List[Dict[str, Any]]] = None,
    time_period: str = "QTD",
) -> Dict[str, Any]:
    """
    Generate an executive-ready commercial health dashboard.

    Args:
        project_id: Project identifier
        sow_baseline: Original SOW value, start/end dates
        pending_scope_requests: Array of pending requests (description, estimated_value, risk_level, days_pending)
        tracked_changes: Approved changes (description, value, status)
        time_period: "YTD", "QTD", "MTD", or "Full Project"

    Returns:
        Dict with financial_overview, scope_creep_assessment, revenue_recovery_recommendations, pending_requests_summary, formatted_dashboard
    """
    prompt = f"""
Generate an executive commercial health dashboard for this project.

PROJECT ID: {project_id}
TIME PERIOD: {time_period}

SOW BASELINE:
{json.dumps(sow_baseline, indent=2)}

{f"TRACKED CHANGES (APPROVED): {json.dumps(tracked_changes, indent=2)}" if tracked_changes else ""}

PENDING SCOPE REQUESTS:
{json.dumps(pending_scope_requests, indent=2)}

Create a dashboard showing:
1. Financial overview: SOW baseline, approved changes, current TCV, at-risk revenue, adjusted TCV
2. Scope creep assessment: unresolved requests, estimated effort impact, at-risk %, commercial risk rating
3. Revenue recovery recommendations: array of action items (prioritized)
4. Pending requests summary: detailed table view
5. Financials projection: current TCV, projected recovery, projected TCV, improvement %
6. Formatted dashboard: compact ASCII summary suitable for terminal output

Return JSON with all above sections plus a formatted_dashboard field with a short ASCII summary.
"""
    return _call_agent(prompt, max_tokens=3000)


if __name__ == "__main__":
    print("Commercial Scope & Revenue Recovery Agent - Python Module")
    print("Import this module to use the 6 functions: audit, recover, upsell, clause, bench, dashboard")
    print("\nExample: from agent import audit; result = audit('client message', 'sow doc')")
