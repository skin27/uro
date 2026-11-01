"""Check the Uro (M) forms in the vocabulary tables against the spelling rules.

Usage:
    python tools/lint.py

Only the mechanical rules of grammar/pronunciation.md are checked:
- `c` only in `ch`, no `q`, `x` or `y`, only the letters a to z.
- No `th`, `wh`, `ph` or `ck`.
- No `-tion` or `-sion`, because the ending is `-zion`.
- No `-le` at the end of a word, because the ending is `-el`.
- No double letter, unless two word parts meet (ALLOWED_DOUBLE).
- No two words that differ only by a double letter or by `w` / `v` (SOUND_ALIKE).

Exits with 1 when a form breaks a rule.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB_DIRS = ["basic", "pronoun", "verbs", "numbers"]

# Two word parts meet: real + li, okt + ten. `zoo` has two syllables.
ALLOWED_DOUBLE = {"realli", "spezialli", "oktten", "oktti", "setten", "setti", "zoo"}

# The word class tells these apart (pronunciation.md, beginning).
SOUND_ALIKE = {frozenset(("win", "vin"))}

PATTERNS = [
    (r"c(?!h)", "`c` outside `ch`"),
    (r"[qxy]", "`q`, `x` or `y`"),
    (r"[^a-z]", "a letter outside a to z"),
    (r"th|wh|ph|ck", "`th`, `wh`, `ph` or `ck`"),
    (r"[ts]ion", "`-tion` or `-sion`"),
    (r"[^aeiou]le$", "`-le` at the end"),
]


def table_forms():
    """Return {uro form: set of (english, file)} for all vocabulary tables."""
    forms = {}
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
                if set(line) <= set("|-: \t") or "Uro (M)" not in header:
                    continue
                row = dict(zip(header, cells))
                cell = re.sub(r"\(.*?\)", " ", row["Uro (M)"])
                for form in re.split(r"[/,]", cell):
                    form = form.strip(" -").lower()
                    if form and form != "—" and " " not in form:
                        place = (row.get("English", ""), path.relative_to(ROOT).as_posix())
                        forms.setdefault(form, set()).add(place)
    return forms


def check_form(form):
    """Return the rules that a single form breaks."""
    broken = [message for pattern, message in PATTERNS if re.search(pattern, form)]
    if re.search(r"(.)\1", form) and form not in ALLOWED_DOUBLE:
        broken.append("double letter")
    return broken


def sound_alike(forms):
    """Return pairs of forms that can sound the same."""
    pairs = []
    for form in sorted(forms):
        for other in (re.sub(r"(.)\1", r"\1", form), form.replace("w", "v")):
            if other != form and other in forms and frozenset((form, other)) not in SOUND_ALIKE:
                pairs.append((form, other))
    return pairs


def main():
    forms = table_forms()
    problems = 0
    for form in sorted(forms):
        for message in check_form(form):
            english, path = sorted(forms[form])[0]
            print(f"{path}: {form} ({english}): {message}")
            problems += 1
    for form, other in sound_alike(forms):
        print(f"{form} and {other} can sound the same")
        problems += 1
    print(f"{len(forms)} forms checked, {problems} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
