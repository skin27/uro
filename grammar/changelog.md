# Uro Changelog

Uro follows [semantic versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`), as proposed in the design blog:

- **MAJOR**: breaking changes to grammar or core vocabulary.
- **MINOR**: new grammar or vocabulary that is backwards compatible.
- **PATCH**: fixes to spelling or tables, with no change in meaning.

While Uro is below `1.0`, any minor version may still contain breaking changes.

---

## 0.3.0

### Grammar
- New [`pronunciation.md`](pronunciation.md): letter-to-sound table, stress on the second-to-last syllable, and spelling rules for new words.
- New [`word_formation.md`](word_formation.md): affixes (`-ist`, `-or`, `-sion`, `-iti`, `-ism`, `-logi`, `-al`, `-ik`, `-iv`, `-li`, `non-`, `re-`, …), compounds, and a conversion table for international words.
- Object pronouns (`je` → `me`, `we` → `nos`; all others unchanged) and the reflexive `se`.
- Demonstratives `dis` / `dat` and quantifiers (`al`, `som`, `mult`, `poko`, `nul`, `kada`, `alter`).
- Adverbs: the bare adjective **or** `-li` (2 variants).
- Comparison: `mer` / `mest` / `min` / `minst` + adjective; `ke` (than); `so … komo` (as … as).
- Prepositions (`in`, `fon`, `a`, `op`, `mit`, `bez`, `pro`, `pre`, `post`, `eks`, …).
- Conjunctions: `i`, `o`, `ma`, `if`, `kando`, `komo`, and the universal subordinator `ke` (that / which / than).
- Question words: `ki`, `ke`, `wo`, `kando`, `komo`, `kuanto`, `kual`, `pro ke`; answers `ja` / `ne`.
- Verbs: a modal takes a bare verb (`je voler go`); causative `fakter` + object + verb; the imperative is the base form; the past of `ar` and `haf` is defined.
- Sample text: [`texts/north_wind_and_sun.md`](../texts/north_wind_and_sun.md).
- **Breaking**: the future suffix `-al` is removed (it clashed with the adjective suffix `-al` and created words like `goal` and `kanal`). The second future variant is now `go + verb`.
- **Breaking**: `on` is the default (gender-neutral) third-person singular; `ona` is the optional feminine form.
- Plural edge cases: nouns ending in `-s`/`-ks`/`-z`/`-sh`/`-ch` take `-es`, and nouns ending in `-i` take only `-s`.
- A list of reserved function words, so that new words do not clash with them.

### Vocabulary
- New tables: object pronouns, demonstratives & quantifiers, prepositions, conjunctions, question words, adverbs, phrases, everyday nouns, and travel & services.
- Verbs: 37 new verbs added.
- Numbers: tens (`triti` … `ninti`), `sent`, `mil`, `milion`, `miliard`, and ordinals (`prim`, `sekund`, then `-de`).
- **Breaking**: these words were changed to remove clashes:
  - `nos` (nose) → `nas`, because `nos` also means *our*.
  - `nein` (nine) → `nin`, because German speakers read *nein* as "no"; likewise `neinten` → `ninten`.
  - `ni` (never) → `nunka`, because it was too close to `ne` (not).
- **Breaking**: `c` is now used only in `ch`, so these spellings changed: `citi` → `siti`, `december` → `desember`, `dificil` → `difisil`, `facil` → `fasil`.
- `kneipe` (café) → `kafe`: rule 1 prefers the international word.

### Open points
- `jez`, `theater`, `whiski` and `zoo` do not yet follow the spelling rules (see [`pronunciation.md`](pronunciation.md)).
- Several existing tables have Cyrillic letters mixed into the Latin transliteration, e.g. `[vrаg]` in `basic.md` and `[sestrа]` in `family.md`.
- `ja` (yes) sits close to `je` (I) and `ju` (you), and Polish, Czech and Russian speakers read *ja* as "I". `da` (Slavic, Romanian) is the alternative.
- `vinti` (20) breaks the regular `-ti` pattern of the tens (`triti`, `firti`, …). `duti` is the regular alternative.

---

## 0.2.0 (repository, 2023–2026)

- Grammar specification with an EBNF ([`grammar.md`](grammar.md)).
- "At most two variants" principle.
- Plurals `-s` or `-i`.
- Past tense `haf + verb` or `-ed`; future tense `wil + verb` or `-al`.
- Pronouns `je`, `ju`, `on`, `ona`, `to`, `we`, `oni` and possessives.
- Verb classes: bare root or `-er`.
- Vocabulary tables with comparisons across European languages.

## 0.1.0 (design blog, January 2023)

The first design, published in the Medium series *URO: A new language for Europe*:

- 26-letter alphabet; spelling rules (`x` → `ks`, `q` → `ku`, `y` → `i`/`j`, `-le` → `-el`, no double final letters).
- SVO word order; articles `de` and `un`; gender-neutral by default.
- Plural `-s`/`-es`; invariant adjectives before the noun.
- Adverbs end in `-li` (`happi` → `happili`).
- Past tense `-id`, future tense `-os`.
- Capital letters only for names.
- Numbers `un` … `ten`.
- Word derivation rules: international word, then common root, then a familiar word, then English.
