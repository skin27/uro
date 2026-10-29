# Uro Grammar Specification

Uro is designed with an analytical, rule-based structure inspired by European language families (Germanic, Romance, and Slavic) while remaining simple enough to be parsed and validated like a programming language.

Where natural European languages diverge, Uro allows **at most two valid variants** for a grammatical construction.

Version: **0.3.0** (see [`changelog.md`](changelog.md)). Pronunciation and spelling: [`pronunciation.md`](pronunciation.md). Word formation: [`word_formation.md`](word_formation.md).

---

## 1. Word Order (Syntax)

- **Sentence Structure (`SVO`)**: Declarative sentences strictly follow **Subject – Verb – Object** order.
  - *Example*: `Je vider de dom.` ("I see the house.")
  - *Example*: `On haf un auto.` ("He has a car.")
- **Adjective Placement**: Adjectives always precede the noun (**`Adjective + Noun`**, Germanic/Slavic style) and are **invariant** (they do not change for gender, case, or plural).
  - *Example*: `un novo dom` ("a new house")
  - *Example*: `de bon libres` ("the good books")
- **Subordinate clauses keep `SVO`**. The verb never moves to the end (unlike German or Dutch).
  - *Example*: `Je znar ke on ar in de dom.` ("I know that he is in the house.")
- **Adverbs**: Manner adverbs follow the verb (or its object). Time and place adverbs go at the start or the end of the sentence.
  - *Example*: `On parler rapid.` ("He speaks fast.")
  - *Example*: `Morgen we go a Berlin.` / `We go a Berlin morgen.` ("Tomorrow we go to Berlin.")

---

## 2. Articles

Articles are **invariant** (they do not change for gender, number, or case) and precede the noun (or `Adjective + Noun` phrase):

| Type | Uro | English | Origin / Notes |
|------|-----|---------|----------------|
| **Indefinite** | `un` | a / an | Romance *un/uno/una*, Germanic *ein/een/en* (singular only) |
| **Definite** | `de` | the | Dutch *de*, Scandinavian *den/det/de*, English *the*, German *der/die* |

- *Examples*:
  - `un chiko` ("a boy")
  - `de chiko` ("the boy")
  - `de novo autos` ("the new cars")

---

## 3. Nouns & Plurals

- **Base Form**: Nouns in vocabulary tables are listed in their singular base form. There is no grammatical gender agreement or case inflection on nouns.
- **Pluralization (2 valid variants)**: Plurals are formed by adding either **`-s`** (Western: Romance/Germanic) or **`-i`** (Slavic/Italian/Romanian) to the singular noun:

| Noun ends in | Variant 1 | Variant 2 | Examples |
|--------------|-----------|-----------|----------|
| a consonant | `-s` | `-i` | `dom` → `doms` / `domi`; `brat` → `brats` / `brati` |
| `-s`, `-ks`, `-z`, `-sh`, `-ch` | `-es` | `-i` | `bus` → `buses` / `busi` |
| `-a`, `-e`, `-o`, `-u` | `-s` | `-i` replaces the vowel | `chiko` → `chikos` / `chiki`; `libre` → `libres` / `libri`; `ninio` → `ninios` / `ninii` |
| `-i` | `-s` | — | `siti` → `sitis`; `famili` → `familis`; `taksi` → `taksis` |

- **Gender**: Nouns are gender-neutral by default. Where a female form is wanted, the optional suffix **`-a`** marks it, usually replacing a final `-o` (`chiko` → `chika`, `on` → `ona`). Word pairs such as `papa`/`mama` and `brat`/`sister` stay as they are.

---

## 4. Pronouns & Possessives

Personal pronouns ([`personal_pronoun.md`](../pronoun/personal_pronoun.md)), object pronouns ([`object_pronoun.md`](../pronoun/object_pronoun.md)) and possessive determiners ([`possessive_pronoun.md`](../pronoun/possessive_pronoun.md)) are organized as follows:

