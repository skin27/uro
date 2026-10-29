# Uro

A constructed language for Europe

## Rules

The basic rules for the construction of new words is as follows

1. Use the international form if available.
2. Otherwise use the common root from European languages
3. Otherwise use a familiar word (commonly known)
4. Otherwise use the English word

### Orthography & Phonetics

One letter, one sound. See **[`grammar/pronunciation.md`](grammar/pronunciation.md)** for the full letter-to-sound table, stress rule and spelling rules.

- **`k` vs `c`**: Always use `k` for the hard `/k/` sound (e.g. `kalendar`, `klub`, `koktail`, `blanko`). Use `s` for `/s/` (e.g. `sol`, `sistem`). A Latin `c` before *e* or *i* becomes `z`, pronounced /ts/ or /z/ (e.g. `ziti`, `dezember`, `zigarette`, `sozial`). `c` is only used in `ch` for `/tʃ/` (e.g. `chiko`, `chika`).
- **`i` vs `y`**: Do not use `y` for vowel sounds; use `i` instead, both at the end of words (e.g. `famili`, `ziti`, `enemi`, `universiti`, `whiski`) and internally (e.g. `sistem`).
- **Stress**: always on the second-to-last syllable (`VI-der`, `ka-LEN-dar`).

### Grammar & Morphology (Max 2 Variants)

Unlike strictly schematic languages such as Esperanto that enforce a single artificial suffix for every part of speech, Uro intentionally preserves a natural European feel by allowing **at most two valid variants** for morphological and syntactic forms.

See **[`grammar/grammar.md`](grammar/grammar.md)** for the full grammar specification (including EBNF syntax rules):

- **Word Order**: Strict `SVO` (Subject–Verb–Object), with invariant adjectives always before the noun (`novo dom`).
- **Articles**: Invariant `un` (a/an) and `de` (the).
- **Noun Plurals (2 variants)**: `-s` (`libres`, `ninios`) or `-i` (`brati`, `domi`).
- **Pronouns & Possessives**: Personal pronouns ([`pronoun/personal_pronoun.md`](pronoun/personal_pronoun.md)), object pronouns `me`/`nos` and reflexive `se` ([`pronoun/object_pronoun.md`](pronoun/object_pronoun.md)), and possessives ([`pronoun/possessive_pronoun.md`](pronoun/possessive_pronoun.md)).
- **Verbs & Tenses (2 variants)**:
  - Base forms use either bare roots (`hor`, `go`, `work`) or `-er` (`vider`, `parler`, `speler`, `jester`).
  - Past: `haf vider` or `videred`. Future: `wil vider` or `go vider`. Conditional: `wud vider`.
  - Modals take a bare verb (`Je voler go.`); `las` + object + verb means *let* (`Las nos go!`); the imperative is the base form (`Go!`).
- **Adverbs & Comparison**: bare adjective or `-li` (`rapid` / `rapidli`); `plus` / `de plus` / `min` / `minst` + adjective, `niz` = than.
- **Prepositions**: `in`, `fon` (of), `od` (from), `a` (to), `op` (on), `mit` / `bez` (with/without), `pro` (for), `pre` / `post` (before/after), `trans` (across), `vers` (toward), `trots` (despite), …
- **Conjunctions**: `i`, `o`, `ale`, `if`, `dat` (that), `ke` (which, who) and `niz` (than); compounds such as `mem if` (although) and `durant ke` (while).
- **Negation**: `not` placed before the verb (`je not vider`); the answer is `no`. Negative words such as `nulting` and `nikdi` work with or without `not` (2 variants).
- **Questions (2 variants)**: `SVO?` (`Ju parler Uro?`) or Verb–Subject inversion (`Parler ju Uro?`). Question words `ki`, `ke`, `wo`, `kando`, `komo`, `kuanto`, `kual`, `pro ke`.
- **Word Formation**: international affixes (`-ist`, `-zion`, `-iti`, `-ik`, `non-`, `re-`, …) and a conversion table for international words, see [`grammar/word_formation.md`](grammar/word_formation.md).

