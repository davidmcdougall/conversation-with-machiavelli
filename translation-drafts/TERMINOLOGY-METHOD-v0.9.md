# Terminology distinction and recurrence method v0.9

**Status:** G2 evidence model; proposed under WI-000119

**Governing inputs:** `translation-system/TRANSLATION-PHILOSOPHY-v0.9.md`;
accepted author and genre profiles; `ARCHITECTURE-v0.1.md` §5.5

**Stopping rule:** this method defines evidence to collect and tests to run. It
does not create a terminology schema, populate a binding register, adopt a
default rendering, translate a passage, or decide TP-Q08 or TP-Q09.

## 1. Purpose

The stable point of inquiry is the source-language occurrence. An English form
is evidence about one treatment of that occurrence, not the definition of a
concept. Terminology control has succeeded when recurrence, distinction,
variation, and reasons for divergence remain inspectable. It has failed when a
register becomes a substitution dictionary or when uncontrolled variation
hides a repeated source choice.

This method operationalises six requirements from WI-000119:

1. represent the evidence behind a candidate term record;
2. prevent silent collapse of near-synonyms;
3. distinguish justified one-to-many treatment from unexplained dispersion;
4. track recurrence independently of English concordance;
5. preserve exceptions and rejected renderings with reasons; and
6. nominate seed terms for preregistered evaluation without adopting their
   English treatment.

## 2. Evidence model, not yet a repository schema

`ARCHITECTURE-v0.1.md` recognises `Term` and `TermDecision` as core concepts and
describes one file per term with default, alternatives, semantic clusters,
contexts, and decisions. The repository does not yet contain an adopted
term-record schema. The fields below are therefore a model to test in G3–G4.
WI-000119 does not create files under `terminology/` or declare any field
mandatory for production.

### 2.1 Candidate Term record

| Field | Evidence function |
|---|---|
| candidate ID | provisional stable handle; never reused as a meaning label |
| source lemma or display form | source-language point of inquiry; multiple lemmas remain separate unless evidence supports grouping |
| attested forms | orthographic, inflectional, and editorial forms, each linked to occurrences |
| language | distinguishes Italian, Latin, and mixed or quoted material |
| authors and works | exposes distribution without implying shared sense |
| recensions or work versions | prevents recurrence from erasing revision |
| genres and functional subtypes | permits stratified comparison under `profiles/GENRES.md` |
| occurrence pointers | permanent passage IDs plus local token or span location |
| source state | corpus version, integrity class, and relevant source-finding pointer |
| local function | source-accountable description of what the occurrence does in context |
| provisional semantic cluster | hypothesis grouping occurrences; never an ontology or fixed concept |
| explicit contrasts | terms the author distinguishes, coordinates, opposes, or defines nearby |
| recurrence relations | exact form, lemma, morphological family, quoted reuse, or proposed cross-context relation |
| experimental English treatments | output-specific evidence collected only after the relevant pilot output is frozen |
| alternatives considered | possible treatments attached to contexts, not a context-free list |
| rejected treatments | rejected form, affected occurrences, reason, evidence, and decision status |
| exceptions | occurrence or class that should not follow a current default hypothesis, with reason |
| uncertainty | open sense, attachment, source, recension, or grouping question |
| evidence status | sample-observed, cited scholarship, reviewer finding, comparator evidence, or unknown |
| decision pointers | TermDecision and DEC pointer where a later choice is doctrinal |
| provenance | creator, date, evidence version, and supersession history |

The record must carry the warning: **do not mechanically apply a rendering**.
Any future default is a review prompt whose authority, evidence scope, and
exceptions are visible.

### 2.2 TermDecision record

A TermDecision is a versioned claim about defined occurrences or an evidence
class. It should record:

- decision ID and status (`proposed`, `tested`, `accepted`, `rejected`, or
  `superseded`; no status is adopted under WI-000119);
- candidate Term ID and exact occurrence scope;
- question answered and alternatives considered;
- evidence used, including negative and disagreement evidence;
- chosen treatment if any, with reason and confidence;
- known exceptions and rejected treatments;
- author, genre, work, recension, and date boundaries;
- review finding or experiment pointers;
- doctrinal DEC pointer if the decision changes protocol; and
- supersession relation preserving the earlier decision.

An unexplained preference is not a decision. A frequent English form is not a
default merely because it is frequent. Comparator agreement is evidence, not
authority.

## 3. Occurrence-first workflow

### Step 1 — collect without normalising meaning