| Person | Subject | Object | Possessive (Max 2 Variants) |
|--------|---------|--------|-----------------------------|
| **1st sg.** (I / me / my) | `je` | `me` | `mi` |
| **2nd sg./pl.** (you / your) | `ju` | `ju` | `tu` or `ju` |
| **3rd sg.** (he / him / his) | `on` | `on` | `su` or `on` |
| **3rd sg. fem.** (she / her) | `ona` | `ona` | `su` or `ona` |
| **3rd sg. neut.** (it / its) | `to` (or `it`) | `to` | `su` or `to` |
| **1st pl.** (we / us / our) | `we` | `nos` (or `we`) | `nos` or `we` |
| **3rd pl.** (they / them / their) | `oni` | `oni` | `oni` |
| **Reflexive** (-self) | — | `se` | — |

- **Object pronouns** have the same form as the subject pronouns, except for **`je` → `me`** (Romance *me/moi*, Slavic *mě/mnie/mene*, Germanic *mich/mij/mig/me*) and **`we` → `nos`** (Romance *nos/nous*, Slavic *nas/nás*).
  - `On vider me.` ("He sees me.")
  - `Ju help nos.` ("You help us.")
- **Gender**: `on` is the default third-person singular (*he*, or a person of unknown or unspecified gender). `ona` is the optional feminine form.
- **Reflexive `se`** is used for all persons (Romance *se/si*, Slavic *się/se/sa*, German *sich*, Dutch *zich*, Scandinavian *sig*):
  - `On laver se.` ("He washes himself.")
  - `Oni vider se.` ("They see themselves / each other.")
- **Possessives** always precede the noun (and any adjectives):
  - `mi dom` ("my house")
  - `tu novo libre` / `ju novo libre` ("your new book")
  - `su auto` / `on auto` ("his car")

---

## 5. Demonstratives & Quantifiers

Demonstratives and quantifiers are **invariant** and precede the noun, in the same position as articles ([`demonstrative.md`](../pronoun/demonstrative.md)):

| Uro | English | Example |
|-----|---------|---------|
| `dis` | this / these | `dis libre`, `dis libres` |
| `dat` | that / those | `dat dom` |
| `al` | all | `al ludi` ("everyone") |
| `som` | some | `som water` |
| `mult` | many / much / very | `mult libres`, `mult bon` |
| `poko` | few / little | `poko temp` |
| `nul` | no / none | `nul penge` |
| `kada` | every / each | `kada den` |
| `alter` | other | `de alter chiko` |

- Demonstratives and quantifiers can stand alone as pronouns: `Je voler dis.` ("I want this.")
- Combined with `ting` (thing) and `un` (one), they form indefinite pronouns: `somting` (something), `nulting` (nothing), `alting` (everything), `somun` (someone), `nulun` (nobody).

---

## 6. Adjectives, Adverbs & Comparison

### Adverbs (2 valid variants)
An adverb of manner is either the **bare adjective** (German/Dutch style) or the adjective + **`-li`**:
- `On parler rapid.` / `On parler rapidli.` ("He speaks quickly.")
- `Je slaper bon.` / `Je slaper bonli.` ("I sleep well.")

### Comparison
Comparison is **analytic only**. Uro does not use the Germanic `-er`/`-est` endings, which would clash with the verb ending `-er`.

| Degree | Uro | Example |
|--------|-----|---------|
| More … (than) | `mer` + Adj (+ `ke` …) | `Mi auto ar mer rapid ke tu auto.` |
| Most … | `de mest` + Adj | `de mest bel siti` |
| Less … (than) | `min` + Adj (+ `ke` …) | `Dis libre ar min dorog.` |
| Least … | `de minst` + Adj | `de minst difisil frag` |
| As … as | `so` + Adj + `komo` | `On ar so grand komo su brat.` |

- There are no irregular comparatives: `mer bon` ("better"), `de mest bon` ("the best").
- *Sources*: `mer`/`mest` (Dutch *meer/meest*, German *mehr/meist*, Scandinavian *mer/mest*, English *more/most*); `min`/`minst` (Romance *meno/moins/menos*, Slavic *mniej/méně/manje*, Dutch *minder/minst*, Swedish *mindre/minst*).

---

## 7. Verbs & Tenses

