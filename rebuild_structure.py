import os
import shutil
from pathlib import Path

repo_root = Path(__file__).parent.parent

# Mapping of flattened file names to original paths
for flat_file in repo_root.glob("*__*"):
    if flat_file.name in ["rebuild_structure.py", "README.md"]:
        continue
    # Reverse the "__" back to "/"
    original_path = Path(str(flat_file.name).replace("__", "/"))
    dest_path = repo_root / original_path
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(flat_file), str(dest_path))

# Move rebuild script and workflow into .github/scripts for archival
archive_dir = repo_root / ".github" / "scripts"
archive_dir.mkdir(parents=True, exist_ok=True)
shutil.move(str(repo_root / "rebuild_structure.py"), archive_dir / "rebuild_structure.py")

print("Folder structure restored successfully.")