Record every occurrence in the frozen sample by passage ID. Preserve surface
form and source state. Lemma grouping may aid search, but must not silently
merge distinct words, homographs, Latin forms, editorial expansions, or
recension states.

### Step 2 — describe local function

Before viewing pilot English, record grammatical role, referent or target,
argumentative function, nearby definition or contrast, institutional context,
and material ambiguity. The description may say that `Questa ragione` refers
back to an argument; it may not preselect an English equivalent.

### Step 3 — propose clusters as hypotheses

Group occurrences only for a stated reason: shared local function, explicit
authorial relation, recurring institutional referent, or a hypothesis supplied
by cited scholarship. Record counterexamples and uncertain membership. A
cluster can cross authors or genres only as a comparison question.

### Step 4 — freeze output-specific treatments

After each experimental output is frozen, attach its English treatment to the
same occurrence pointers. Do not overwrite source evidence with English
lemmas. Preserve omission, paraphrase, note, and unresolved escalation as
distinct outcomes.

### Step 5 — screen for suspicion

Generate four review queues:

1. one source form receiving materially different English treatments;
2. distinct source forms receiving the same English treatment;
3. a treatment diverging from a tested default hypothesis; and
4. a term-dense passage in which local distinctions or recurrence become less
   inspectable.

Each queue is a prompt for contextual review. None is an automated finding or
repair.

### Step 6 — adjudicate with scope

The terminology auditor records the affected occurrences, failure type,
evidence, and recommendation. A later adjudicator may accept variation, record
an exception, propose a TermDecision, or return the output. The translation is
never silently conformed by the screen.

## 4. Near-synonym non-collapse rule

Distinct source forms must remain separately traceable even when English
cannot sustain a neat lexical contrast. A **collapse candidate** arises when
two or more source forms receive the same English treatment in a context where
the source supplies evidence of distinction.

Evidence of distinction, strongest first, includes:

1. explicit authorial definition or correction;
2. direct coordination, opposition, or contrast in the same passage;
3. different grammatical or institutional functions within a shared cluster;
4. stable differentiated use across multiple occurrences; and
5. cited historical-linguistic evidence, marked with its author, work, and
   genre scope.

`NM-PRIN.15.02` supplies the model dry run: `avaro` and `misero` are explicitly
distinguished. The method records two source forms, the same passage pointer,
the definition relation, and a high-priority collapse check. It proposes no
English pair. If a pilot uses the same English word for both, that is a review
finding candidate—not an automatic error—because surrounding syntax or a note
may preserve the distinction. The reviewer must state whether the source
distinction remains inspectable.

Conversely, lexical difference alone does not require different English words.
Inflection, ordinary variation, register, or English grammar may justify
convergence. The reason and occurrence scope must be recorded.

## 5. One-to-many and many-to-one treatment

### 5.1 One source form, several English treatments

One-to-many treatment is permitted when local function, sense, referent,
genre, author, recension, syntax, or English grammar materially differs. It is
suspicious when comparable occurrences diverge without a recorded reason.

For every dispersion candidate, review:

- whether the occurrences belong to the same provisional cluster;
- whether the English difference preserves or invents a distinction;
- whether one output is paraphrastic, omitted, or note-dependent;
- whether author, genre, or recension explains the divergence; and
- whether a current default hypothesis created pressure against the context.

### 5.2 Several source forms, one English treatment

Many-to-one treatment is permitted where English lacks a useful contrast and
the local argument does not depend on it. It is suspicious when it erases an
explicit distinction, actor category, institution, modality, hedge strength,
or causal relation.

The review record must identify the source forms separately, the shared
treatment, the evidence of distinction, and how—if at all—the output preserves
that evidence elsewhere. “Natural English” is not a sufficient reason.

### 5.3 Defaults and exceptions

A tested default hypothesis may reduce needless drift, but it never overrides
an occurrence. Every exception records:

- occurrence pointers;
- default hypothesis departed from;
- contextual reason;
- evidence and reviewer;
- whether the exception is local, genre-bound, author-bound, or recension-bound;
  and
- whether the case weakens the default itself.

Repeated exceptions of the same kind should trigger review of the default or
cluster definition rather than accumulation of boilerplate. WI-000120 must
preregister any triggering count and its evidentiary rationale before output.

## 6. Recurrence tracking

Recurrence is computed and inspected at separate layers:

| Layer | What counts | What it may show | What it cannot establish |
|---|---|---|---|
| exact form | character-level source form after declared search normalisation | repeated wording, orthographic pattern | stable lemma or sense |
| lemma/family | declared morphological grouping | broader lexical recurrence | conceptual identity |
| passage relation | explicit quotation, response, definition, or textual dependency | historically grounded reuse | unrecorded influence |
| provisional semantic cluster | evidence-backed hypothesis | candidate sense distribution | fixed philosophical concept |
| English treatment | frozen output form | concordance or dispersion | source recurrence |