### Base / Present Tense
Verbs do **not** conjugate for person or number (`je vider`, `on vider`, `oni vider`).
Lexical verbs follow **2 valid morphological patterns**:
1. **Bare root form**: `hor` (hear), `go` (go), `appel` (call), `sit` (sit), `smil` (smile), `walk` (walk), `work` (work), `pluk` (pick), `listen` (listen).
2. **Unified `-er` suffix**: `vider` (see), `vender` (sell), `parler` (speak), `penser` (think), `skriber` (write), `speler` (play), `jester` (eat), `rirer` (laugh).

**Choosing the pattern for a new verb**: use the bare root when the shared root is a short Germanic/English verb (`bring`, `send`, `begin`, `help`). Otherwise use root + `-er` (`prober`, `responder`, `visiter`).

The verb root can also be used as a noun: `frager` → `frag` (question), `finer` → `fin` (end), `work` → `work`.

Irregular/Auxiliary verbs in the present tense are invariant:
- **To be**: `ar` ([`to_be.md`](../verbs/to_be.md)) — `je ar`, `ju ar`, `on ar`, `we ar`, `oni ar`.
- **To have**: `haf` ([`to_have.md`](../verbs/to_have.md)) — `je haf`, `ju haf`, `on haf`, `we haf`, `oni haf`.

### Past & Future Tenses (2 Valid Variants)
Both forms are valid in each tense:

| Tense | Variant 1 | Variant 2 | Examples ("I saw" / "I will see") |
|-------|-----------|-----------|-----------------------------------|
| **Present** | `Verb` | — | `je vider` / `je work` |
| **Past** | `haf + Verb` | `Verb-ed` | `je haf vider` or `je videred` (`je worked`) |
| **Future** | `wil + Verb` | `go + Verb` | `je wil vider` or `je go vider` |

- The future with `go` follows the European "going to" construction: French *je vais voir*, Spanish *voy a ver*, Dutch *ik ga zien*, English *I'm going to see*.
- The past of `ar` and `haf` follows the same rule: `je ared` / `je haf ar` ("I was"), `je hafed` / `je haf haf` ("I had").

### Modal Verbs & Verb Chains
A modal or other verb is followed directly by the **bare verb**. There is no infinitive marker like *to* or *zu*:
- `Je voler go.` ("I want to go.")
- `We mus work.` ("We must work.")
- `Ju kan parler Uro.` ("You can speak Uro.")
- `On treb help.` ("He needs help.")

The modal verbs are `kan` (can, may), `mus` (must), `dever` (should), `voler` (want) and `treb` (need).

**Causative**: `fakter` + object + bare verb ("make someone do something"), like French *faire rire* and Italian *fare ridere*:
- `De sol fakter de man open su mantel.` ("The sun makes the man open his coat.")

### Imperative
The imperative is the base form, with no subject:
- `Go!` ("Go!")
- `Skriber a me!` ("Write to me!")
- `Ne go!` ("Don't go!")

---

## 8. Negation

- **Rule**: Negation is formed exclusively by placing **`ne`** directly before the verb (or auxiliary particle).
  - *Present*: `Je ne vider de auto.` ("I do not see the car.")
  - *With `ar`*: `On ne ar in de dom.` ("He is not in the house.")
  - *Past/Future*: `We ne haf vider` / `We ne videred` ("We did not see") | `Ju ne wil go` / `Ju ne go go` ("You will not go").
- `ne` is also the answer "no" (see §9).

---

## 9. Questions

### Yes/No questions (2 valid forms)
1. **`SVO` + Question Mark (`?`)** (Intonation / Punctuation):
   - `Ju parler Uro?` ("Do you speak Uro?")
   - `On ar tu brat?` ("Is he your brother?")
2. **Verb–Subject Inversion (`VSO`)**:
   - `Parler ju Uro?` ("Do you speak Uro?")
   - `Ar on tu brat?` ("Is he your brother?")
   - `Haf ju vider mi libre?` ("Have you seen my book?")

The answer is **`ja`** (yes) or **`ne`** (no).

### Question words
A question word comes first. It is followed by `SVO` or by inversion (2 variants) ([`questions.md`](../basic/questions.md)):

