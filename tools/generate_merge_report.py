#!/usr/bin/env python3
"""Generate a tidy Markdown report listing merged/redirected files and their targets.

Writes the report to tools/reports/merge_report.md and prints the path.
"""
from pathlib import Path
import re
import os
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
BACKUPS = ROOT / '.linkfix_backups'
OUT_DIR = ROOT / 'tools' / 'reports'
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / 'merge_report.md'

def latest_backup_dir():
    if not BACKUPS.exists():
        return None
    dirs = sorted([p for p in BACKUPS.iterdir() if p.is_dir()])
    return dirs[-1] if dirs else None

def find_merged_files(root: Path):
    merged = []
    for p in root.rglob('*.md'):
        # skip backups
        if '.linkfix_backups' in str(p):
            continue
        try:
            text = p.read_text(encoding='utf-8', errors='ignore')
        except OSError:
            continue
        if 'merged_into:' in text or 'This file has been merged into' in text:
            merged.append((p, text))
    return merged

def extract_target(text):
    # Look for YAML-like merged_into: <path>
    m = re.search(r'^merged_into:\s*(.+)$', text, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    # Fallback: look for 'This file has been merged into [Name](path)'
    m2 = re.search(r'This file has been merged into .*\(([^)]+)\)', text)
    if m2:
        return m2.group(1).strip()
    return None

def human_rel(pathstr, root=ROOT):
    try:
        p = Path(pathstr)
        if p.is_absolute():
            try:
                return p.relative_to(root)
            except Exception:
                return p
        return Path(pathstr)
    except Exception:
        return pathstr

def main():
    merged = find_merged_files(ROOT)
    bp = latest_backup_dir()

    rows = []
    for p, text in sorted(merged, key=lambda x: str(x[0])):
        target = extract_target(text)
        if not target:
            target = '(unknown)'
        # normalize to repo-relative path if possible
        target_rel = human_rel(target)
        backup_exists = False
        backup_path = None
        if bp:
            maybe = bp / p.relative_to(ROOT)
            if maybe.exists():
                backup_exists = True
                backup_path = maybe

        rows.append((p.relative_to(ROOT), str(target_rel), 'yes' if backup_exists else 'no', str(backup_path) if backup_path else ''))

    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')
    header = f"# Merge / Redirect Report\n\nGenerated: {now} (UTC)\n\nLatest backup: {bp if bp else '(none found)'}\n\n"

    table_lines = []
    table_lines.append('| File | Redirects to | Backup available | Backup path |')
    table_lines.append('|---|---|---:|---|')
    for f, t, has, bpath in rows:
        table_lines.append(f'| `{f}` | `{t}` | {has} | `{bpath}` |')

    summary = f"\nTotal merged/redirect files found: {len(rows)}\n\n"

    OUT_PATH.write_text(header + '\n'.join(table_lines) + summary, encoding='utf-8')
    print('Wrote report to', OUT_PATH)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
