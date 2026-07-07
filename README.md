# Scopewatch
# Commercial Scope & Revenue Recovery Agent

An Anthropic AI Agent Skill for detecting revenue leakage in professional services by auditing client requests against signed SOWs and automatically recovering out-of-scope work.

**Built for:** Senior PMs, Engagement Managers, Commercial Leads | **Works with:** Claude.ai, Claude API, Custom Projects

---

## 🚀 What It Does

Automate the $M revenue recovery process from scope creep. One PM command handles:

```
Client Email: "Can you build a real-time dashboard?"
           ↓
✅ AUDIT      → Out of scope - not in SOW Section 4.1
💰 RECOVER    → $33K at-risk revenue if done for free
📝 UPSELL     → Generates polite change request email
⚖️ CLAUSE     → Cites SOW Section 4.2 for legal backing
👥 BENCH      → Identifies 3 resources needed (19 days effort)
📈 DASHBOARD  → Shows TCV $537.5K | At-Risk $33K (5.8%)
```

---

## 🎯 For PMs: Quick Start (4 Steps)

### **Step 1: Download the Skills Files**
1. Go to this repository: `https://github.com/viliusfetingis18-lab/commercial-scope-revenue-agent`
2. Click the green **"Code"** button → **"Download ZIP"**
3. Extract the folder to your computer
4. You now have the 6 core skills locally

### **Step 2: Import Skills to Claude**
Go to **claude.ai** → Create a new project → Click **"Add Skills"** → Look for this option:
```
⚙️ "Upload Custom Skill" 
   (NOT "Add from URL" — you must upload the file)
```

### **Step 3: Upload Each of the 6 Core Skills**
Upload these files one at a time to your Claude project:

1. ✅ **skill.md** (contains all 6 core skill definitions)
   - OR upload as individual skill files if separated

Once uploaded, Claude will recognize all 6 functions:
- Audit client requests
- Calculate revenue at-risk
- Generate change request emails
- Cite contract clauses
- Identify resource gaps
- Show commercial health dashboard

### **Step 4: Customize & Add Your 4 Additional Skills**
In your Claude project, click **"Customize Skills"** → Edit the skill definitions:

**Add Your 4 Custom Skills (Examples):**
- 🔧 **Custom 1: Risk Escalation** — Auto-escalate scope creep >$50K to CFO
- 🔧 **Custom 2: Client Tier Rules** — Apply different rules for Platinum vs. Standard clients
- 🔧 **Custom 3: Historical Patterns** — Flag requests matching past scope creep trends
- 🔧 **Custom 4: Weekly Digest** — Summary email of all pending scope requests

Then click **"Save"** → Your agent now has **10 skills total**.

---

## 📊 Real Example: From Request to Recovery

**Scenario:** Acme Corp (Platinum client) asks for real-time inventory dashboard

**What You Do (as PM):**
```
You: "Hey Claude, audit this client request against our SOW"

Claude runs all 6 core skills automatically:
✅ AUDIT      → Out-of-scope (95% confidence) | HIGH RISK
💰 RECOVER    → Lost revenue: $33K | Margin loss: $11.5K
📝 UPSELL     → [Ready-to-send email] "Hi Acme, love this idea..."
⚖️ CLAUSE     → SOW Section 4.2: "Changes require written amendment"
👥 BENCH      → Need: Sr. Engineer (12d) + DevOps (4d) + QA (3d)
📈 DASHBOARD  → TCV $450K → At-Risk $33K → Recommended: Approve for $42.5K
```

**You hit "Send" on the upsell email. $33K recovered in 2 minutes.**

---

## 📋 The 6 Core Skills Explained

| Skill | When to Use | Example Input | Example Output |
|-------|------------|---------------|-----------------|
| **Audit** | Daily – every new client request | "Can we add a mobile app?" | OUT_OF_SCOPE · 95% confidence |
| **Recover** | Evaluate financial impact | Scope item + rates | Lost revenue: $33K |
| **Upsell** | Draft change requests | Client tier + tone | Polished email ready to send |
| **Clause** | Need contract backing | Change Control, AICPA | "Per SOW Section 4.2..." |
| **Bench** | Resource planning | Work description | Sr. Engineer (12d), DevOps (4d) |
| **Dashboard** | Executive reporting | Project ID + pending requests | TCV snapshot + recovery recs |

---

## 🔧 How to Add Your 4 Custom Skills in Claude

Once you've uploaded the 6 core skills:

1. In Claude, open your project → **"Skills"** tab
2. Click **"Edit"** next to the agent skill
3. Scroll to the bottom and click **"+ Add Custom Skill"**
4. Define your custom skill using this template:

### **Custom Skill Template**
```
Skill Name: Risk Escalation
Description: Automatically escalates scope requests above financial threshold to CFO

When to trigger: Client requests >$50K in out-of-scope work

Input needed:
- Scope item description
- Estimated cost
- Client tier (Platinum/Gold/Silver)

Output:
- Escalation target (CFO/CMO/PMO)
- Email recipients
- Urgency level (CRITICAL/HIGH/MEDIUM)
```

Repeat 4 times for your custom skills. Claude will then have **10 skills total** available.

---

## 💼 For Engineering/API Users: Installation

### Prerequisites
```bash
Python 3.10+
Anthropic API key
```

