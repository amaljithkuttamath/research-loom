# Search plans — planned only

No source, paper, or study result has been inspected. Each query below is an exact initial plain-language string, not a verified source-specific syntax claim. Before executing, verify the current interface and supported query syntax, record any translation, and record access failures. Selected search skill for every branch: `research-loom-search`; its bundled file exists and was read.

## Shared rules

Use terminology discovery to refine the strings with an audit trail. Prefer primary original research, benchmark artifacts, versioned repositories, and official configuration documents. Abstracts/metadata can screen candidates; inspect relevant full-text passages/artifacts before using a finding. Tag Python, task type, repository-size fit, agent/model/version, reading level, source version, and human-effort measure. Deduplicate publication versions without erasing branch provenance.

For each branch, initially screen up to 20 relevant records across its queries, prioritizing original evidence and clear context fit. Stop earlier after two consecutive query variants produce no new eligible evidence. If the cap is hit, report coverage limits rather than claiming saturation. Follow references to promising originals within the same budget. These are pragmatic limits, not a systematic-review completeness claim.

Academic sources have unverified tool access; ACM/IEEE full text may require subscriptions. If blocked, use legitimate author/institutional copies or label metadata-only access. Site-limited general web discovery is a fallback and must be labeled as such; it does not provide equivalent database coverage. No access, interface behavior, or tool availability is claimed here.

## g1-evaluation (G1)

Purpose: Academic evaluation evidence.

Source/interface to verify: Semantic Scholar and OpenAlex discovery; original publisher/preprint records after discovery.

Selected skill: research-loom-search.

Exact initial queries:

- `AI coding agents Python issue resolution patch correctness human review effort`

- `software engineering agents benchmark patch correctness Python small repositories`

Filters and reasons: No date cutoff initially; prioritize recent verified configurations later without excluding older methods. Explicitly tag language and repository-size mismatch.

Intended evidence: Original task-level evaluations and applicable reviews.

Access/tool constraint: shared access checks apply; no executed queries.

Stopping criterion: shared record/query cap plus goal-level completion criteria in questions.md. Save remaining gaps if evidence is insufficient.

## g1-artifacts (G1)

Purpose: Validate configurations and benchmark applicability.

Source/interface to verify: Original benchmark repositories/dataset documentation and official agent documentation, discovered via general web search.

Selected skill: research-loom-search.

Exact initial queries:

- `Python issue resolution benchmark dataset repository task patch tests limitations`

- `coding agent issue fix official documentation model version sandbox tools`

Filters and reasons: Prioritize original artifacts and versioned snapshots. Do not infer effort from benchmark correctness.

Intended evidence: Dataset/task definitions, evaluation code and official configuration documentation.

Access/tool constraint: shared access checks apply; no executed queries.

Stopping criterion: shared record/query cap plus goal-level completion criteria in questions.md. Save remaining gaps if evidence is insufficient.

## g1-counterevidence (G1)

Purpose: Failure and independent maintainer evidence.

Source/interface to verify: ACM Digital Library discovery and general web search of original maintainer reports/repositories.

Selected skill: research-loom-search.

Exact initial queries:

- `coding agents incorrect patches passing tests human review failures`

- `Python coding agent maintainer review rework issue fixes`

Filters and reasons: Retain negative and inconclusive reports; informal maintainer cases are context, not population estimates.

Intended evidence: Original failures, independent observations, human review measurements.

Access/tool constraint: shared access checks apply; no executed queries.

Stopping criterion: shared record/query cap plus goal-level completion criteria in questions.md. Save remaining gaps if evidence is insufficient.

## g2-workflows (G2)

Purpose: Original workflow comparisons.

Source/interface to verify: Semantic Scholar and ACM Digital Library discovery; original full text where accessible.

Selected skill: research-loom-search.

Exact initial queries:

- `AI coding assistant controlled experiment debugging developer time rework`

- `software engineering agents maintainer effort human baseline issue fixing`

Filters and reasons: Include conventional assistants as measurement background; distinguish them from agent workflows and tag population/task mismatch.

Intended evidence: Controlled and observational human studies plus relevant reviews.

Access/tool constraint: shared access checks apply; no executed queries.

Stopping criterion: shared record/query cap plus goal-level completion criteria in questions.md. Save remaining gaps if evidence is insufficient.

## g2-methods (G2)

Purpose: Build a defensible effort/correctness protocol.

Source/interface to verify: ACM Digital Library and IEEE Xplore discovery; institutional author copies where available.

Selected skill: research-loom-search.

Exact initial queries:

- `software maintenance experiment review correction time patch correctness measurement`

- `developer debugging experiment crossover task difficulty time on task`

Filters and reasons: No date cutoff for methods; include relevant established methods and inspect full text before adoption.

Intended evidence: Original measurement/design studies and methodology papers.

Access/tool constraint: shared access checks apply; no executed queries.

Stopping criterion: shared record/query cap plus goal-level completion criteria in questions.md. Save remaining gaps if evidence is insufficient.

## g2-counterevidence (G2)

Purpose: Find null effects and validity threats.

Source/interface to verify: Semantic Scholar/OpenAlex discovery and original institutional/preprint resources.

Selected skill: research-loom-search.

Exact initial queries:

- `AI coding tools developer productivity no improvement increased review effort`

- `AI coding experiment task contamination learning effects measurement bias`

Filters and reasons: Keep contrary results and contextual differences; do not assume adverse findings generalize to small Python issue fixes.

Intended evidence: Null/adverse comparisons, limitations and replication evidence.

Access/tool constraint: shared access checks apply; no executed queries.

Stopping criterion: shared record/query cap plus goal-level completion criteria in questions.md. Save remaining gaps if evidence is insufficient.

## Week allocation and handoff

Proposed allocation: day 1 resolve candidate/configuration and population details and execute G1 discovery; days 2–3 inspect evidence and write the memo; days 4–5 search G2 methods/workflow evidence and draft the protocol; days 6–7 check evidence links, validity, feasibility and deliverables. Adjust if access or evidence limits prevent completion. No timeline implies data collection or a completed publishable study.

G1 completion is the bounded memo criterion; G2 completion is the protocol criterion. G1 evidence informs G2 design but cannot answer G2 causally. Next eligible action is scope-parameter resolution and interface checking if the user later requests execution. Searches have not run.
