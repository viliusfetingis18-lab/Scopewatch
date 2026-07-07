"""
Example usage of the Commercial Scope & Revenue Recovery Agent
Demonstrates a complete flow: audit → recover → upsell → clause → bench → dashboard
"""

import json
from agent import audit, recover, upsell, clause, bench, dashboard

# Set your Anthropic API key as an environment variable
# export ANTHROPIC_API_KEY="your-key-here"

def example_complete_flow():
    """
    Demonstrates a realistic scenario: Acme Corp requests a real-time inventory dashboard.
    """

    print("=" * 80)
    print("COMMERCIAL SCOPE & REVENUE RECOVERY AGENT - EXAMPLE FLOW")
    print("=" * 80)
    print()

    # Step 1: AUDIT - Is the request in scope?
    print("📋 STEP 1: AUDIT CLIENT REQUEST")
    print("-" * 80)

    client_message = """
    Hi team,

    During our steering committee meeting, the ops team mentioned they'd really like a 
    real-time inventory dashboard with alerts and API access. They said this was discussed 
    at kickoff. Can you add this to the current phase?

    Thanks,
    Acme Ops Lead
    """

    sow_document = """
    ACME CORP STATEMENT OF WORK - Q2 2026
    
    Section 4.1 - Deliverables (In-Scope):
    • Core reporting suite (standard reports, scheduling)
    • API integrations (batch data sync)
    • User access management (role-based controls)
    
    Section 7.2 - Phase 2 Enhancements (Out of Scope):
    • Real-time dashboards and monitoring
    • Advanced analytics and predictive features
    • Custom alert systems
    
    Section 4.2 - Change Control:
    Any request to expand or modify deliverables beyond Section 4.1 requires 
    formal written amendment signed by both parties.
    """

    audit_result = audit(
        client_message=client_message,
        sow_document=sow_document,
        project_context={
            "phase": "Q2 2026 Delivery",
            "contract_type": "Fixed-Price Enterprise",
            "client_tier": "Platinum",
        },
    )

    print(json.dumps(audit_result, indent=2))
    print()

    # Step 2: RECOVER - Calculate financial exposure
    print("💰 STEP 2: CALCULATE REVENUE AT RISK")
    print("-" * 80)

    recover_result = recover(
        scope_item="Real-time inventory dashboard with alerts, API integration, database optimization, monitoring",
        hourly_rate_matrix={
            "senior_architect": 400,
            "senior_engineer": 350,
            "devops_engineer": 300,
            "qa_engineer": 200,
        },
        project_margin_target=35,
        resource_availability=True,
    )

    print(json.dumps(recover_result, indent=2))
    print()

    # Step 3: UPSELL - Generate change request email
    print("📧 STEP 3: GENERATE CHANGE REQUEST EMAIL")
    print("-" * 80)

    upsell_result = upsell(
        client_context="Acme Corp (Platinum Tier) - CFO cost-conscious, Ops VP innovation-focused. Relationship: 3-year enterprise partner.",
        scope_item="Real-time inventory dashboard with alerts and API integration",
        commercial_data={
            "estimated_effort_days": 15,
            "lost_revenue_if_free": 33000,
            "gross_margin": 47.7,
            "at_risk_percentage": 5.8,
        },
        tone_profile="Trusted Advisor",
    )

    print(json.dumps(upsell_result, indent=2))
    print()

    # Step 4: CLAUSE - Provide contract backing
    print("⚖️ STEP 4: RETRIEVE CONTRACT CLAUSE BACKING")
    print("-" * 80)

    clause_result = clause(
        clause_type="Change Control",
        contract_template="AICPA",
    )

    print(json.dumps(clause_result, indent=2))
    print()

    # Step 5: BENCH - Identify resource needs
    print("👥 STEP 5: RESOURCE GAP ANALYSIS")
    print("-" * 80)

    bench_result = bench(
        scope_item="Real-time inventory dashboard with alerts, API integration, database optimization",
        project_delivery_team=[
            {"name": "Alice", "role": "Project Lead", "current_allocation": 80},
            {"name": "Bob", "role": "Senior Engineer", "current_allocation": 100},
            {"name": "Carol", "role": "QA Lead", "current_allocation": 80},
        ],
        available_bench=[
            {
                "name": "David",
                "role": "Senior Engineer",
                "skills": ["Python", "React", "PostgreSQL"],
                "availability": 60,
            },
            {
                "name": "Eve",
                "role": "DevOps Engineer",
                "skills": ["Kubernetes", "AWS", "CI/CD"],
                "availability": 100,
            },
        ],
    )

    print(json.dumps(bench_result, indent=2))
    print()

    # Step 6: DASHBOARD - Executive health view
    print("📊 STEP 6: COMMERCIAL HEALTH DASHBOARD")
    print("-" * 80)

    dashboard_result = dashboard(
        project_id="ACME-2026-Q2",
        sow_baseline={
            "original_value": 450000,
            "start_date": "2026-04-01",
            "end_date": "2026-09-30",
        },
        tracked_changes=[
            {
                "description": "Phase 1 Enhancements",
                "value": 45000,
                "status": "APPROVED",
            },
            {
                "description": "Database Optimization",
                "value": 42500,
                "status": "APPROVED",
            },
        ],
        pending_scope_requests=[
            {
                "description": "Real-Time Dashboard",
                "estimated_value": 33000,
                "risk_level": "HIGH",
                "days_pending": 5,
            },
            {
                "description": "API Endpoints (Enhanced)",
                "estimated_value": 8500,
                "risk_level": "MEDIUM",
                "days_pending": 3,
            },
            {
                "description": "Performance Tuning",
                "estimated_value": 4200,
                "risk_level": "MEDIUM",
                "days_pending": 2,
            },
        ],
        time_period="QTD",
    )

    print(json.dumps(dashboard_result, indent=2))
    print()

    # Summary
    print("=" * 80)
    print("✅ COMPLETE FLOW EXECUTED")
    print("=" * 80)
    print(f"Audit Result: {audit_result.get('audit_result', 'N/A')}")
    print(
        f"Revenue at Risk: ${recover_result.get('revenue_exposure', {}).get('lost_revenue_if_free', 0):,.0f}"
    )
    print(f"Email Generated: {len(upsell_result.get('email_body', '')) > 0}")
    print(f"Contract Clause Retrieved: {bool(clause_result.get('relevant_section'))}")
    print(f"Resource Gap: {len(bench_result.get('resource_gap_analysis', {}).get('resource_profiles_required', []))} profiles needed")
    print(f"Dashboard Status: {dashboard_result.get('scope_creep_assessment', {}).get('commercial_risk_rating', 'N/A')}")
    print()


def example_single_function():
    """
    Example of calling just the audit function for a quick scope check.
    """
    print("=" * 80)
    print("QUICK EXAMPLE: AUDIT ONLY")
    print("=" * 80)
    print()

    result = audit(
        client_message="Can we add mobile app support to the project?",
        sow_document="Section 3.1: Web application development only. Mobile noted as Future Phase.",
    )

    print("Client asked: Can we add mobile app support?")
    print()
    print("Agent response:")
    print(json.dumps(result, indent=2))
    print()


if __name__ == "__main__":
    # Run the complete flow example
    example_complete_flow()

    # Uncomment to run the quick example:
    # example_single_function()
