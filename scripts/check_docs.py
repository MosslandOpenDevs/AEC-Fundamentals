#!/usr/bin/env python3
"""Documentation integrity checks for AEC-Fundamentals (stdlib only).

Verifies, without any third-party dependency, that the Markdown will render on
GitHub the way authors intend:

  1. emphasis (**bold**) that cannot render due to CommonMark flanking rules
     (e.g. `**용어(Eng)**한글` — a closing ** after ')' before a letter);
  2. a standalone <img> glued to the next line of Markdown (HTML-block trap);
  3. a paragraph line immediately followed by `---` (accidental SETEXT heading);
  4. every knowledge topic has BOTH a .kor.md and a .eng.md;
  5. relative Markdown links and <img>/![] references resolve to real files;
  6. tracked .md/.csv files use LF (no CRLF).

Exit code is non-zero if any check fails.
"""
import os, re, sys, glob, urllib.parse, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errors = []


def err(msg):
    errors.append(msg)


# ---- CommonMark flanking (matches cmark-gfm for these cases) ----
def _cat(c):
    return unicodedata.category(c) if c else "Zs"


def _ws(c):
    return (not c) or c in " \t\n" or _cat(c) == "Zs"


def _punct(c):
    return bool(c) and (_cat(c).startswith("P") or _cat(c).startswith("S"))


def left_flanking(prev, nxt):
    if _ws(nxt):
        return False
    if _punct(nxt) and not (_ws(prev) or _punct(prev)):
        return False
    return True


def right_flanking(prev, nxt):
    if _ws(prev):
        return False
    if _punct(prev) and not (_ws(nxt) or _punct(nxt)):
        return False
    return True


def md_files():
    fs = glob.glob("AEC-Architecture/**/*.md", recursive=True)
    fs += glob.glob("AEC-Architecture/**/*.MD", recursive=True)
    fs += glob.glob("docs/**/*.md", recursive=True)
    fs += ["README.md"]
    return sorted(set(fs))


def check_emphasis_and_structure():
    for f in md_files():
        lines = open(f, encoding="utf-8").read().split("\n")
        incode = False
        for i, line in enumerate(lines):
            s = line.strip()
            if s.startswith("```"):
                incode = not incode
                continue
            if incode:
                continue
            test = re.sub(r"`[^`]*`", "", line)  # drop inline code spans
            for m in re.finditer(r"\*\*(.+?)\*\*", test):
                o, c = m.start(), m.end() - 2
                po = test[o - 1] if o > 0 else ""
                no = test[o + 2] if o + 2 < len(test) else ""
                pc = test[c - 1] if c > 0 else ""
                nc = test[c + 2] if c + 2 < len(test) else ""
                if not (left_flanking(po, no) and right_flanking(pc, nc)):
                    err(f"{f}:{i+1}: bold will not render (flanking): {m.group(0)[:50]!r}")
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            if re.fullmatch(r"<img\b[^>]*>", s) and nxt and not nxt.startswith("<"):
                err(f"{f}:{i+1}: <img> glued to Markdown text (add a blank line after it)")
            if (
                nxt and set(nxt) in ({"-"}, {"="}) and s
                and not s.startswith(("#", ">", "|", "- ", "* ", "+ ", "<"))
                and not (len(s) >= 2 and s[0].isdigit() and s[1] in ").")
            ):
                err(f"{f}:{i+1}: paragraph followed by '{nxt[:3]}' becomes a SETEXT heading (add a blank line)")


def check_pairs():
    groups = {}
    for f in glob.glob("AEC-Architecture/**/*.md", recursive=True):
        b = os.path.basename(f)
        for suf in (".kor.md", ".eng.md"):
            if b.endswith(suf):
                groups.setdefault(os.path.join(os.path.dirname(f), b[: -len(suf)]), set()).add(suf)
    for stem, s in sorted(groups.items()):
        if s != {".kor.md", ".eng.md"}:
            missing = {".kor.md", ".eng.md"} - s
            err(f"{stem}: missing language pair {sorted(missing)}")


def check_links_and_images():
    for f in md_files():
        d = os.path.dirname(f)
        src = open(f, encoding="utf-8").read()
        targets = []
        # ![](img): destination is whitespace-delimited in Markdown
        targets += re.findall(r"!\[[^\]]*\]\(<?([^)>\s]+)>?\)", src)
        # <img src="...">: quote-delimited — keep spaces (valid in HTML attributes)
        targets += re.findall(r"<img[^>]*\ssrc=[\"']([^\"']+)[\"']", src)
        # [text](dest ["title"]): strip an optional trailing title only
        for dest in re.findall(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)", src):
            dest = dest.strip()
            mt = re.match(r"^(<[^>]+>|\S+)(?:\s+[\"'].*[\"'])?$", dest)
            if mt:
                dest = mt.group(1).strip("<>")
            targets.append(dest)
        for t in targets:
            t = t.strip()
            if t.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            t = t.split("#")[0]
            if not t:
                continue
            p = os.path.normpath(os.path.join(d, urllib.parse.unquote(t)))
            if not os.path.exists(p):
                err(f"{f}: broken relative link/image -> {t}")


def check_crlf():
    for pat in ("**/*.md", "**/*.MD", "**/*.csv"):
        for f in glob.glob(pat, recursive=True):
            if f.startswith(".git/"):
                continue
            if b"\r\n" in open(f, "rb").read():
                err(f"{f}: contains CRLF line endings (use LF)")


def main():
    check_emphasis_and_structure()
    check_pairs()
    check_links_and_images()
    check_crlf()
    if errors:
        print(f"✗ {len(errors)} documentation issue(s):\n")
        for e in errors:
            print("  -", e)
        return 1
    print("✓ all documentation checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
