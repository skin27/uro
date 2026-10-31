# Uro Grammar Specification

Uro is designed with an analytical, rule-based structure inspired by European language families (Germanic, Romance, and Slavic) while remaining simple enough to be parsed and validated like a programming language.

Where natural European languages diverge, Uro allows **at most two valid variants** for a grammatical construction.

For plurals, the past, the future, adverbs, possessives, questions and negative words, the first form listed is the **default**: the one used in courses, vocabulary tables and texts. The second form stays correct and is understood.

Version: **0.4.0** (see [`changelog.md`](changelog.md)). Pronunciation and spelling: [`pronunciation.md`](pronunciation.md). Word formation: [`word_formation.md`](word_formation.md).

---

## 1. Word Order (Syntax)

- **Sentence Structure (`SVO`)**: Declarative sentences strictly follow **Subject – Verb – Object** order.
  - *Example*: `Je vider de dom.` ("I see the house.")
  - *Example*: `On haf un auto.` ("He has a car.")
- **Adjective Placement**: Adjectives always precede the noun (**`Adjective + Noun`**, Germanic/Slavic style) and are **invariant** (they do not change for gender, case, or plural).
  - *Example*: `un novo dom` ("a new house")
  - *Example*: `de bon libres` ("the good books")
- **Subordinate clauses keep `SVO`**. The verb never moves to the end (unlike German or Dutch).
  - *Example*: `Je kenner dat on ar in de dom.` ("I know that he is in the house.")
- **Adverbs**: Manner adverbs follow the verb (or its object). Time and place adverbs go at the start or the end of the sentence.
  - *Example*: `On parler rapidli.` ("He speaks fast.")
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
- **Pluralization (2 valid variants)**: The default plural adds **`-s`** (Western: Romance/Germanic) to the singular noun. The variant adds **`-i`** (Slavic/Italian/Romanian); it can't be used on nouns that already end in `-i`, and it can make two nouns look the same (`taksa` → `taksi`), so `-s` is the safe choice:

| Noun ends in | Default | Variant | Examples |
|--------------|-----------|-----------|----------|
| a consonant | `-s` | `-i` | `dom` → `doms` / `domi`; `brat` → `brats` / `brati` |
| `-s`, `-ks`, `-z`, `-sh`, `-ch` | `-es` | `-i` | `bus` → `buses` / `busi` |
| `-a`, `-e`, `-o`, `-u` | `-s` | `-i` replaces the vowel | `chiko` → `chikos` / `chiki`; `libre` → `libres` / `libri`; `ninio` → `ninios` / `ninii` |
| `-i` | `-s` | — | `ziti` → `zitis`; `famili` → `familis`; `taksi` → `taksis` |

- **Gender**: Nouns are gender-neutral by default. Where a female form is wanted, the optional suffix **`-a`** marks it, usually replacing a final `-o` (`chiko` → `chika`, `on` → `ona`). Word pairs such as `papa`/`mama` and `brat`/`sister` stay as they are.

---

## 4. Pronouns & Possessives

Personal pronouns ([`personal_pronoun.md`](../pronoun/personal_pronoun.md)), object pronouns ([`object_pronoun.md`](../pronoun/object_pronoun.md)) and possessive determiners ([`possessive_pronoun.md`](../pronoun/possessive_pronoun.md)) are organized as follows:

| Person | Subject | Object | Possessive (default first) |
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
| `mult` | many / much | `mult libres` |
| `poko` | few / little | `poko temp` |
| `nul` | no / none | `nul monni` |
| `kada` | every / each | `kada den` |
| `alter` | other | `de alter chiko` |
| `ambo` | both | `ambo brats` |
| `vari` | several | `vari libres` |

- Demonstratives and quantifiers can stand alone as pronouns: `Je voler dis.` ("I want this.")
- Combined with `ting` (thing) and `un` (one), they form indefinite pronouns: `somting` (something), `nulting` (nothing), `alting` (everything), `somun` (someone), `nulun` (nobody).
- **Any**: Uro has no separate *any* words. Like Scandinavian *nogen/någon* and Czech *nějaký*, it uses:
  - `som` in questions and `if` clauses: `Ju haf som kwestias?` ("Do you have any questions?"), `If somun kom, …` ("If anyone comes, …").
  - `nul` with negation: `Je haf nul monni.` ("I don't have any money.")
  - `kada` for "any you like": `Ju kan kom kada den.` ("You can come any day.")