| Uro | English | Example |
|-----|---------|---------|
| `ki` | who | `Ki ar dat?` ("Who is that?") |
| `ke` | what | `Ke ju voler?` ("What do you want?") |
| `wo` | where | `Wo ar de stasion?` ("Where is the station?") |
| `kando` | when | `Kando de tren kom?` / `Kando kom de tren?` |
| `komo` | how | `Komo ju ar?` ("How are you?") |
| `kuanto` | how much / many | `Kuanto to kost?` ("How much does it cost?") |
| `kual` | which | `Kual libre ju voler?` ("Which book do you want?") |
| `pro ke` | why | `Pro ke ju rirer?` ("Why are you laughing?") |

`pro ke` literally means "for what". It is built like Italian *perché*, Spanish *por qué*, Czech *proč* and French *pourquoi*.

---

## 10. Prepositions

Prepositions are **invariant** and always precede their noun phrase ([`prepositions.md`](../basic/prepositions.md)):

| Uro | English | Example |
|-----|---------|---------|
| `in` | in, into | `in de dom` |
| `fon` | of, from | `de dom fon mi papa` ("my father's house"); `Je kom fon Polska.` |
| `a` | to (direction, recipient) | `We go a Paris.`; `Je dar de libre a ju.` |
| `op` | on, onto | `de libre op de stol` |
| `mit` / `bez` | with / without | `kafe mit melk`, `kafe bez suker` |
| `pro` | for | `un libre pro ju` |
| `pre` / `post` | before / after | `pre de den`, `post de work` |
| `inter` | between | `inter de doms` |
| `kontra` | against | `kontra de wind` |
| `per` | through, by, per | `per de porta`, `per tren`, `ten euro per den` |
| `under` / `over` | under / over, above, about | `under de baum`; `un libre over Europa` |
| `til` | until, till | `til morgen` |
| `bi` | at, by, near | `bi de porta`, `bi mi mama` |
| `rund` | around | `rund de siti` |
| `eks` | out of | `eks de dom` |
| `za` | behind | `za de dom` |
| `durant` | during | `durant de nok` |

- **Possession** is expressed with `fon`: `de nom fon de chiko` ("the boy's name"). There is no `'s` ending.
- Uro never contracts a preposition with an article (no *du/del/zum*): `fon de`, `a de`, `in de`.

---

## 11. Conjunctions & Subordinate Clauses

([`conjunctions.md`](../basic/conjunctions.md))

| Uro | English | Example |
|-----|---------|---------|
| `i` | and | `papa i mama` |
| `o` | or | `kafe o te?` |
| `ma` | but | `Je voler go, ma je mus work.` |
| `if` | if | `If ju haf temp, we go a de museum.` |
| `ke` | that / which / who (relative) / than | see below |
| `pro ke` | because | `We rester in de dom, pro ke to ar kold.` |
| `kando` | when | `Kando je kom, we jester.` |
| `komo` | as, like | `On parler komo un enginir.` |

### The universal `ke`
A single subordinator, **`ke`**, introduces every kind of subordinate clause. It works like Romance *que/che/că* and Polish/Czech *że/že*:
- **That-clause**: `Je penser ke on ar hir.` ("I think that he is here.")
- **Relative clause**: `De man ke ju vider ar mi brat.` ("The man that you see is my brother.")
- **Comparison**: `On ar mer grand ke je.` ("He is taller than me.")

Indirect questions use the question word directly: `Je ne znar wo on ar.` ("I don't know where he is.")

---

## 12. Numbers

([`numbers.md`](../numbers/numbers.md))

- **Units**: `un du tri fir fif siks set okt nin ten`.
- **Teens**: unit + `ten`: `unten` (11), `duten` (12) … `ninten` (19).
- **Tens**: unit + `-ti` (like English *-ty*): `triti` (30), `firti` (40) … `ninti` (90). The exception is `vinti` (20).
- **Larger numbers** are written big to small, units last (no German/Dutch reversal): `vinti un` (21), `sent triti du` (132), `mil nin sent ninti nin` (1999).
- `sent` (100), `mil` (1000), `milion` (10⁶), `miliard` (10⁹). Uro uses `miliard` to avoid the *billion* ambiguity.
- **Ordinals**: `prim` (first) and `sekund` (second) are irregular, as in nearly every European language. All others take **`-de`**: `tride`, `firde`, `fifde`, `tende`. Uro does not use `-te`, which would sound almost the same as the tens (`fifti` vs *fifte*).

