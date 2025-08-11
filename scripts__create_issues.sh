#!/usr/bin/env bash
# Requires: GitHub CLI (gh) authenticated and repo set as origin
set -euo pipefail

# Create milestones
for m in "Month 1" "Month 2" "Month 3" "Month 4" "Month 5" "Month 6" "Month 7" "Month 8" "Month 9" "Month 10" "Month 11" "Month 12"; do
  gh api repos/:owner/:repo/milestones -f title="$m" || true
done

# Import issues from CSV (uses GitHub's issues import)
# Fields: Title,Body,Labels,Milestone
python3 - <<'PY'
import csv, os, subprocess, json
repo = os.popen("gh repo view --json nameWithOwner -q .nameWithOwner").read().strip()
def create_issue(row):
    title, body, labels, milestone = row
    label_args = sum([["-l", l.strip()] for l in labels.split(",") if l.strip()], [])
    ms_number = None
    # Fetch milestone number by title
    ms = json.loads(subprocess.check_output(["gh","api",f"repos/{repo}/milestones"]).decode())
    for m in ms:
        if m["title"] == milestone:
            ms_number = m["number"]; break
    cmd = ["gh","issue","create","-t",title,"-b",body] + label_args
    if ms_number:
        cmd += ["-m", str(ms_number)]
    subprocess.check_call(cmd)

with open("issues.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # header
    for row in reader:
        create_issue(row)
PY