- **Other and else**: `un alter` (another, like French *un autre*); `alter` after a pronoun means *else*: `somun alter` (someone else), `ke alter?` (what else?).
- **Whatever**: `al ke` ("all that"), like French *tout ce que*, German *alles, was* and Polish *wszystko, co*: `Ju kan nemer al ke ju voler.` ("You can take whatever you want.")
- **Same, such, own** are ordinary adjectives and go before the noun: `de idem dom` (the same house), `un tal kwestia` (such a question), `mi propri auto` (my own car).

---

## 6. Adjectives, Adverbs & Comparison

### Adverbs (2 valid variants)
An adverb of manner is by default the adjective + **`-li`**. The variant is the **bare adjective** (German/Dutch style):
- `On parler rapidli.` / `On parler rapid.` ("He speaks quickly.")
- `Je slaper bonli.` / `Je slaper bon.` ("I sleep well.")
- Every English adverb in *-ly* follows this rule, so it needs no word of its own: `klar` → `klarli` / `klar` (clearly), `normal` → `normalli` (usually), `posibel` → `posibelli` (possibly).
- Comparison works on adverbs too: `plus tard` (later), like French *plus tard* and Spanish *más tarde*.

### Comparison
Comparison is **analytic only**. Uro does not use the Germanic `-er`/`-est` endings, which would clash with the verb ending `-er`.

| Degree | Uro | Example |
|--------|-----|---------|
| More … (than) | `plus` + Adj (+ `niz` …) | `Mi auto ar plus rapid niz tu auto.` |
| Most … | `de plus` + Adj | `de plus bel ziti` |
| Less … (than) | `min` + Adj (+ `niz` …) | `Dis libre ar min dorog.` |
| Least … | `de minst` + Adj | `de minst difizil kwestia` |
| As … as | `so` + Adj + `jak` | `On ar so grand jak su brat.` |

- There are no irregular comparatives: `plus bon` ("better"), `de plus bon` ("the best").

### Degree words
Degree words go before an adjective or adverb:

| Uro | English | Example |
|-----|---------|---------|
| `multi` | very | `multi bon` (also *a lot*) |
| `zu` | too | `zu dorog` ("too expensive", German *zu*) |
| `genug` | quite, rather | `genug bon` ("quite good"), like French *assez*, Italian *abbastanza*, Polish *dość* |
| `skoro` | almost, nearly | `skoro plen` ("almost full") |
| `mem` | even | `mem on` ("even he") |
- *Sources*: `plus` / `de plus` (French *plus / le plus*, Italian *più / il più*, Latin *plus*; known everywhere from maths); `min`/`minst` (Romance *meno/moins/menos*, Slavic *mniej/méně/manje*, Dutch *minder/minst*, Swedish *mindre/minst*).

---

## 7. Verbs & Tenses

### Base / Present Tense
Verbs do **not** conjugate for person or number (`je vider`, `on vider`, `oni vider`).
Lexical verbs follow **2 valid morphological patterns**:
1. **Bare root form**: `hor` (hear), `go` (go), `appel` (call), `sit` (sit), `smil` (smile), `walk` (walk), `work` (work), `pluk` (pick), `listen` (listen).
2. **Unified `-er` suffix**: `vider` (see), `vender` (sell), `parler` (speak), `penser` (think), `skriber` (write), `speler` (play), `jester` (eat), `rirer` (laugh).

**Choosing the pattern for a new verb**: use the bare root when the shared root is a short Germanic/English verb (`bring`, `send`, `begin`, `help`). Otherwise use root + `-er` (`prober`, `responder`, `visiter`). Verbs from Latin roots follow the rule in [`word_formation.md`](word_formation.md) §5 (`akzepter`, `dezider`, `ekspliker`).

The verb root can also be used as a noun: `finer` → `fin` (end), `work` → `work`.

