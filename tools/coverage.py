"""Measure how many words of an English word list have a Uro translation.

Usage:
    python tools/coverage.py [word_list] [--missing]

The default word list is tools/top1000.txt (the EF top 1000 English words).

A word counts as covered when it is the head word of a cell in the `English`
column of a vocabulary table. Cells are read like this:
- `/` separates alternatives: `still / yet` covers *still* and *yet*.
- Text in parentheses is a note and is ignored: `to (direction)` covers *to*.
- A leading `to ` is dropped: `to be` covers *be*.
- Entries of more than one word are phrases and cover nothing: `how much`.

Some words have no table row because a grammar rule covers them. They are
listed in GRAMMAR below. Words that Uro leaves out on purpose are in SKIPPED.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB_DIRS = ["basic", "pronoun", "verbs", "numbers"]

# Words covered by a rule in grammar/grammar.md rather than by a table row.
GRAMMAR = {
    "a": "un (§2)",
    "the": "de (§2)",
    "be": "ar (§7)",
    "have": "haf (§7)",
    "will": "wil (§7)",
    "may": "kan (§7)",
    "child": "ninio (listed as children)",
    "others": "alters / alteri (plural of alter, §3)",
    "myself": "se (§4)",
    "yourself": "se (§4)",
    "himself": "se (§4)",
    "herself": "se (§4)",
    "itself": "se (§4)",
    "themselves": "se (§4)",
    "n't": "ne (§8)",
    "so": "so (§6)",
    "better": "mer bon (§6)",
    "best": "de mest bon (§6)",
}

# American or informal words that a European language does not need.
SKIPPED = {
    "american", "congress", "democrat", "republican", "attorney", "yard",
    "pm", "mr", "mrs", "oh", "yeah", "ok",
}


def table_words():
    """Return {english word: (uro, file)} for all vocabulary tables."""
    words = {}
    for folder in VOCAB_DIRS:
        for path in sorted((ROOT / folder).glob("*.md")):
            header = None
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.startswith("|"):
                    header = None
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if header is None:
                    header = cells
                    continue
                if set(line) <= set("|-: \t") or header[0].lower() != "english":
                    continue
                english = re.sub(r"\(.*?\)", " ", cells[0])
                for part in english.split("/"):
                    part = re.sub(r"^to ", "", part.strip().lower())
                    if part and " " not in part:
                        words.setdefault(part, (cells[1], path.relative_to(ROOT).as_posix()))
    return words


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    word_list = Path(args[0]) if args else ROOT / "tools" / "top1000.txt"
    lines = word_list.read_text(encoding="utf-8").splitlines()
    wanted = [w.strip() for w in lines if w.strip() and not w.startswith("#")]

    tables = table_words()
    in_tables = [w for w in wanted if w.lower() in tables]
    by_grammar = [w for w in wanted if w.lower() not in tables and w.lower() in GRAMMAR]
    skipped = [w for w in wanted if w.lower() in SKIPPED]
    covered = len(in_tables) + len(by_grammar)
    missing = [w for w in wanted
               if w.lower() not in tables and w.lower() not in GRAMMAR and w.lower() not in SKIPPED]

    print(f"Covered: {covered} / {len(wanted)} ({100 * covered / len(wanted):.1f}%)")
    print(f"  in vocabulary tables: {len(in_tables)}")
    print(f"  by grammar rules:     {len(by_grammar)}")
    print(f"Skipped on purpose: {len(skipped)}")
    print(f"Missing: {len(missing)}")
    if "--missing" in sys.argv:
        print()
        print(" ".join(missing))


if __name__ == "__main__":
    main()