Reports should expose, separately:

- occurrences by author, work, genre/function, and recension;
- exact-form and lemma counts;
- cluster membership and uncertain cases;
- explicit contrasts and relationship pointers;
- English-treatment distribution by experimental cell;
- missed recurrence, false relation, collapse, and over-discipline findings;
- source-state changes that invalidate an occurrence; and
- cost and reviewer attention required to reach the judgment.

Cross-author overlap creates a comparison row, never a merged author record.
`virtù` in the two Machiavelli passages and `virtù` in `FG-CONS.1.12` may be
queried together, but agreement of spelling does not establish agreement of
function. `ragione` in `FG-CONS.1.12.03` is first recorded as an anaphoric
argument reference; broader reason-as-faculty evidence remains a separate
hypothesis until sampled.

## 7. Rejected-rendering and exception evidence

The method preserves rejected alternatives because an unexplained absence
cannot teach the system. A rejection entry should include:

| Field | Requirement |
|---|---|
| treatment | exact English form or strategy considered |
| occurrence scope | passage IDs; never “the author” without evidence |
| rejected because | source sense, register, institution, syntax, ambiguity, recurrence, or English reason |
| evidence | source feature, finding, comparison, experiment, or adjudication pointer |
| materiality | what would be lost or falsely introduced |
| status | proposed rejection, tested rejection, accepted rejection, or superseded |
| exceptions | contexts where the rejected treatment may remain viable |

Rejection is not a permanent blacklist. New genre, recension, or source
evidence may supersede it. The earlier reason remains visible.

## 8. Seed-term selection for G3 evaluation

Seed terms are test objects, not entries in an adopted glossary. WI-000120 must
freeze their occurrence manifests and decision rules before pilot output. The
following set is nominated from the accepted G1 passages and profiles.

### 8.1 Direct-development seeds

| Seed or contrast set | Direct evidence | Primary test |
|---|---|---|
| `virtù` / `vizio` and apparent moral polarity | `NM-PRIN.15.02`; `NM-DISC.1.12.06`; `FG-CONS.1.12.03` | cross-context recurrence without one imposed concept; reversal preserved |
| `avaro` / `misero` | `NM-PRIN.15.02` | explicit near-synonym distinction not silently collapsed |
| `stato` / `Stato` | `NM-PRIN.15.02`; political-form context elsewhere in the fixed set | technical-political force and non-univocity tested without automatic “nation-state” |
| `ordine` / `ordini` / `modo` / `modi` / `governi` | both Machiavelli units | morphological recurrence and institutional/practical senses kept inspectable |
| necessity and modality cluster | `NM-PRIN.15`; `NM-DISC.1.12` | force differences survive without forced English concordance |
| religion/practice/authority cluster | `NM-DISC.1.12` | belief, practice, institution, reputation, and political use do not collapse |
| political forms and relations | `NM-DISC.1.12`; `FG-CONS.1.12` | `republica`, `regno`, `monarchia`, `imperio`, `dominio`, `provincia` remain distinct and historically bounded |
| Machiavelli actor categories | `principi` (`NM-PRIN.15.01–.02`; `NM-DISC.1.12.01–.04`, `.07`); `popoli` (`NM-DISC.1.12.01`, `.04`, `.07`); `sudditi` (`NM-PRIN.15.01`) | the attested forms avoid modern compression; some members are present in the fixed sample, while the wider cluster required by the philosophy remains to be sampled |
| `cittadini` | `FG-CONS.1.12.02`; Guicciardini-scoped fixed-set evidence | the actor category avoids modern compression without being attributed to a Machiavelli passage; the wider cluster remains to be sampled |
| judgment and hedge forms | `FG-CONS.1.12` | attachment and strength, not token parity, govern review |
| `ragione` | `FG-CONS.1.12.03` | local argument reference remains distinct from the unsampled faculty cluster |
| causal and adversative connectives | all three passages | function and scope preserved; consecutive `però` not treated as adversative |

### 8.2 Expansion seeds requiring source-ready G3 samples

