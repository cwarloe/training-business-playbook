# Training Business Playbook

This repository scaffolds everything needed to launch a premium, $1,000-per-person 1–2 day training within 12 months.

## What's Inside
- **12-Month Plan**: `assets/Training_Business_12_Month_Plan.xlsx`
- **Docs Site (MkDocs)**: content in `docs/` and `mkdocs.yml` for GitHub Pages
- **Curriculum**: workshop agendas, exercises, handouts in `curriculum/`
- **Marketing**: landing page copy, emails, social content in `marketing/`
- **Sales**: objection handling, CRM sheets, pricing tiers in `sales/`
- **Ops**: checklists, SOPs, venue/virtual runbooks in `ops/`
- **Automation**: placeholders for email sequences and outreach in `automation/`
- **Issues & Project**: `issues.csv` to import into GitHub as issues with labels/milestones
- **Workflows**: `.github/workflows/pages.yml` deploys the docs site on push to `main`

## Quick Start

1. **Create the repo on GitHub** (empty, no README).
2. **Clone and populate**:
   ```bash
   git clone <YOUR_REPO_URL> training-business
   cd training-business
   ```
3. **Copy these files into the repo** (unzipped bundle contents).
4. **Commit & push**:
   ```bash
   git add .
   git commit -m "Initial commit: training business playbook"
   git push origin main
   ```
5. **Enable Pages** (if using MkDocs deploy workflow below):
   - Settings → Pages → Source: **GitHub Actions**

6. **Import Issues**:
   - Go to **Issues** → **Import** → upload `issues.csv` to create pre-scoped work items.

7. **Install mkdocs-material (optional for local preview)**:
   ```bash
   pip install mkdocs mkdocs-material
   mkdocs serve
   ```

## Structure

```
.
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── 01_feature_request.md
│   │   ├── 02_bug_report.md
│   │   └── 03_task.md
│   └── workflows
│       └── pages.yml
├── automation/
├── assets/
│   └── Training_Business_12_Month_Plan.xlsx
├── curriculum/
├── docs/
│   ├── index.md
│   ├── offer.md
│   ├── curriculum.md
│   ├── marketing.md
│   ├── sales.md
│   └── ops.md
├── marketing/
├── ops/
├── sales/
├── scripts/
│   └── create_issues.sh
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── mkdocs.yml
├── issues.csv
└── README.md
```

---

*Generated on 2025-08-11.*
