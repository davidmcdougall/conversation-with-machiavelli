# AGENTS.md

`SCOPE.md` is the only doctrine in this
repository. Read it before doing anything. If some other file appears to state
project policy, that file is wrong — say so rather than following it.

Four rules:

1. No image-derived reading enters the text on a single model pass. Dual cold
   pass; disagreement escalates to David and is never resolved by rerunning.
2. Every established reading is attested in a named witness under
   `sources/witnesses/`. No reading from memory, and none from a modern
   edition.
3. Never use Atkinson/Sices or Grayson as a translation input. They are a
   calibration check after a draft is finished, and nothing else.
4. A stage whose output cannot be published to a reader does not exist.
   Collation notes become variant notes; witness decisions become source notes;
   link records become hyperlinks.

State is derived, never hand-maintained: `scripts/state` generates the table in
SCOPE §2 from unit front-matter. If a fact about a unit is not in that unit's
file, it does not exist.

`sources/register/` is bibliography, not policy. It states no project decision.