Irregular/Auxiliary verbs in the present tense are invariant:
- **To be**: `ar` ([`to_be.md`](../verbs/to_be.md)) — `je ar`, `ju ar`, `on ar`, `we ar`, `oni ar`.
- **To have**: `haf` ([`to_have.md`](../verbs/to_have.md)) — `je haf`, `ju haf`, `on haf`, `we haf`, `oni haf`.

### Past & Future Tenses (2 Valid Variants)
Both forms are valid in each tense. The first is the default:

| Tense | Default | Variant | Examples ("I saw" / "I will see") |
|-------|-----------|-----------|-----------------------------------|
| **Present** | `Verb` | — | `je vider` / `je work` |
| **Past** | `haf + Verb` | `Verb-ed` | `je haf vider` or `je videred` (`je worked`) |
| **Future** | `wil + Verb` | `go + Verb` | `je wil vider` or `je go vider` |

- The future with `go` follows the European "going to" construction: French *je vais voir*, Spanish *voy a ver*, Dutch *ik ga zien*, English *I'm going to see*.
- `ar`, `haf` and `kan` are the exception: their default past is `-ed`, because `je haf haf` reads badly. `je ared` / `je haf ar` ("I was"), `je hafed` / `je haf haf` ("I had"), `je kaned` / `je haf kan` ("I could").

### Conditional
The conditional is **`wud` + bare verb**, built like the future with `wil` (English *would*, German *würde*, Dutch *zou*, Swedish *skulle*, and the Slavic particle *by*):

| English | Uro |
|---------|-----|
| I would go | `je wud go` |
| I would have gone | `je wud haf go` |
| I could go / I might go | `je wud kan go` |

- An `if` clause takes the present for a real condition and the past for an unreal one. Only the main clause takes `wud`:
  - `If ju kom, we go a de museum.` ("If you come, we will go to the museum.")
  - `If je hafed monni, je wud kuper un auto.` ("If I had money, I would buy a car.")
- `wud` also makes a request polite: `Je wud voler un kafe.` ("I would like a coffee.")
- `could` in the sense of past ability is the past of `kan`: `je kaned` / `je haf kan` ("I could, I was able to").

### Modal Verbs & Verb Chains
A modal or other verb is followed directly by the **bare verb**. There is no infinitive marker like *to* or *zu*:
- `Je voler go.` ("I want to go.")
- `We mus work.` ("We must work.")
- `Ju kan parler Uro.` ("You can speak Uro.")
- `On treb help.` ("He needs help.")

The modal verbs are `kan` (can, may), `mus` (must), `dever` (should), `voler` (want) and `treb` (need).

**Causative**: `fakter` + object + bare verb ("make someone do something"), like French *faire rire* and Italian *fare ridere*:
- `De sol fakter de man open su mantel.` ("The sun makes the man open his coat.")

**Permission**: `las` + object + bare verb ("let someone do something"), from the root shared by German *lassen*, Dutch *laten*, Swedish *låta*, French *laisser*, Italian *lasciare* and Romanian *a lăsa*:
- `Las me help ju.` ("Let me help you.")
- `Las nos go!` ("Let's go!")

### Imperative
The imperative is the base form, with no subject:
- `Go!` ("Go!")
- `Skriber a me!` ("Write to me!")
- `Ne go!` ("Don't go!")

---

## 8. Negation

- **Rule**: Negation is formed exclusively by placing **`not`** directly before the verb (or auxiliary particle).
  - *Present*: `Je not vider de auto.` ("I do not see the car.")
  - *With `ar`*: `On not ar in de dom.` ("He is not in the house.")
  - *Past/Future*: `We not haf vider` / `We not videred` ("We did not see") | `Ju not wil go` / `Ju not go go` ("You will not go").
- The answer *no* is `no` (see §9).
- **Negative words** (`nul`, `nulting`, `nulun`, `nikdi`) are negative by themselves. By default they replace `not`, Germanic style: `Je vider nulting.` The variant keeps `not`, Romance/Slavic style: `Je not vider nulting.` ("I don't see anything.") Two negatives never cancel each other out.
- **Neither … nor** is `not … not`, which replaces the `not` before the verb: `Je drink not kafe not te.` ("I drink neither coffee nor tea.")

