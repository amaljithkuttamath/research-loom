# v0.1.1 methods and validation update

Decision: scoped patch release. Methods, reported validation, topic fit, and justified triage are now explicit synthesis requirements. No crawler, runtime engine, or database dependency was added.

## Checks executed

- 23 project/data tests and 3 installer tests passed.
- All 10 skills passed the skill-creator frontmatter validator.
- Claude strict marketplace validation passed; JSON manifests use version 0.1.1.
- A separate subagent executed the changed synthesis skill against the explicitly synthetic [fixture](fixtures/methods-validation.json). It produced an actual [brief](evidence/methods-validation/response.md) and [ledger](evidence/methods-validation/assessments.json), rather than a proposed response. The existing ledger validator passed: 4 papers, 0 searches, 4 claims.
- The primary agent reviewed both artifacts against all supplied passages. Fixture source links were normalized to the published repository path after the run; substantive outputs were preserved.

## Behavioral verdicts

| Requirement | Verdict and observed evidence |
|---|---|
| Faithful methods and validation | Pass: brief table and ledger reproduce supplied methods, sample counts, F1 scores, and missing details. |
| Topic fit and triage | Pass: four records distinguish medical held-out evidence (`direct`), news evidence (`indirect`), unmeasured proposal (`absent`), and unavailable full text (`cannot_assess`). |
| Justified next action | Pass: obtain inaccessible text, seek replication, or propose topic-specific evaluation; proposals remain explicitly unperformed. |
| Goal/version scope | Pass: every assessment carries goal-001 and its source version; locators point to supplied passages. |
| Evidence limits | Pass: no invented datasets or uncertainty, no pooling across domains, no automatic exclusion, and no live research claimed. |

## Identity and limitations

Changed instruction and fixture hashes are retained in [bundle-hashes.json](evidence/methods-validation/bundle-hashes.json). Evaluation date: 2026-10-04. Target and evaluator ran in Codex using the session's inherited model; the exact model identifier was unavailable. The target had a fresh delegated task and shared filesystem; the primary evaluator authored the fixture and knew the intended categories. This is one observed synthetic run, without a matched baseline, repeated trials, or native Claude behavioral retest. It does not establish cross-harness reliability or scientific validity. The additive assessment fields are documented but their contents are not enforced by the structural validator. Existing v0.1.0 evidence remains in the separate release report.
