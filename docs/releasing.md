# Releasing a version

<!-- SPDX-License-Identifier: CC0-1.0 -->

Every version is tagged and archived when it is released, from 0.3 onward,
not only at v1.0 (DEC-013; review pass 1). Each tag is a fixed point that a
citation can name. A version is never retagged. If a release is wrong, the
fix is the next version.

## Numbering

`SCOPE.md` carries the version ("**Version.** Draft 0.3"). `CITATION.cff`
carries it as `0.3.N`, and `scripts/state --check` fails if the two differ.
Bump the last number (0.3.0 → 0.3.1) for a release that adds or corrects
pairs or apparatus. Bump the middle number when SCOPE does (0.3 → 0.4). The
tag is `v` plus the `CITATION.cff` version: `v0.3.1`.

## Steps

No step needs Terminal.

1. **Bump.** Set `version:` and `date-released:` in `CITATION.cff`, both
   the top-level fields and those under `preferred-citation`. Add the
   version's section to `CHANGELOG.md`. Rebuild, then run
   `scripts/validate`, `scripts/state --check` and `scripts/checklinks`.
   Commit.
2. **Tag.** In GitHub Desktop, open History, right-click the release commit,
   choose *Create Tag…*, and name it `v0.3.1`. Push; GitHub Desktop pushes
   the tag with the branch. Make the tag on the release commit itself, not
   on a later commit.
3. **Release.** On github.com, open *Releases → Draft a new release*, choose
   the tag, title it "Version 0.3.1", and paste the version's `CHANGELOG.md`
   section as the description. Publish. GitHub attaches the source as `.zip`
   and `.tar.gz` archives of that tag, and those files are the version's
   snapshot.
4. **Archive.** At https://archive.softwareheritage.org/save/, save
   `https://github.com/davidmcdougall/conversation-with-machiavelli` (origin
   type `git`). Software Heritage keeps every tag permanently, independent of
   GitHub. Record the snapshot's SWHID in the version's `CHANGELOG.md`
   section.
5. **v1.0 only:** the Zenodo DOI (DEC-012 criterion 6), recorded in
   `CITATION.cff` as `doi:`.

## Tags so far

| Tag | Commit | GitHub release | Software Heritage |
|---|---|---|---|
| `v0.3.0` | `8646cd1` | to do | to do |
