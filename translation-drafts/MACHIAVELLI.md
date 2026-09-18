# Machiavelli — linguistic and voice profile for translation evaluation

**Status:** G2 evaluation profile; proposed under WI-000117

**Governing philosophy:** `translation-system/TRANSLATION-PHILOSOPHY-v0.9.md`

**Fixed source sample:** `NM-PRIN.15`; `NM-DISC.1.12`

**Stopping rule:** this profile identifies risks and testable features. It
creates no English rendering, term decision, source change, author-wide
statistical claim, or protocol rule.

## 1. Evidence boundary

The direct corpus evidence is deliberately narrow: one chapter of *Il
Principe* and one chapter of the *Discorsi*. Both are accepted S2 evaluation
inputs in the G1 readiness packet. Observations labelled **sample-observed**
refer only to those passages. Broader claims require the cited
historical-linguistic scholarship; anything not supported by either source is
marked **unknown**.

The boundary matters unusually strongly for Machiavelli. Giovanna Frosini
emphasises the variety of his works, forms, constructions, and vocabulary and
warns that the lack of a complete reliable autograph-based edition makes
corpus-wide quantification unreliable. The *Principe* and most of the
*Discorsi* also lack surviving autographs. [MACH-LINGUA] Giuseppe Patota likewise
shows that argumentative schemas change with communicative function and genre:
personal political argument, impersonal report, persuasion, history, and
dialogue cannot be assigned one undifferentiated “Machiavellian voice.”
[MACH-STILE]

Accordingly, this profile supplies hypotheses for G3 sampling. It is not a
style template to impose on the whole corpus.

## 2. Syntax and period profile

### 2.1 Relations before sentence shape

Both fixed passages build arguments through repeated causal, consequential,
conditional, and concessive relations. The translation risk is not simply
long sentences; it is losing the hierarchy and attachment of those relations.

In `NM-PRIN.15.01`, the movement from declared usefulness to `verità
effettuale`, from the distance between conduct and prescription to ruin, and
from that ruin to the prince's practical necessity is carried by a chain of
`ma`, `perché`, `che`, `onde`, and the construction `volendosi mantenere`.
In `NM-PRIN.15.02`, the catalogue of paired qualities is followed by
limitations introduced through `ma perché`, `se egli è possibile`, `ma non
potendo`, and the final apparent `virtù`/`vizio` reversal. These are
sample-observed relations, not detachable maxims. [NM-PRIN.15.01–02]

`NM-DISC.1.12` repeatedly moves from a general proposition to grounds,
examples, and political consequences through `perché`, `adunque`, `e fatto
questo`, `per conseguente`, `di qui`, `come`, and `né`. The last three
paragraphs form one accumulating explanation of the Church's role: moral
example, territorial power, external intervention, division, and exposure to
attack. Sentence division must not make these claims independent of their
stated grounds. [NM-DISC.1.12.01–07]

Patota identifies the broader Machiavellian “vocabulary of necessity” and
conclusive connectors as structural links between example and political
demonstration, while stressing the binary and branching organisation of much
political argument. [MACH-STILE] G3 should therefore tag relations and
argument steps before testing English sentence division.

### 2.2 Evaluation features

For every sampled complex period, record:

- the main assertion and every subordinate ground or limitation;
- the scope of negation, condition, modality, and exception;
- the referent of explicit and implied subjects;
- whether a sequence is binary, enumerative, branching, or cumulative;
- where example becomes inference and inference becomes recommendation;
- whether a connector is logical, temporal, resumptive, or rhetorical; and
- what argumentative movement would be lost by splitting the period.

Do not reward sentence-count identity. Do not reward shorter English if the
result detaches a conclusion from its condition or turns an apparent quality
into an endorsed one.

### 2.3 Direct sample hypotheses

| Feature | Fixed-passage evidence | Evaluation risk |
|---|---|---|
| causal chaining | repeated `perché` in both units | flattened hierarchy; every clause presented as an equal reason |
| necessity/modality | `debbano`, `conviene`, `è necessario`, `si può`, `debbono`, `bisognerebbe` | obligation, possibility, and inference collapsed into one assertive register |
| paired alternatives | qualities in `NM-PRIN.15.02`; Church powerful/not powerful in `NM-DISC.1.12.06–07` | elegant parallelism replacing asymmetric consequences |
| accumulation | `di qui` sequence and final Church argument | repetition removed as redundant; causal build weakened |
| embedded qualification | `se egli è possibile`, `ma non potendo`, `per avventura` | conditional or evidentiary restraint dropped |
| argumentative return | apparent good/bad qualities reconsidered by consequence | maxim extracted before its reversal or limit |

## 3. Voice and rhetorical movement

### 3.1 Authorial presence

The fixed chapters do not support an impersonal “realist” voice. Machiavelli
marks acts of writing, doubt, intention, knowledge, judgment, and argumentative
transition: `io so`, `dubito`, `l'intento mio`, `mi è parso`, `dico`, `secondo
me`, and `voglio ... discorrere`. These forms locate responsibility and degree
of commitment. Omitting them can convert an argued position into anonymous
doctrine. [NM-PRIN.15.01–02; NM-DISC.1.12.05]