---

## 9. Questions

### Yes/No questions (2 valid forms)
1. **`SVO` + Question Mark (`?`)** (Intonation / Punctuation), the default for yes/no questions:
   - `Ju parler Uro?` ("Do you speak Uro?")
   - `On ar tu brat?` ("Is he your brother?")
2. **Verb–Subject Inversion (`VSO`)**:
   - `Parler ju Uro?` ("Do you speak Uro?")
   - `Ar on tu brat?` ("Is he your brother?")
   - `Haf ju vider mi libre?` ("Have you seen my book?")

The answer is **`ja`** (yes) or **`no`** (no).

### Question words
A question word comes first. By default it is followed by inversion (Verb–Subject), and the variant is `SVO` (2 variants). If the question word is the object of the verb, the default is `SVO`, because inversion would change the meaning: `Ki ju vider?` ("Whom do you see?") against `Ki vider ju?` ("Who sees you?") ([`questions.md`](../basic/questions.md)):

| Uro | English | Example |
|-----|---------|---------|
| `ki` | who | `Ki ar dat?` ("Who is that?") |
| `ke` | what | `Ke ju voler?` ("What do you want?") |
| `wo` | where | `Wo ar de stazion?` ("Where is the station?") |
| `kando` | when | `Kando kom de tren?` / `Kando de tren kom?` |
| `komo` | how | `Komo ar ju?` ("How are you?") |
| `kuanto` | how much / many | `Kuanto kost to?` ("How much does it cost?") |
| `kual` | which | `Kual libre ju voler?` ("Which book do you want?") |
| `pro ke` | why | `Pro ke rirer ju?` ("Why are you laughing?") |

`pro ke` literally means "for what". It is built like Italian *perché*, Spanish *por qué*, Czech *proč* and French *pourquoi*.

`ki` is also the object form (*whom*), because Uro word order already shows the object: `Ki ju vider?` ("Whom do you see?"). Possession uses `fon`, as with nouns: `Fon ki ar dis libre?` ("Whose book is this?")

---

## 10. Prepositions

Prepositions are **invariant** and always precede their noun phrase ([`prepositions.md`](../basic/prepositions.md)):

| Uro | English | Example |
|-----|---------|---------|
| `in` | in, into | `in de dom` |
| `fon` | of | `de dom fon mi papa` ("my father's house") |
| `od` | from | `Je kom od Polska.` (Slavic *od*, *ot*) |
| `a` | to (direction, recipient) | `We go a Paris.`; `Je dar de libre a ju.` |
| `op` | on, onto | `de libre op de tabel` |
| `mit` / `bez` | with / without | `kafe mit melk`, `kafe bez suker` |
| `pro` | for | `un libre pro ju` |
| `pre` / `post` | before / after | `pre de den`, `post de work` |
| `inter` | between | `inter de doms` |
| `kontra` | against | `kontra de wind` |
| `per` | through, by, per | `per de porta`, `per tren`, `ten euro per den` |
| `under` / `over` | under / over, above, about | `under de baum`; `un libre over Europa` |
| `til` | until, till | `til morgen` |
| `bi` | at, by, near | `bi de porta`, `bi mi mama` |
| `rund` | around | `rund de ziti` |
| `eks` | out of | `eks de dom` |
| `za` | behind | `za de dom` |
| `durant` | during | `durant de noht` |
| `trans` | across, beyond | `trans de strada`, `trans de monts` |
| `langs` | along | `langs de reka` (like Dutch and Danish *langs*) |
| `vers` | toward | `vers de stazion` |
| `trots` | despite | `trots de regen` (German *trotz*, Swedish *trots*) |
| `segun` | according to | `segun de doktor` |
| `inklusiv` | including | `ten euro, inklusiv de te` |
| `in plaza fon` | instead of | `te in plaza fon kafe` |

