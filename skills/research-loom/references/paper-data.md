# Simple paper data contract

Keep `.research-loom/research.json` in each project. It is ordinary UTF-8 JSON with `schema_version: 1` and three arrays: `papers`, `searches`, `claims`. Initialize from the bundled asset and validate with `python3 scripts/research_data.py validate --project <project>`. A future server can read the file directly. No database or graph-service dependency is required.

Use stable IDs such as `paper-001`, `version-001`, `search-001`, `claim-001`; IDs are not array positions. Preserve them on later updates. One paper can contain several publication versions. Do not merge different studies just because their titles look similar. Treat uncertain identity as unresolved.

A paper record:

```json
{
  "id": "paper-001",
  "title": "Example title (fixture, not a real citation)",
  "authors": ["Example author"],
  "identifiers": {},
  "versions": [{
    "id": "version-001",
    "url": "https://example.org/paper",
    "publication_status": "preprint",
    "read_level": "abstract",
    "checked_at": "2026-10-04T12:00:00Z"
  }]
}
```

Populate bibliographic metadata only from inspected authoritative records. For documentation, code, datasets, or other nonpaper evidence, add `source_type` (for example `repository_documentation`); use an empty authors list and unknown publication status rather than inventing academic metadata. The same source/version links apply. `identifiers` may contain DOI/repository IDs. `publication_status` is `preprint`, `published`, `corrected`, `retracted`, or `unknown`; `read_level` is `metadata`, `abstract`, or `full_text` and records actual reading, not theoretical access. Add optional year, venue, local file path, notes, or underlying study identity when known.

A search record has `id`, `goal_id`, `branch_id`, `source`, exact `query`, `status` (`planned`, `executed`, `blocked`), `executed_at` (required only for executed searches), and `hits`. Each hit has `paper_id`, `version_id`, and optional rank/URL. Retain repeated discovery across search records. A query plan alone must not be labeled executed. Raw search-result files can be referenced by optional artifact path. Add `query_type: direct_resource_access` for direct URL inspection and `query_type: search` for search queries; direct opens must not inflate search counts. Persist the plan before executing queries and record actual execution timestamps; preserve deviations rather than rewriting history.

A claim record has `id`, `goal_id`, `text`, `status` (`unverified`, `supported`, `disputed`, `unsupported`), and `evidence`. Each evidence link has `paper_id`, `version_id`, `locator`, `read_level`, `relation` (`supports`, `contradicts`, `context`), and `verification` (`verified`, `unverified`). Add a short excerpt or paraphrase and `verified_at` when verification was performed. Quotes must respect applicable limits. The claim's evidence cannot exceed the source version's actual read level. A supported claim needs at least one verified supporting link; this structural rule does not prove the claim is scientifically true. Contradictions must remain visible.

Keep timestamps and links inspectable. Use a pinned commit, stable publication identifier, or retained source snapshot/hash where available; explicitly note mutable URLs and approximate timestamps. `full_text` means the relevant supporting passage was inspected in the full resource, not that every line was read. Record config/node/attempt history separately in `state.json`; do not duplicate the workflow state inside every paper. The orchestrator is the sole writer to shared project JSON; search branches return artifacts for it to merge. Write via temporary file and atomic replacement. This design supports a future audit UI showing a claim, its evidence locator, source/version/read level, and searches that found it.

The validator checks structural relationships and reading levels, not scientific truth, live URL resolution, goal existence in workflow state, valid timestamps, or completed-node output quality. Audit these from the actual artifacts and sources during evaluation.

## Per-goal methods and validation assessment

During paper synthesis, add `assessments` to each relevant paper record. This additive field keeps existing schema-version-1 projects readable. Each entry has `goal_id`, `version_id`, `method`, `reported_validation`, `topic_fit`, `locators` (an array), `triage` (`direct`, `indirect`, `absent`, or `cannot_assess`), `reason`, and `next_action`. Use plain text for the descriptive fields; explicitly mark unavailable details. For sufficiently validated evidence, the next action can be “use within the stated limits.” Link assessed empirical claims through the existing claim-evidence records as usual.

Assessments are scoped to both goal and version. Do not overwrite another goal's judgment or silently carry it to a later version. Keep locators for inspected method/validation passages; an inaccessible source can have an empty locator list with an explicit access gap. The structural validator currently permits these fields but does not validate their contents or scientific judgment; the behavioral eval must audit them against supplied evidence.
