import shutil
from pathlib import Path

repo_root = Path(__file__).resolve().parent

# Skip lists so we don't try to modify workflow files via Actions
skip_exact = {"rebuild_structure.py", "README.md"}
skip_prefixes = {
    "autobuild_workflow__",      # old flattened name (if present)
    ".github__workflows__",      # flattened workflow files (e.g., pages.yml)
}

# Move flattened files like "docs__index.md" -> "docs/index.md"
for flat_file in repo_root.glob("*__*"):
    name = flat_file.name
    if name in skip_exact or any(name.startswith(p) for p in skip_prefixes):
        continue
    dest = repo_root / Path(name.replace("__", "/"))
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(flat_file), str(dest))

# Archive this script into .github/scripts for reference
archive_dir = repo_root / ".github" / "scripts"
archive_dir.mkdir(parents=True, exist_ok=True)
shutil.move(str(repo_root / "rebuild_structure.py"), str(archive_dir / "rebuild_structure.py"))

print("Folder structure restored successfully (workflow files were skipped).")