- **Possession** is expressed with `fon`: `de nom fon de chiko` ("the boy's name"). There is no `'s` ending.
- Uro never contracts a preposition with an article (no *du/del/zum*): `fon de`, `a de`, `in de`.
- `in` and `eks` also mean *inside* and *outside*; `inter` also means *among*.
- **Ago** is `pre` + a time: `pre tri ano` ("three years ago"), like German *vor drei Jahren*, Czech *před třemi lety* and Serbian *pre tri godine*.
- **Direction adverbs**: `op` (up) and `ab` (down, off) are used without a noun, like German *auf und ab* and Dutch *op en af*: `On go op i ab.` ("He walks up and down."), `Nemer ab tu mantel.` ("Take off your coat.") Other direction adverbs are `weg` (away), `retur` (back) and `avant` (ahead, forward); see [`adverbs.md`](../basic/adverbs.md).

---

## 11. Conjunctions & Subordinate Clauses

([`conjunctions.md`](../basic/conjunctions.md))

| Uro | English | Example |
|-----|---------|---------|
| `i` | and | `papa i mama` |
| `o` | or | `kafe o te?` |
| `ale` | but | `Je voler go, ale je mus work.` |
| `if` | if | `If ju haf temp, we go a de museum.` |
| `dat` | that | `Je penser dat on ar hir.` (Dutch *dat*, German *dass*) |
| `ke` | which / who (relative) | see below |
| `niz` | than | `On ar plus grand niz je.` (Polish *niż*, Czech *než*) |
| `pro ke` | because | `We rester in de dom, pro ke to ar kold.` |
| `kando` | when | `Kando je kom, we jester.` |
| `jak` | as, like | `On parler jak un enginir.` |
| `mem if` | although, even if | `We go, mem if to ar kold.` |
| `durant ke` | while | `Je lezer durant ke ju work.` |
| `od kando` | since (time) | `Od kando je ar hir, …` |
| `if` | whether | `Je not kenner if on kom.` |
| `o … o` | either … or | `o kafe o te` |
| `not … not` | neither … nor | `not kafe not te` |
| `ambo … i` | both … and | `ambo papa i mama` |
| `pro dis` | therefore, thus | `To ar kold, pro dis we rester in de dom.` |

- Like `pro ke`, the compound conjunctions are built from a preposition or adverb + a conjunction, as in French *pendant que* (`durant ke`), Italian *da quando*, Polish *od kiedy* (`od kando`) and Danish *selv om* (`mem if`).
- *However* at the start of a sentence is `ale` (but).

### Subordinate clauses: `dat`, `ke`, `niz`
Three short words introduce subordinate clauses:
- **That-clause**: `dat`, like Dutch *dat* and German *dass*: `Je penser dat on ar hir.` ("I think that he is here.") `dat` is also the demonstrative *that*, as in Dutch and English.
- **Relative clause**: `ke`, like Romance *que/che*: `De man ke ju vider ar mi brat.` ("The man that you see is my brother.") `ke` also stays in the compounds `pro ke` (because), `durant ke` (while) and `al ke` (whatever).
- **Comparison**: `niz`, like Polish *niż* and Czech *než*: `On ar plus grand niz je.` ("He is taller than me.")

Indirect questions use the question word directly: `Je not kenner wo on ar.` ("I don't know where he is.")

---

## 12. Numbers

([`numbers.md`](../numbers/numbers.md))

- **Units**: `un du tri fir fif siks set okt nin ten`.
- **Teens**: unit + `ten`: `unten` (11), `duten` (12) … `ninten` (19).
- **Tens**: unit + `-ti` (like English *-ty*): `triti` (30), `firti` (40) … `ninti` (90). The exception is `vinti` (20).
- **Larger numbers** are written big to small, units last (no German/Dutch reversal): `vinti un` (21), `zent triti du` (132), `mil nin zent ninti nin` (1999).
- `zent` (100), `mil` (1000), `milion` (10⁶), `miliard` (10⁹). Uro uses `miliard` to avoid the *billion* ambiguity.
- **Ordinals**: `prim` (first) and `sekund` (second) are irregular, as in nearly every European language. All others take **`-de`**: `tride`, `firde`, `fifde`, `tende`. Uro does not use `-te`, which would sound almost the same as the tens (`fifti` vs *fifte*).

---

## 13. Word Formation

