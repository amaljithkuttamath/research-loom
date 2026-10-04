# Search and source plan

Status: planned searches only. The query strings below have not been run. No named candidate or source is endorsed by this plan.

## Decision memo searches

| Purpose | Query examples | Preferred source types | Extraction priorities |
| --- | --- | --- | --- |
| Discover candidate agents | `AI coding agent Python issue fixing official documentation`; `coding agent repository issue resolution official documentation` | Official product documentation and release notes | Version, execution mode, supported workflows, verification facilities, cost and data-access constraints |
| Assess correctness evidence | `coding agents Python issue resolution independent evaluation`; `SWE-bench agent evaluation methodology verified issues limitations`; `coding agent patch correctness regression evaluation` | Original papers, benchmark methodology, reproducible evaluation repositories | Agent/version, dataset, repository languages and sizes, issue eligibility, validation, success/failure definitions, sample size, confidence and limitations |
| Assess review effort | `AI coding agents maintainer review effort empirical study`; `agent generated pull requests review time correctness study`; `AI coding assistance developer productivity randomized trial review rework` | Original empirical studies with accessible methods | Setting, participant experience, baseline, allocation, timing method, review and rework inclusion, quality criteria, unsuccessful attempts |
| Check target applicability | `AI coding agent evaluation small Python repositories`; `Python open source maintainer agent generated patches study` | Original studies and documented repository-level evaluations | Similarity to small Python repos, issue difficulty, test coverage, maintainer involvement, generalization limits |

Discovery can use scholarly indexes and the open web. Follow discoveries to primary sources rather than citing summaries as evidence. Read full methods when available; an abstract alone does not establish a reliable comparison. Official product claims establish advertised capability, not comparative effectiveness.

## Protocol searches

- `software engineering AI coding agent maintainer effort controlled experiment`
- `coding agent human review workload empirical study`
- `software engineering paired randomized experiment issue fixing learning effects`
- `AI coding agent evaluation contamination benchmark issue leakage`
- `developer productivity time measurement quality failed tasks empirical methodology`

Source priorities: original studies with protocols or instruments; software-engineering experiment methodology; benchmark validity analyses; accessible replication materials. Look for suitable issue-selection, validation, timing, assignment, and missing-data practices. Check overlap with prior work before claiming novelty.

## Screening and evidence record

Record query, search date, index, source URL, publication/update date, source type, and inclusion/exclusion reason. Extract claims with page or section locations, evaluation setting, agent and model versions, comparison baseline, denominators, correctness criteria, effort measures, and material limitations.

Include evidence that measures issue resolution or maintainer/developer effort and has enough methodological detail to assess relevance. Keep benchmark-only evidence clearly identified. Exclude unsupported marketing comparisons from outcome conclusions. Retain contradictory results and null findings. Search follow-up citations and replication materials; document inaccessible full texts instead of filling gaps by inference.

## One-week sequencing

1. Day 1: finalize scope, candidate-discovery searches, and evidence-record format.
2. Days 2–3: screen primary evaluations; extract correctness and effort evidence.
3. Day 4: verify versions and feasibility against official documentation; resolve important source gaps.
4. Day 5: draft memo with evidence-strength and applicability judgments.
5. Days 6–7: check every substantive claim against its source, revise the shortlist, and outline the later protocol.

This schedule produces an evidence-backed memo if relevant sources are available. Lack of direct effort evidence should result in a documented uncertainty and local-trial recommendation, not an invented estimate.

## Protocol outline for later development

Choose eligible issues before assignment; specify the no-agent baseline; randomize or counterbalance conditions; prevent the same participant from solving the same issue twice; standardize agent budgets and permissible interventions. Use independent correctness review where feasible. Log active human time by category, all failed attempts, acceptance decisions, and rework. Plan sample size and analysis after a feasibility pilot, and preregister primary outcomes before confirmatory data collection. Seek any required institutional review and participant consent before collecting participant data.
