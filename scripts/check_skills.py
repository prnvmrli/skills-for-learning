#!/usr/bin/env python3
"""Lint the skills: frontmatter, code fences, NBSP, relative links and #anchors, plugin JSON.

Usage: python3 scripts/check_skills.py [repo_root]   (exit 1 on any failure)
"""
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
fails = set()


def fail(path, msg):
    fails.add(f"FAIL {path.relative_to(root)}: {msg}")


def strip_fences(path, text):
    """Return text with fenced blocks blanked out; report unclosed fences."""
    out, fence, start = [], None, 0
    for n, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is None and m:
            fence, start = m.group(1), n
            out.append("")
        elif fence and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2).strip():
            fence = None
            out.append("")
        else:
            out.append("" if fence else line)
    if fence:
        fail(path, f"fence opened at line {start} never closes")
    return "\n".join(out)


def slugs(md_path):
    # GitHub-style heading anchors.
    text = strip_fences(md_path, md_path.read_text())
    return {
        re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-")
        for h in re.findall(r"^#{1,6} +(.+?) *#*$", text, re.M)
    }


def check_links(path, prose, skill_root):
    targets = [t for t in re.findall(r"`[^`\n]*`|\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", prose) if t]
    targets += [str(skill_root / t) for t in re.findall(r"`(references/[^`]+\.md)`", prose)] if skill_root else []
    for t in targets:
        if re.match(r"^[a-z]+:", t):  # http:, mailto:, vscode: ...
            continue
        file_part, _, anchor = t.partition("#")
        target = (path.parent / file_part).resolve() if file_part else path
        if not target.exists():
            fail(path, f"broken link {t}")
        elif anchor and target.suffix == ".md" and anchor not in slugs(target):
            fail(path, f"broken anchor {t}")


for json_path in sorted((root / ".claude-plugin").glob("*.json")):
    try:
        json.loads(json_path.read_text())
    except ValueError as e:
        fail(json_path, f"invalid JSON: {e}")

for skill_dir in sorted(p for p in (root / "skills").iterdir() if p.is_dir()):
    if not (skill_dir / "SKILL.md").exists():
        fail(skill_dir, "skill directory has no SKILL.md")
for nested in (root / "skills").glob("*/*/**/SKILL.md"):
    fail(nested, "nested SKILL.md would register as an extra skill")

for md in sorted([root / "README.md", *(root / "skills").rglob("*.md")]):
    text = md.read_text()
    upstream = "upstream" in md.parts  # vendored verbatim; only fence/NBSP checks
    if "\u00a0" in text:
        fail(md, "contains non-breaking spaces")
    prose = strip_fences(md, text)
    skill_root = None
    if md.parent.parent == root / "skills" and md.name == "SKILL.md":
        skill_root = md.parent
        fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not fm:
            fail(md, "frontmatter missing or not closed with ---")
        else:
            name = re.search(r"^name: *(.*)$", fm.group(1), re.M)
            desc = re.search(r"^description: *(.*)$((?:\n[ \t]+.*)*)", fm.group(1), re.M)
            if not name or name.group(1).strip() != md.parent.name:
                fail(md, f"name must equal directory name '{md.parent.name}'")
            folded = desc and desc.group(1).strip() in (">", "|", ">-", "|-")
            if not desc or not (desc.group(2).strip() if folded else desc.group(1).strip()):
                fail(md, "empty description")
    elif "references" in md.parts:
        skill_root = md.parent.parent
    if not upstream:
        check_links(md, prose, skill_root)

print("\n".join(sorted(fails)) if fails else "OK: all skills pass")
sys.exit(1 if fails else 0)