| Seed or cluster | Reason nominated | Condition before use |
|---|---|---|
| `discrezione` and `particolare` | central Guicciardini risk in cited scholarship | freeze passages where forms actually occur; do not infer from `FG-CONS.1.12` |
| `esperienza` / `prudenza` / reason-as-faculty | adjacent judgment cluster | distinguish from local `ragione` and record work/genre scope |
| recension-level revised terms in the *Ricordi* | tests whether word changes sharpen distinctions | source-ready linked recension units required |
| Florentine institutions and offices | architecture names anachronism and fixed-rendering pressure | select passages with verified entity and institutional context |
| diplomatic and administrative agency terms | author profiles identify mixed personal/institutional voice | record sender, office, recipient, function, and production role |

If WI-000120 cannot obtain a source-ready sample, it must record the seed as
deferred. It may not substitute an unattested famous term into the fixed
passages or manufacture an English test case.

## 9. Fixed-passage dry runs without translation

These dry runs test the evidence model only. They contain no candidate English
rendering.

### Dry run A — explicit distinction

| Field | Record |
|---|---|
| source forms | `avaro`; `misero` |
| occurrence | `NM-PRIN.15.02` |
| relation | explicit authorial distinction and definition |
| cluster | reputation and use of wealth; provisional |
| review trigger | any pilot treatment that makes the distinction uninspectable |
| default | none |
| unknown | whether English can preserve the contrast lexically, syntactically, or by a sparse note |

### Dry run B — recurrence without conceptual identity

| Field | Record |
|---|---|
| source form | `virtù` |
| occurrences | one at `NM-PRIN.15.02`; one at `NM-DISC.1.12.06`; two at `FG-CONS.1.12.03` — four across the fixed set |
| local functions | apparent quality under consequential reversal; political/military capacity; the conquering Romans' capacity in an instrumental frame; the emperors' `mancò la virtù` as the causal hinge in losing empire |
| relation | exact-form recurrence across argument, discourse, and response |
| review trigger | forced English concordance or unrecorded dispersion |
| default | none |
| unknown | which occurrences belong to comparable semantic clusters after wider sampling |

### Dry run C — same form, adjacent evidence classes

| Field | Record |
|---|---|
| source form | `ragione` |
| occurrence | `FG-CONS.1.12.03` |
| local function | anaphoric reference to the preceding argument |
| broader hypothesis | reason as a faculty in cited Guicciardini scholarship; not evidenced here |
| review trigger | the local reference translated or annotated as the broader faculty without evidence |
| default | none |

The three dry runs demonstrate distinction, recurrence, and semantic-cluster
boundaries. They do not decide TP-Q08 or TP-Q09; those questions require frozen
experimental English and preregistered decision rules.

## 10. Evaluation outputs and failure criteria

For each seed, WI-000120 should preregister how the pilot will count:

- **missed recurrence:** a source relation that the annotation/treatment makes
  unavailable to review;
- **false relation:** occurrences grouped without adequate source evidence;
- **near-synonym collapse:** a material source distinction made
  uninspectable;
- **unexplained dispersion:** comparable occurrences varied without reason;
- **over-discipline:** a default or annotation forces sameness against context;
- **false exception:** a deviation recorded where no default or comparison
  class was valid; and
- **review burden:** time and human attention required to distinguish signal
  from screen noise.

No numeric pass threshold is set here. WI-000120 fixes decision rules before
output; WI-000128 later reports unlike metrics separately rather than pooling
them into one terminology score.

## 11. Handoff and migration impact

WI-000120 receives:

- the candidate record fields to test;
- the occurrence-first workflow;
- the non-collapse, one-to-many, and recurrence rules;
- the rejected-rendering and exception fields;
- the direct-development and expansion seed lists; and
- three source-only dry runs.

There is no repository migration under WI-000119. No `terminology/` directory,
schema, record, decision status, or validator rule is created. If G3–G4 expose
a witnessed need for a schema, that proposal and any enforcement must follow
the corpus-architect sequencing rule in separate, properly authorised work.

## 12. Evidence consulted

- `translation-system/TRANSLATION-PHILOSOPHY-v0.9.md`, especially §§3–6 and
  TP-Q08–TP-Q09.
- `translation-system/profiles/MACHIAVELLI.md`, especially §§2, 4–8.
- `translation-system/profiles/GUICCIARDINI.md`, especially §§2–8.
- `translation-system/profiles/GENRES.md`.
- `ARCHITECTURE-v0.1.md`, §§3.3–3.5 and 5.1–5.5.
- `TRANSLATION_PROTOCOL.md`, failure watchlist and terminology stage.
- `register/SCHEMA.md`.
- `corpus/NM-PRIN/NM-PRIN.15.md`.
- `corpus/NM-DISC/NM-DISC.1.12.md`.
- `corpus/FG-CONS/FG-CONS.1.12.md`.
