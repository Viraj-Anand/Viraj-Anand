"""Small README sanity checks."""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]*)\)")
SECRET_RE = re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16})")


def find_bad_links(text):
    """Return links with empty text/target or a non-https absolute URL."""
    bad = []
    for label, url in LINK_RE.findall(text):
        if not label or not url or url.startswith("http://"):
            bad.append((label, url))
    return bad


def find_secrets(text):
    return SECRET_RE.findall(text)


def main(path="README.md"):
    text = Path(path).read_text(encoding="utf-8")
    problems = find_bad_links(text) + find_secrets(text)
    for p in problems:
        print("problem:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:2]))