### 3.2 Movement rather than slogan

The sample voice often proceeds through a sequence:

1. state the question or received view;
2. distinguish terms, alternatives, or cases;
3. introduce an example or practical condition;
4. draw a conclusion using necessity or consequence; and
5. qualify, reverse, or intensify the apparent starting point.

Patota's broader analysis supports binary, branching, enumerative, and
objection-and-reply structures in the political prose, but also distinguishes
them from impersonal reports and from the more elevated, rhetorically managed
historical works. [MACH-STILE] The translation should preserve local movement,
not manufacture a house style of permanently clipped aphorisms.

### 3.3 Rhetorical hazards

- **Maxim extraction:** a memorable clause may be subordinate to the case that
  follows or precedes it.
- **False certainty:** present-tense generalisation does not erase a stated
  condition, example base, or authorial judgment marker.
- **Symmetry inflation:** binary syntax may lead English to make both members
  more balanced than their consequences are.
- **Ornamental upgrading:** direct or everyday political vocabulary should not
  be converted into abstract academic terminology merely because the argument
  is consequential.
- **Voice homogenisation:** treatise, republican discourse, report, history,
  drama, and correspondence require separate evidence.

## 4. Institutional and diplomatic features

Machiavelli's political language draws on contemporary Florentine use and his
experience in a chancery responsible for public documentation and government
communications. Frosini describes the transfer of daily language into
chancery codification; Patota notes that much political vocabulary is weakly
technicised and can make precise claims using apparently general words.
[MACH-LINGUA; MACH-STILE] The Florentine chancery itself was an apparatus of
professional writing, law, rhetoric, and documentary government, not a modern
civil service with one stable hierarchy. [MACH-CANCELLERIA]

The fixed sample requires at least the following distinctions to remain
inspectable:

- `principe`, `repubblica`, `regno`, `Stato`, `provincia`, `imperio`, and
  `dominio` name different agents, forms, territories, or relations;
- `Chiesa romana`, `Corte`, `Preti`, and `Religione` are not interchangeable;
- `popoli`, `sudditi`, `amici`, `uomini`, and `principi` must not acquire
  automatic modern democratic or sociological senses;
- `ordini` may concern arrangements, institutions, established modes, or
  ordering practices and requires local analysis; and
- institutional agency must not be reassigned to Machiavelli merely because
  he drafted or reported an official text.

For diplomatic and administrative genres not represented in the fixed sample,
record sender, institutional voice, recipient, office, document function,
reported speech, and Machiavelli's production role before translating first
person or collective agency. The correct translation treatment is **unknown**
until the genre profiles and representative samples are fixed.

## 5. False-friend and semantic-risk inventory

This is a watchlist, not a glossary. It proposes no default English rendering.

| Source form or cluster | Evidence/status | Risk to test |
|---|---|---|
| `virtù`, `vizio`, `buono`, `non buono` | directly load-bearing in `NM-PRIN.15`; scholarship describes `virtù` as plural and flexible rather than univocal [MACH-VIRTU] | automatic moral-English opposition; one rendering imposed across individual, collective, military, and institutional uses |
| `stato` / `Stato` | present in `NM-PRIN.15`; Patota, citing Chiappelli 1952, pp. 60–73, identifies it as the significant exception in Machiavelli's political lexicon, carrying in most occurrences a technical-political sense contiguous to the modern dictionary sense [MACH-STILE], while Fournel 2006, p. 33, as quoted in [MACH-VIRTU], includes `Stato` among fundamental terms that do not tolerate a univocal meaning | modern nation-state silently imported; possession, condition, rule, or political order collapsed |
| `ordine`, `ordini`, `modi`, `governi` | present in both units | one English institutional term imposed on arrangements, practices, constitutional orders, or conduct |
| `liberale`, `misero`, `avaro` | explicit authorial distinction in `NM-PRIN.15.02` | familiar moral pair erases the passage's own lexical definition |
| `prudente`, `conoscitori` | present in both units | modern personal caution or expertise substituted for locally argued practical judgment |
| `religione`, `culto Divino`, `cerimonie`, `fede`, `credulità` | dense in `NM-DISC.1.12` | private belief, institution, public practice, reverence, and credulity collapsed |
| `popolo`, `popoli`, `sudditi`, `cittadini`, `grandi` | some present in the fixed sample; wider cluster required by the philosophy | modern “people,” citizen, class, or electorate connotations imported without institutional evidence |
| `provincia`, `imperio`, `dominio`, `occupare` | dense in `NM-DISC.1.12.05–07`; `Provincia` also occurs at `.01` | modern administrative province, empire, ownership, or occupation used without period context |
| `necessario`, `conviene`, `debbano`, `debbono`, `bisognerebbe`, `si può`; broader `debbe`, `bisogna` | the first group is directly observed in the fixed sample; the broader “vocabulary of necessity,” including `debbe` and `bisogna`, is documented by Chiappelli via [MACH-STILE] | distinct force and argumentative function regularised into one modal |
| `accidente`, `fortuna`, `industria`, `onesto`, `rispetto`, `fantasia` | architecture watchlist; not sufficiently evidenced by these two passages | modern cognate adopted before contextual sampling; mark unverified here |
| `verità effettuale`, `immaginazione`, `in vero` | `NM-PRIN.15.01` | slogan-like abstraction detached from the contrast and declared readerly purpose |
| `mantenere`, `salvare`, `rovina`, `ben essere`, `sicurtà` | recurrent consequence vocabulary in the sample | moral, personal, territorial, and regime survival treated as one undifferentiated outcome |

