#!/usr/bin/env python3
"""File Pruner: scans gcm-vault for the three cleanliness rules in 04_sop/audit.md.
Read-only. Prints violations for manual review; does not delete anything.

Usage:
    python3 file_pruner.py [vault_root] [desktop_path]

Defaults: vault_root=repo's gcm-vault/, desktop_path=~/Desktop
"""
import os
import re
import sys
from collections import defaultdict

VERSION_RE = re.compile(r"^(?P<base>.+?)_v(?P<ver>\d+)_(?P<date>\d{8})\.(?P<ext>\w+)$")


def find_vault_root():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(here, "..", ".."))


def rule1_stale_versions(vault_root):
    """Same base name, multiple versions: only newest + second newest should remain outside 99_archive."""
    groups = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(vault_root):
        if "99_archive" in dirpath.split(os.sep):
            continue
        for fn in filenames:
            m = VERSION_RE.match(fn)
            if m:
                key = (dirpath, m.group("base"), m.group("ext"))
                groups[key].append((int(m.group("ver")), m.group("date"), fn))

    violations = []
    for key, items in groups.items():
        items.sort(reverse=True)
        if len(items) > 2:
            for ver, date, fn in items[2:]:
                violations.append(os.path.join(key[0], fn))
    return violations


def rule2_deprecated_outside_archive(vault_root):
    violations = []
    for dirpath, dirnames, filenames in os.walk(vault_root):
        if "99_archive" in dirpath.split(os.sep):
            continue
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    head = f.read(2000)
            except OSError:
                continue
            if re.search(r"^status:\s*deprecated\s*$", head, re.MULTILINE):
                violations.append(path)
    return violations


def rule3_duplicated_on_desktop(vault_root, desktop_path):
    violations = []
    if not os.path.isdir(desktop_path):
        return violations
    vault_names = {}
    for dirpath, dirnames, filenames in os.walk(vault_root):
        for fn in filenames:
            vault_names.setdefault(fn, []).append(os.path.join(dirpath, fn))
    for dirpath, dirnames, filenames in os.walk(desktop_path):
        for fn in filenames:
            if fn in vault_names:
                for vp in vault_names[fn]:
                    violations.append((os.path.join(dirpath, fn), vp))
    return violations


def main():
    vault_root = sys.argv[1] if len(sys.argv) > 1 else find_vault_root()
    desktop_path = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser("~/Desktop")

    print(f"Vault root: {vault_root}")
    print(f"Desktop path checked: {desktop_path}\n")

    v1 = rule1_stale_versions(vault_root)
    print(f"[Rule 1] Stale versions beyond latest+previous ({len(v1)}):")
    for p in v1:
        print(f"  - {p}")

    v2 = rule2_deprecated_outside_archive(vault_root)
    print(f"\n[Rule 2] status: deprecated outside 99_archive/ ({len(v2)}):")
    for p in v2:
        print(f"  - {p}")

    v3 = rule3_duplicated_on_desktop(vault_root, desktop_path)
    print(f"\n[Rule 3] Files duplicated on Desktop ({len(v3)}):")
    for desktop_file, vault_file in v3:
        print(f"  - {desktop_file}  <->  {vault_file}")

    total = len(v1) + len(v2) + len(v3)
    print(f"\nTotal violations: {total}. This script does not delete anything — review then remove manually.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