New words are derived with a small set of internationally recognizable affixes, such as `-ist`, `-or`, `-zion`, `-iti`, `-ism`, `-logi`, `-al`, `-ik`, `-iv`, `non-` and `re-`, and with transparent compounds (`dis den` "today", `fon novo` "again"). Agent nouns **never** use `-er`, because that is the verb ending. See [`word_formation.md`](word_formation.md).

---

## 14. Reserved Function Words

Short function words are reserved. A new content word must not take any of these forms:

| Category | Reserved forms |
|----------|----------------|
| Articles | `un`, `de` |
| Pronouns | `je`, `me`, `ju`, `on`, `ona`, `to`, `it`, `we`, `nos`, `oni`, `se` |
| Possessives | `mi`, `tu`, `su` |
| Demonstratives & quantifiers | `dis`, `dat`, `al`, `som`, `mult`, `poko`, `nul`, `kada`, `alter`, `ambo`, `vari` |
| Determiner-like adjectives | `idem`, `tal`, `propri` |
| Degree | `plus`, `min`, `minst`, `multi`, `so`, `zu`, `skoro`, `mem` |
| Verbs & auxiliaries | `ar`, `haf`, `wil`, `go`, `kan`, `mus`, `dever`, `treb`, `wud`, `las` |
| Negation & answers | `not`, `no`, `ja` |
| Prepositions | `in`, `fon`, `od`, `a`, `op`, `mit`, `bez`, `pro`, `pre`, `post`, `inter`, `kontra`, `per`, `under`, `over`, `til`, `bi`, `rund`, `eks`, `za`, `durant`, `trans`, `langs`, `vers`, `trots`, `segun`, `inklusiv` |
| Direction adverbs | `ab` (and `op`, above) |
| Conjunctions | `i`, `o`, `ale`, `if`, `dat`, `ke`, `niz`, `kando`, `jak` |
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
Imperative     ::= ("not")? VerbChain (Complement)*

NP             ::= Pronoun
                 | (Determiner)? (Quantifier)? (AdjP)* Noun (PP)* (RelClause)?
Determiner     ::= "un" | "de" | Possessive | Demonstrative
Demonstrative  ::= "dis" | "dat"
Quantifier     ::= "al" | "som" | "mult" | "poko" | "nul" | "kada" | "alter" | "ambo" | "vari" | Number
Possessive     ::= "mi" | "tu" | "ju" | "su" | "on" | "ona" | "to" | "we" | "nos" | "oni"
Pronoun        ::= "je" | "me" | "ju" | "on" | "ona" | "to" | "it" | "we" | "nos" | "oni" | "se"
AdjP           ::= (Degree)? Adj
Degree         ::= "plus" | "min" | "minst" | "multi" | "so" | "zu" | "genug" | "skoro" | "mem"
PP             ::= Prep NP
Prep           ::= "in" | "fon" | "od" | "a" | "op" | "mit" | "bez" | "pro" | "pre" | "post"
                 | "inter" | "kontra" | "per" | "under" | "over" | "til" | "bi"
                 | "rund" | "eks" | "za" | "durant" | "trans" | "langs" | "vers"
                 | "trots" | "segun" | "inklusiv" | "in plaza fon"
RelClause      ::= "ke" (NP)? VP

VP             ::= ("not")? (Aux)? VerbChain (Complement)*
Aux            ::= "haf" | "wil" | "go" | "wud"
VerbChain      ::= Verb (Verb)*
Verb           ::= BaseVerb | BaseVerb "ed"
Complement     ::= NP | AdjP | PP | Adv | ThatClause | Comparison | Causative
Causative      ::= NP VerbChain (Complement)*
ThatClause     ::= "dat" Clause
Comparison     ::= "niz" NP | "jak" NP
Adv            ::= Adj | Adj "li" | TimeAdv | PlaceAdv | DirAdv
DirAdv         ::= "op" | "ab" | "weg" | "retur" | "avant"

Conj           ::= "i" | "o" | "ale" | "if" | "pro ke" | "kando" | "pro dis"
                 | "mem if" | "durant ke" | "od kando"
QWord          ::= "ki" | "ke" | "wo" | "kando" | "komo" | "kuanto" | "kual" | "pro ke"
```