---

## 13. Word Formation

New words are derived with a small set of internationally recognizable affixes, such as `-ist`, `-or`, `-sion`, `-iti`, `-ism`, `-logi`, `-al`, `-ik`, `-iv`, `non-` and `re-`, and with transparent compounds (`dis den` "today", `fon novo` "again"). Agent nouns **never** use `-er`, because that is the verb ending. See [`word_formation.md`](word_formation.md).

---

## 14. Reserved Function Words

Short function words are reserved. A new content word must not take any of these forms:

| Category | Reserved forms |
|----------|----------------|
| Articles | `un`, `de` |
| Pronouns | `je`, `me`, `ju`, `on`, `ona`, `to`, `it`, `we`, `nos`, `oni`, `se` |
| Possessives | `mi`, `tu`, `su` |
| Demonstratives & quantifiers | `dis`, `dat`, `al`, `som`, `mult`, `poko`, `nul`, `kada`, `alter` |
| Degree | `mer`, `mest`, `min`, `minst`, `so` |
| Verbs & auxiliaries | `ar`, `haf`, `wil`, `go`, `kan`, `mus`, `dever`, `treb` |
| Negation & answers | `ne`, `ja` |
| Prepositions | `in`, `fon`, `a`, `op`, `mit`, `bez`, `pro`, `pre`, `post`, `inter`, `kontra`, `per`, `under`, `over`, `til`, `bi`, `rund`, `eks`, `za`, `durant` |
| Conjunctions | `i`, `o`, `ma`, `if`, `ke`, `kando`, `komo` |
| Question words | `ki`, `wo`, `kuanto`, `kual` |

---

## 15. Formal Grammar Summary (EBNF-Style for Parser Design)

```ebnf
Sentence       ::= Declarative "." | Question "?" | Imperative "!"
Declarative    ::= (Adv)? Clause (Conj Clause)*
Clause         ::= NP VP
Question       ::= Clause
                 | Verb NP (Complement)*
                 | QWord (Clause | VP | Verb NP (Complement)*)
Imperative     ::= ("ne")? VerbChain (Complement)*

NP             ::= Pronoun
                 | (Determiner)? (Quantifier)? (AdjP)* Noun (PP)* (RelClause)?
Determiner     ::= "un" | "de" | Possessive | Demonstrative
Demonstrative  ::= "dis" | "dat"
Quantifier     ::= "al" | "som" | "mult" | "poko" | "nul" | "kada" | "alter" | Number
Possessive     ::= "mi" | "tu" | "ju" | "su" | "on" | "ona" | "to" | "we" | "nos" | "oni"
Pronoun        ::= "je" | "me" | "ju" | "on" | "ona" | "to" | "it" | "we" | "nos" | "oni" | "se"
AdjP           ::= (Degree)? Adj
Degree         ::= "mer" | "mest" | "min" | "minst" | "mult" | "so"
PP             ::= Prep NP
Prep           ::= "in" | "fon" | "a" | "op" | "mit" | "bez" | "pro" | "pre" | "post"
                 | "inter" | "kontra" | "per" | "under" | "over" | "til" | "bi"
                 | "rund" | "eks" | "za" | "durant"
RelClause      ::= "ke" (NP)? VP

VP             ::= ("ne")? (Aux)? VerbChain (Complement)*
Aux            ::= "haf" | "wil" | "go"
VerbChain      ::= Verb (Verb)*
Verb           ::= BaseVerb | BaseVerb "ed"
Complement     ::= NP | AdjP | PP | Adv | ThatClause | Comparison | Causative
Causative      ::= NP VerbChain (Complement)*
ThatClause     ::= "ke" Clause
Comparison     ::= "ke" NP | "komo" NP
Adv            ::= Adj | Adj "li" | TimeAdv | PlaceAdv

Conj           ::= "i" | "o" | "ma" | "if" | "pro ke" | "kando"
QWord          ::= "ki" | "ke" | "wo" | "kando" | "komo" | "kuanto" | "kual" | "pro ke"
```
