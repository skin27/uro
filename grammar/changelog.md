# Uro Changelog

Uro follows [semantic versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`), as proposed in the design blog:

- **MAJOR**: breaking changes to grammar or core vocabulary.
- **MINOR**: new grammar or vocabulary that is backwards compatible.
- **PATCH**: fixes to spelling or tables, with no change in meaning.

While Uro is below `1.0`, any minor version may still contain breaking changes.

---

## Unreleased: 0.4 review

A word-by-word review of the 0.4 vocabulary, logged in [`plans/review_0.4.md`](../plans/review_0.4.md).

- Nouns: `aktion` (action, was `aksion`), `suma` (amount, was `kuantiti`), `analisis` (analysis, was `analiz`), `pristup` (approach, was `aproch`).
- Verbs: `admit` (was `admiter`), `influer` (affect, was `afekter`), `permit` (allow, was `permiter`), `demander` (ask, was `frager`), `asumer` (assume, was `suposer`). *Wonder* follows *ask*: `demander se` (was `frager se`).
- Function words: `skoro` (almost, was `kuasi`), `langs` (along, was `long`; `long` stays the adjective), `tambjen` (also, was `auk`), `jak` (as, like, was `komo`; *as … as* is now `so … jak`, and `komo` stays *how*). The reserved list and the EBNF are updated.
- Nouns: `kondukt` (behavior, was `komportament`), `budova` (building, was `edifisio`), `kura` (care, was `sorg`; *worry* stays `sorg`).
- Verbs: `biter` (beat, hit, was `bater`), `devener` (become, was `werd`), `verer` (believe, was `kreder`).
- Adjective: `rodjen` (born, was `nat`).
- Conjunction: `ale` (but, however, was `ma`). The reserved list and the EBNF are updated.
- **Breaking spelling rule**: a Latin *c* before *e* or *i* is now written `z`, and `z` is pronounced /ts/ (as in German *Zentrum*, Italian *grazie*) or /z/. About 60 words were respelled, among them `ziti` (city, town), `zentrum`, `zentral`, `zivil`, `zitadin`, `dezember`, `zigarette`, `poliz`, `sozial`, `spezial`, `prozes`, `kapaziti`, `akzepter`, `dezider` / `dezision`, `produzer`, `reziver`, `plaz` (place, site; `in plaz fon`), `priz`, `serviz`, `zent` (100), `konduzer` (drive, lead). *sc* (`sijensa`) is unchanged.
- Other words: `kariera` (career, was `karijera`), `zenturi` (century, was `sekul`), `zertan` (certain, was `sert`), `stul` (chair, was `stol`), `okasion` (chance, was `shans`), `lader` (charge, was `lad`), `reklamer` (claim, was `afirmer`), `fermer` (close, was `kloz`).
- `delikt` (crime, was `krimen`), `rezer` (cut, was `tajer`), `design` (design, was `dizain`), `trots` (despite, was `malgre`; the reserved list and the EBNF are updated).
- `hund` (dog, was `dog`), `drop` (drop, was `las fal`), `emploje` (employee; *worker* stays `workor`), `enter` (enter, was `entrer`), `entero` (entire; *whole* stays `hel`), `medio` (environment, was `ambijent`), `ekologik` (environmental, was `ambijental`), `etabler` (establish, was `stabiler`), `ever` (ever, was `unka`), `eksist` (exist, was `eksister`).
- `pole` (field, was `kamp`), `flai` (fly, was `flig`), `sleder` (follow, was `folg`), `reziper` (get, receive, was `reziver`), `government` (was `guvern`), `terra` (ground, earth, was `tera`), `viser` (hang, was `hang`), `herz` (heart, was `kord`).
- New preposition `od` (from); `fon` now means only *of*. `od kando` (since) and `od novo` (again) follow. The reserved list and the EBNF are updated.
- `improver` (improve, was `meliorer`), `interviu` (was `intervju`), `problem` (issue, was `kestion`), `kuchnia` (kitchen, was `kuchin`), `kenner` (know, was `znar`; *recognize* is `rekenner`), `kennis` (knowledge, was `znanje`), `leger` (lay, put, set, was `leg`), `lider` (leader, was `shef`), `nivo` (level, was `nivel`), `liger` (lie, was `lig`), `multi` (a lot, was `mult`), `amer` (love, was `luber`).
- **Breaking**: the ending *-tion* / *-sion* is now `-zion` (`nazion`, `nazional`, `informazion`, `dezizion`, `stazion`, `televizion`, `internazional`, …), like Italian *-zione* and German *-tion*. word_formation.md and pronunciation.md are updated.
- **Breaking, comparison**: `plus` (more) and `de plus` (most), like French *plus / le plus* and Italian *più / il più*: `plus bon` (better), `de plus bon` (best), `plus tard` (later). `mer` and `mest` are gone; `min` / `minst` stay.
- **Breaking, negation**: `not` before the verb (`Je not vider.`), `no` as the answer, `not … not` for *neither … nor*. `ne` is gone. `nikdi` (never, was `nunka`).
- `mashina` (machine), `magazin` (magazine), `manajement` (management), `matrimonio` (marriage), `afer` (matter), `messager` (message), `monni` (money), `monat` (month), `matin` (morning), `noht` (night), `biuro` (office).

---

## 0.4.0

Goal: cover the 1000 most common English words (see [`plans/v0.4.md`](../plans/v0.4.md)). Coverage is measured with `python tools/coverage.py`.

| Milestone | Coverage |
|-----------|---------:|
| 0.3.0 baseline | 30.9% |
| M1 function words | 37.5% |
| M2 verbs | 51.5% |
| M3 adjectives & adverbs | 62.9% |
| M4 everyday nouns | 76.2% |
| M5 international nouns | 98.8% |

The remaining 12 words are left out on purpose (*American, Congress, Democrat, Republican, attorney, yard, PM, Mr, Mrs, oh, yeah, ok*).

### Tooling (M0)
- New `tools/coverage.py` and `tools/top1000.txt` (the EF top 1000 English words).

### Grammar (M1)
- Conditional: `wud` + bare verb (`je wud go`, `je wud haf go`, `je wud kan go`). `if` clauses take the past for an unreal condition.
- `las` + object + bare verb (let): `Las nos go!`
- *Any* has no words of its own: `som` in questions and `if` clauses, `nul` with negation, `kada` for "any you like". `whatever` = `al ke`, `another` = `un alter`, `else` = `alter` after a pronoun.
- Negative words (`nul`, `nulting`, `nulun`, `nunka`) can be used with or without `ne` (2 variants); two negatives never cancel out. *Neither … nor* = `ne … ne`.
- New quantifiers `ambo` (both) and `vari` (several); adjectives `idem` (same), `tal` (such), `propri` (own).
- Degree words: `trop` (too), `genug` (quite, rather), `kuasi` (almost), `mem` (even).
- New prepositions: `trans` (across, beyond), `long` (along), `vers` (toward), `malgre` (despite), `segun` (according to), `inklusiv` (including), `in plas fon` (instead of). `in` / `eks` also mean *inside* / *outside*; `inter` also means *among*; `pre` + time means *ago*.
- Direction adverbs: `op` (up), `ab` (down, off), `weg` (away), `retur` (back), `avant` (ahead, forward).
- New conjunctions: `mem if` (although), `durant ke` (while), `fon kando` (since), `if` (whether), `o … o`, `ne … ne`, `ambo … i`.
- Question words: `ki` is also *whom*; `fon ki` is *whose*.
- Other adverbs: `unka` (ever, pairs with `nunka`), `just` (just), `un temp` (once), `samen` (together), `solo` (alone, also *only*), `bon` / `bonli` (well).
- The reserved word list and the EBNF include all new function words.

### International nouns (M5)
- New tables: [`society.md`](../basic/society.md) (35), [`work.md`](../basic/work.md) (26), [`media.md`](../basic/media.md) (42), [`leisure.md`](../basic/leisure.md) (17) and [`abstract.md`](../basic/abstract.md) (104), plus `kolor` in `colours.md`.
- Most words follow [`word_formation.md`](word_formation.md) §4: `informasion`, `sekuriti`, `teknologi`, `sistem`, `rezultat`, `kultur`.
- Nouns from Uro verbs by §3 (drop `-er`): `kres` (growth), `perd` (loss), `pens` (thought), `strel` (shot), `vid` (view), `spel` (game), `reserch` (research, *re-* + `serch`).
- Shared with an existing word, as in the main languages: `politik` (politics, policy, political), `histori` (history, story), `proses` (process, trial), `eleksion` (election, choice), `mir` (world, peace, like Russian *mir*), `film` (film, movie), `work` (work, job), `sorg` (worry, care), `problem` (problem, trouble).
- Two rows for two meanings: *party* (`parti` / `fest`), *race* (`korsa` / `rasa`), *rest* (`rest` / `repos`).
- New spelling rule in [`pronunciation.md`](pronunciation.md): *i* + *e* in two syllables is written `ije`, because `ie` is /i/. Earlier words were respelled: `klijent`, `pasijent`, `sijensist`, `proprijetar`, `ambijental`; new words use it too (`sosijeti`, `eksperijens`, `karijera`, `serija`).
- Fixed the 0.3 open point on Cyrillic letters in Latin transliterations (`[vrag]`, `[sestra]`, `[nikagda]`, `[togda]`, `[polovina]`).

### Everyday nouns (M4)
- New tables: [`people.md`](../basic/people.md) (44 rows), [`home.md`](../basic/home.md) (28), [`places.md`](../basic/places.md) (30) and [`health.md`](../basic/health.md) (10). Time words go to `nature_time.md` (13), body parts to `food_body.md` (6), and `sentiment`, `kalor`, `tref`, `peso` to `everyday.md`.
- Agent nouns take `-or` on the verb stem: `spelor` (player), `workor` (worker, employee), `trenor` (coach), `manejor` (manager). International ones keep their form: `direktor`, `profesor`, `instruktor`, `autor`.
- Like German *Mann* / *Frau*, Dutch *man* / *vrouw* and French *homme* / *femme*, `man` and `woman` also mean *husband* and *wife*.
- Compass points: `nord`, `sud`, `ost`, `west`; as modifiers they make the adjectives (`sud Europa`).
- Words shared with an existing meaning: `dom` (house, home), `karta` (map, card), `weg` (way, road), `siti` (city, town), `mort` (dead, death), `sena` (scene, stage), `publik` (public, audience), `personal` (personal, staff).
- Two meanings, two rows: *floor* (`pod`, surface / `etazh`, storey), *stage* (`sena` / `faza`), *drug* (`medikament` / `narkotik`).

### Adjectives & adverbs (M3)
- 36 new rows in `adjectives.md` and a new [`adjectives_international.md`](../basic/adjectives_international.md) with 62 international adjectives (`nasional`, `sosial`, `politik`, `publik`, `modern`, `posibel`, …).
- Pairs: `alto` / `bas` (high / low), `rano` / `tard` (early / late), `levo` / `pravo` (left / right), `ver` / `fals` (true / false, wrong), `korekt` (right, correct).
- One adjective where the families share one: `sekur` (safe, sure: German *sicher*, Swedish *säker*, Spanish *seguro*), `grand` (big, large, great), `hard` (hard, tough), `hel` (whole, entire).
- `aktual` means *current*, as in German *aktuell*, Polish *aktualny*, French *actuel* and Spanish *actual* (not English *actual*).
- *-ly* adverbs come from the adjective by grammar.md §6 (`klarli`, `normalli`). New adverb rows only for the irregular ones: `realli` (actually), `spesialli` (especially), `in efekt` (indeed), `kan ar` (perhaps), `mer tard` (later), `in kort` (soon), `dis nok` (tonight).
- `tools/coverage.py` counts an *-ly* adverb as covered when its adjective is in an adjectives table.

### Verbs (M2)
- 142 new rows in `verbs.md` (140 verbs; *lie* and *save* have two rows each, one per meaning).
- New [`word_formation.md`](word_formation.md) §5: Latin verbs take the shared Romance stem + `-er` (`aksepter`, `desider`, `ekspliker`, `kreater`, `identifiker`, `realizer`).
- Where the main language families use one verb for two English verbs, Uro does too: `porter` (carry, wear), `hold` (hold, keep), `leg` (put, lay, set), `konduser` (drive, lead), `paser` (pass, happen), `prober` (try, prove), `bater` (beat, hit), `aparer` (appear, seem), `kontroler` (control, check), `luk` (look, watch), `rester` (stay, remain), `treb` (need, require). Earlier verbs are reused for *talk* (`parler`), *tell* (`sag`) and *respond* (`responder`).
- Verb phrases: `las fal` (drop), `lever se` (rise), `frager se` (wonder), `ariver a` (reach). Derived verbs: `reznar` (recognize, from `znar`), `plener` (fill, from `plen`), `diskover` (discover, from `kover`), `remover` (remove, from `mover`).

### Vocabulary (M1)
- 54 new rows in `verbs.md`, `demonstrative.md`, `questions.md`, `conjunctions.md`, `prepositions.md` and `adverbs.md`.
- Existing rows now also list *these*, *those*, *somebody*, *everybody*, *thus*, *into*, *onto*, *upon* and *out*.

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