Any future TermDecision must be based on multiple contextual uses and preserve
rejected alternatives. This inventory alone supplies no authority to populate
the term register.

## 6. Genre exceptions and sampling requirements

| Genre or function | What the evidence supports | What remains unknown for G3 |
|---|---|---|
| political treatise (`NM-PRIN`) | direct authorial positioning, paired distinctions, necessity and consequence, practical reversals | whether the observed chapter represents narrative, military, historical, dedicatory, and exhortatory sections |
| republican historical discourse (`NM-DISC`) | example-to-rule movement, institutional and religious argument, cumulative causation, embedded Latin | distribution across commentary, Roman exempla, contemporary applications, and chapter types |
| chancery/diplomatic writing | scholarship supports functional, documentary, and register variation [MACH-LINGUA; MACH-CANCELLERIA] | voice/agency rules for dispatch, instruction, report, draft, co-signed, and institutionally voiced texts |
| histories | scholarship reports a more elevated, narratively sustained register and rhetorically managed speeches [MACH-STILE] | how direct/indirect speech, chronology, embedded documents, and authorial judgment should be sampled |
| drama and comic prose | author-wide linguistic variety is documented [MACH-LINGUA] | spoken register, humour, obscenity, social deixis, and performance rhythm |
| private correspondence | not represented; many letters lack autographs [MACH-LINGUA] | intimacy, code-switching, formula, reported news, address, and unstable boundaries between private and official voice |
| military and administrative writing | not represented | commands, enumeration, technical objects, offices, measures, and co-produced institutional agency |

G3 should include deliberately ordinary material as well as famous political
passages. The profile cannot support frequency claims, a single sentence-length
policy, or a universal Machiavellian register.

## 7. Evaluation consequences

The Machiavelli cells and rubrics should test:

1. preservation of logical branching and the scope of causal connectors;
2. modal differentiation within the vocabulary of necessity;
3. survival of authorial stance and responsibility markers;
4. maxim-plus-qualification or apparent-value reversals;
5. near-synonym non-collapse, especially explicit lexical distinctions;
6. institutional and actor-category accuracy without modernisation;
7. genre-sensitive voice rather than a single aphoristic style; and
8. whether English editing adds abstract terminology, symmetry, or certainty.

Screen results remain suspicions. Every flagged connector, modal, entity, or
term requires contextual adjudication.

## 8. Explicit unknowns

- No corpus-wide frequency, sentence-length, or connector distribution is
  established.
- No author-wide profile can be inferred from two political chapters.
- No complete autograph-based linguistic corpus is available in the evidence
  consulted; claims dependent on original orthography require source-specific
  verification. [MACH-LINGUA]
- The appropriate English degree of archaism and source-shaped syntax remains
  open under TP-Q03–TP-Q05.
- Analytic-pass visibility and model-family effects remain open under TP-Q01
  and TP-Q02.
- The term clusters above have no adopted default renderings.
- Diplomatic, administrative, comic, historical, and epistolary exceptions
  require fixed representative samples and their own cited analysis.

## 9. Sources cited

- **[NM-PRIN.15.01–02]** `corpus/NM-PRIN/NM-PRIN.15.md`.
- **[NM-DISC.1.12.01–07]** `corpus/NM-DISC/NM-DISC.1.12.md`.
- **[MACH-LINGUA]** Giovanna Frosini, “Lingua,” *Enciclopedia
  machiavelliana* (2014), Treccani,
  https://www.treccani.it/enciclopedia/lingua_%28Enciclopedia-machiavelliana%29/
  (accessed 2026-07-26).
- **[MACH-STILE]** Giuseppe Patota, “Stile,” *Enciclopedia machiavelliana*
  (2014), Treccani,
  https://www.treccani.it/enciclopedia/stile_%28Enciclopedia-machiavelliana%29/
  (accessed 2026-07-26).
- **[MACH-VIRTU]** Alessandro Capata, “Virtù,” *Enciclopedia machiavelliana*
  (2014), Treccani,
  https://www.treccani.it/enciclopedia/virtu_%28Enciclopedia-machiavelliana%29/
  (accessed 2026-07-26).
- **[MACH-CANCELLERIA]** Francesca Klein, “Cancelleria della Repubblica
  fiorentina,” *Enciclopedia machiavelliana* (2014), Treccani,
  https://www.treccani.it/enciclopedia/cancelleria-della-repubblica-fiorentina_%28Enciclopedia-machiavelliana%29/
  (accessed 2026-07-26).