The language is versioned; see [`grammar/changelog.md`](grammar/changelog.md) and the plan for the next version in [`plans/v0.4.md`](plans/v0.4.md). `python tools/coverage.py` reports how many of the 1000 most common English words have a Uro word. A sample text is in [`texts/north_wind_and_sun.md`](texts/north_wind_and_sun.md).

## Vocabulary

Examples of the vocabulary can be found in the various markdown files:

- **Basics**:
  - [`basic/basic.md`](basic/basic.md) — Core everyday vocabulary
  - [`basic/international.md`](basic/international.md) — International words
  - [`basic/everyday.md`](basic/everyday.md) — Everyday nouns (person, thing, place, money, language…)
  - [`basic/travel.md`](basic/travel.md) — Travel & services
  - [`basic/people.md`](basic/people.md) — People & roles
  - [`basic/home.md`](basic/home.md) — Home, things & materials
  - [`basic/places.md`](basic/places.md) — Places & directions
  - [`basic/health.md`](basic/health.md) — Health
  - [`basic/society.md`](basic/society.md) — Society, politics & law
  - [`basic/work.md`](basic/work.md) — Business, money & work
  - [`basic/media.md`](basic/media.md) — Knowledge, media & technology
  - [`basic/leisure.md`](basic/leisure.md) — Arts, sport & leisure
  - [`basic/abstract.md`](basic/abstract.md) — Abstract nouns
  - [`basic/phrases.md`](basic/phrases.md) — Greetings & useful phrases
  - [`basic/adjectives.md`](basic/adjectives.md) — Common adjectives & opposites
  - [`basic/adjectives_international.md`](basic/adjectives_international.md) — International adjectives (`-al`, `-ik`, `-iv`, …)
  - [`basic/adverbs.md`](basic/adverbs.md) — Adverbs of time, place & degree; yes/no
  - [`basic/prepositions.md`](basic/prepositions.md) — Prepositions
  - [`basic/conjunctions.md`](basic/conjunctions.md) — Conjunctions
  - [`basic/questions.md`](basic/questions.md) — Question words
  - [`basic/nature_time.md`](basic/nature_time.md) — Time, nature, animals & world
  - [`basic/food_body.md`](basic/food_body.md) — Food, drink & body parts
  - [`basic/colours.md`](basic/colours.md) — Colours
  - [`basic/family.md`](basic/family.md) — Family & kinship
  - [`basic/daysofweek.md`](basic/daysofweek.md) — Days of the week
  - [`basic/months.md`](basic/months.md) — Months of the year
  - [`basic/seasons.md`](basic/seasons.md) — Seasons
- **Pronouns**:
  - [`pronoun/personal_pronoun.md`](pronoun/personal_pronoun.md) — Personal pronouns
  - [`pronoun/object_pronoun.md`](pronoun/object_pronoun.md) — Object & reflexive pronouns
  - [`pronoun/possessive_pronoun.md`](pronoun/possessive_pronoun.md) — Possessive pronouns
  - [`pronoun/demonstrative.md`](pronoun/demonstrative.md) — Demonstratives & quantifiers
- **Verbs**:
  - [`verbs/verbs.md`](verbs/verbs.md) — Common core verbs
  - [`verbs/to_be.md`](verbs/to_be.md) — Present conjugation of *to be* (`ar`)
  - [`verbs/to_have.md`](verbs/to_have.md) — Present conjugation of *to have* (`haf`)
- **Numbers**:
  - [`numbers/numbers.md`](numbers/numbers.md) — Numerals, tens, hundreds & ordinals

These files contain:

1. **English** word
2. **Uro (M)** — **Canonical specification** (Manually curated pan-European vocabulary)
3. **Uro (AI)** — Historical/comparative baseline (AI-generated via ChatGPT)
4. **Other languages** — Reference comparison across 16 European languages (Germanic, Romance, and Slavic)