### Clone & Setup
```bash
git clone https://github.com/viliusfetingis18-lab/commercial-scope-revenue-agent.git
cd commercial-scope-revenue-agent

pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
```

### Usage Example
```python
from agent import audit, recover, dashboard

# Audit a request
result = audit(
    client_message="Can you add inventory tracking dashboard?",
    sow_document="Section 4.1: Core reporting only. Real-time = Phase 2.",
    project_context="Enterprise logistics, Q2 2026"
)

# Get financial impact
impact = recover(
    scope_item="Real-time dashboard + API + DB optimization",
    hourly_rate_matrix={
        "senior_engineer": 350,
        "devops": 300,
        "qa": 200
    },
    project_margin_target=35
)

# Show dashboard
health = dashboard(
    project_id="ACME-2026-Q2",
    sow_baseline={"value": 450000},
    pending_scope_requests=[result],
    time_period="QTD"
)
```

---

## 🔗 Integration Points

**Works seamlessly with:**
- **Project Management:** Jira, Monday.com, Asana
- **Rate Cards:** SAP SuccessFactors, Kimble
- **SOWs & Contracts:** Salesforce, Workday, Docusign, Ironclad
- **Email/Chat:** Gmail, Outlook, Slack
- **Accounting:** NetSuite, SAP

---

## 📚 Files in This Repository

- **`skill.md`** — Complete skill definitions (upload this to Claude)
- **`requirements.txt`** — Python dependencies (for engineers)
- **`sample_sow.md`** — Template SOW for testing
- **`CUSTOMIZE.md`** — Detailed guide for adding your 4 custom skills
- **`README.md`** — This file

---

## 🚀 Getting Started Paths

### 👔 **You're a Senior PM** → Start here:
1. Download this repo (green "Code" button → Download ZIP)
2. Go to claude.ai → Create project → Upload "skill.md"
3. Chat: *"Audit this client request: [paste email]"*
4. Use the generated change request email
5. ✅ Done in 2 minutes

### 🛠️ **You're an Engineer** → Start here:
1. Clone this repo: `git clone https://github.com/viliusfetingis18-lab/commercial-scope-revenue-agent.git`
2. `pip install -r requirements.txt`
3. Set your API key: `export ANTHROPIC_API_KEY="your-key"`
4. Import functions into your app
5. See `skill.md` for function specifications

### 🎯 **You're Customizing for Your Org** → Start here:
1. Download this repo
2. Upload skill.md to Claude (Step 2 above)
3. Review `CUSTOMIZE.md` for examples of custom skills
4. In Claude, edit the project and add your 4 custom skills
5. Save → Your team can now use your customized 10-skill agent
6. Share the project link with your PM team

---

## ⚡ Sample Commands for PMs

**Audit a request:**
```
"Audit this client request against our Acme SOW: 
'Can you build a real-time dashboard for inventory tracking?' 
Tell me if it's in scope or out of scope."
```

**Calculate impact:**
```
"What's the revenue at-risk if we build the real-time dashboard for free?
Use senior engineer rate of $350/hr, DevOps at $300/hr, QA at $200/hr.
Our target margin is 35%."
```

**Generate change request:**
```
"Write a professional change request email for the dashboard feature. 
Client: Acme Corp (Platinum tier).
Tone: Trusted Advisor.
Include the revenue impact and resource requirements."
```

**Check resources:**
```
"What resources do we need to build the dashboard? 
How many days of effort? 
Which team members are available?"
```

**View health:**
```
"Show me the commercial health dashboard for ACME-2026-Q2. 
Include TCV, at-risk revenue, and all pending scope requests."
```

---

## 📊 Commercial Metrics Tracked

- **Total Contract Value (TCV)** — Current contract baseline
- **At-Risk Revenue** — Unbilled scope creep exposure
- **Approved Changes** — Signed amendments + value
- **Pending Requests** — Awaiting decision
- **Effort Impact** — Days/resources needed
- **Margin Impact** — Gross margin if done for free
- **Recovery Recommendations** — Suggested actions

---

## ⚠️ Important: Download & Upload Workflow

**You CANNOT just paste a URL into Claude.**  
You must:

1. ✅ **Download** the repository as a ZIP file
2. ✅ **Extract** to your computer
3. ✅ **Upload** skill.md manually to your Claude project
4. ✅ **Customize** by adding your 4 additional skills in Claude
5. ✅ **Save** your project
6. ✅ **Share** with your PM team via project link

This gives you full control and ensures your customizations are saved.

---

## 📄 License

MIT – Use freely in your organization, contribute improvements back.

---

## 🤝 Contributing

Have ideas for additional custom skills? See `CUSTOMIZE.md` for templates and examples.

**Common additions:**
- Industry-specific SOW templates
- New contract frameworks (AICPA, APPM, IPA)
- Rate card integrations
- Client escalation workflows
- Historical trend analysis

---

## 📞 Support

- **For PMs:** Use the Claude interface, ask questions naturally
- **For Engineers:** Check `skill.md` for full function specs
- **For Customization:** See `CUSTOMIZE.md` and skill template examples

---

**Built with Anthropic Agent Skills** | Last Updated: 2026-07-07 | v1.0.0  
**Maintained by:** [Your Team] | **For questions:** [contact]
