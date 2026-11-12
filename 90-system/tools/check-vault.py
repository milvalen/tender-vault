#!/usr/bin/env python3
"""Check the vault against 90-system/documentation-standard.md.

Usage: python3 -I 90-system/tools/check-vault.py [VAULT]

Checks metadata, parent navigation, ASCII filenames, directory overviews,
local links and anchors, reachability from README/Home, JSON settings and
accidental secrets. Prints non-fatal warnings for sentences over 30 words and
banned phrases (see the documentation standard). Exit status 0 means no errors. Standard library only.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

REQUIRED = ["title", "type", "status", "owner", "created", "updated",
            "observed", "source", "sensitivity", "parent"]
TYPES = {"index", "reference", "plan", "record", "runbook", "standard", "template"}
STATUSES = {"draft", "proposed", "active", "verified", "historical", "planned",
            "deprecated", "template"}
NO_METADATA = {"AGENTS.md", "CLAUDE.md", "GEMINI.md", "PRODUCT.md", "DESIGN.md"}
NO_PARENT = {"README.md"}
SKIP_DIRS = {".git", ".obsidian", ".trash", "_private", "__pycache__", ".impeccable"}
SKIP_FILES = {".gitignore", ".gitattributes", ".DS_Store"}
ENTRY_PAGES = ["README.md", "Home.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md"]

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_ONLY_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
TARGET = r"((?:[^()\s]|\([^()\s]*\))+)"
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(" + TARGET + r"(?:\s+\"[^\"]*\")?\)")
EMBED = re.compile(r"!\[[^\]]*\]\(" + TARGET + r"\)")
FENCE = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")
SECRET = re.compile(r"(gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY|"
                    r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})")

errors = []
warnings = []
MAX_WORDS = 30
BANNED = re.compile(r"(?i)\b(etc\.?|and so on|soon|recently)(?!\w)")
LINT_SKIP = ("00-inbox/",)


def err(path, message):
    errors.append(f"{path}: {message}")


def warn(path, message):
    warnings.append(f"WARNING {path}: {message}")


def lint_prose(rel, body):
    """Soft ASD-STE100-style checks: long sentences and banned phrases."""
    text = FENCE.sub("", body)
    for line in text.split("\n"):
        line = line.strip()
        if not line or line.startswith(("|", "#", ">", "---")):
            continue
        line = re.sub(r"^([-*]|\d+\.)\s+(\[[ x]\]\s+)?", "", line)
        line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
        line = INLINE_CODE.sub("code", line).replace("**", "")
        m = BANNED.search(line)
        if m:
            warn(rel, f"banned phrase `{m.group(1)}`: {line[:60]!r}")
        for sentence in re.split(r"(?<=[.!?;])\s+", line):
            words = re.findall(r"\w+", sentence)
            if len(words) > MAX_WORDS:
                warn(rel, f"sentence has {len(words)} words (max {MAX_WORDS}): {sentence[:60]!r}")


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5:]


def parse_flat_yaml(raw, rel):
    meta = {}
    for line in raw.split("\n"):
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):(.*)$", line)
        if not m:
            err(rel, f"metadata line is not `key: value`: {line!r}")
            continue
        if m.group(1) in meta:
            err(rel, f"metadata key `{m.group(1)}` repeats")
        meta[m.group(1)] = m.group(2).strip()
    for k, v in meta.items():
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
            meta[k] = v[1:-1]
    return meta


def slug(heading):
    text = re.sub(r"[`*_~\[\]]|\(([^)]*)\)", "", heading.strip().lower())
    text = "".join(c for c in text if c in " -" or unicodedata.category(c)[0] in "LN")
    return text.replace(" ", "-")


def anchors(body):
    seen, result = {}, set()
    for line in FENCE.sub("", body).split("\n"):
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            s = slug(m.group(1))
            n = seen.get(s, 0)
            seen[s] = n + 1
            result.add(s if n == 0 else f"{s}-{n}")
    return result


def collect(vault):
    files = []
    for p in sorted(vault.rglob("*")):
        rel = p.relative_to(vault)
        if any(part in SKIP_DIRS for part in rel.parts) or not p.is_file():
            continue
        if p.name in SKIP_FILES:
            continue
        files.append(rel)
    return files


def main():
    vault = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]).resolve()
    files = collect(vault)
    pages = [f for f in files if f.suffix == ".md"]
    bodies, links = {}, {}

    for rel in files:
        if not all(ord(c) < 128 for c in rel.as_posix()):
            err(rel, "path is not ASCII")
        if rel.name.lower() == "index.md":
            err(rel, "use a directory-named overview, not index.md")
        if DATE_ONLY_NAME.match(rel.name):
            err(rel, "filename is only a date; name the subject")
    dirs = {rel.parent for rel in pages if rel.parent != Path(".") and "assets" not in rel.parts}
    for d in sorted(dirs):
        if not (vault / d / f"{d.name}.md").is_file():
            err(d, f"missing overview {d.name}/{d.name}.md")

    for rel in pages:
        text = (vault / rel).read_text(encoding="utf-8")
        raw, body = split_frontmatter(text)
        bodies[rel] = body
        if not rel.as_posix().startswith(LINT_SKIP):
            lint_prose(rel, body)
        if SECRET.search(text):
            err(rel, "possible credential or private key")
        if rel.name in NO_METADATA:
            continue
        if raw is None:
            err(rel, "missing YAML metadata")
            continue
        meta = parse_flat_yaml(raw, rel)
        is_template = meta.get("type") == "template"
        for k in REQUIRED:
            if k == "parent" and rel.as_posix() in NO_PARENT:
                continue
            if not meta.get(k):
                err(rel, f"missing metadata `{k}`")
        if meta.get("type") and meta["type"] not in TYPES:
            err(rel, f"unknown type `{meta['type']}`")
        if meta.get("status") and meta["status"] not in STATUSES:
            err(rel, f"unknown status `{meta['status']}`")
        for k in ("created", "updated"):
            v = meta.get(k, "")
            if v and not ISO_DATE.match(v) and not (is_template and "{{" in v):
                err(rel, f"`{k}` is not an ISO date: {v}")
        obs = meta.get("observed", "")
        if obs and obs != "unknown" and not ISO_DATE.match(obs):
            err(rel, f"`observed` is not an ISO date or unknown: {obs}")
        c, u = meta.get("created", ""), meta.get("updated", "")
        if ISO_DATE.match(c) and ISO_DATE.match(u) and u < c:
            err(rel, "`updated` is earlier than `created`")
        if rel.as_posix() in NO_PARENT:
            continue
        parent = meta.get("parent")
        if parent:
            if not (vault / rel.parent / parent).is_file():
                err(rel, f"parent does not exist: {parent}")
            elif not any(unquote(t).split("#")[0] == parent
                         for t in LINK.findall(FENCE.sub("", body))):
                err(rel, f"no visible link to parent {parent}")

    page_anchors = {rel: anchors(bodies[rel]) for rel in pages}
    for rel in pages:
        body = INLINE_CODE.sub("", FENCE.sub("", bodies[rel]))
        out = set()
        for target in LINK.findall(body) + EMBED.findall(body):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            path_part, _, frag = unquote(target).partition("#")
            full = (vault / rel.parent / path_part).resolve() if path_part else vault / rel
            if not full.is_relative_to(vault) or not full.is_file():
                err(rel, f"broken link: {target}")
                continue
            dest = full.relative_to(vault)
            out.add(dest)
            if frag and dest.suffix == ".md" and slug(frag) not in page_anchors.get(dest, set()) \
                    and frag not in page_anchors.get(dest, set()):
                err(rel, f"broken anchor: {target}")
        links[rel] = out

    seen = [Path(p) for p in ENTRY_PAGES if (vault / p).is_file()]
    reached = set(seen)
    while seen:
        for dest in links.get(seen.pop(), ()):
            if dest not in reached:
                reached.add(dest)
                seen.append(dest)
    for rel in files:
        if rel not in reached:
            err(rel, "not reachable from README or Home")

    for p in sorted((vault / ".obsidian").glob("*.json")):
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except ValueError as e:
            err(p.relative_to(vault), f"invalid JSON: {e}")

    if warnings:
        print("\n".join(warnings))
        print(f"{len(warnings)} warning(s) (do not fail the check)")
    if errors:
        print("\n".join(errors))
        print(f"FAILED: {len(errors)} error(s)")
        return 1
    print(f"OK: {len(pages)} Markdown pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
