# Research brief

## Priority output: maintainer decision memo

Audience: maintainers choosing AI coding agents for small Python repositories.

Decision: select agents worth evaluating locally for issue fixing. The immediate output is a decision memo, due within one week. A recommendation to adopt an agent would require stronger evidence than a shortlist for a trial.

Outcomes: issue-fix correctness and maintainer review effort. Treat correctness as resolution of the intended issue plus absence of observed regressions under a documented validation procedure. Treat review effort as time spent inspecting, validating, explaining revisions, and handling rework. Existing tests alone are insufficient to establish correctness.

Scope assumptions to confirm during evidence collection: repository size threshold, kinds of issues, agent versions and operating modes, budget, and acceptable data-access terms. Use small Python repositories as the target context; do not silently generalize from large projects or other languages.

Memo structure: decision and scope; comparison of candidate agents; strength and applicability of correctness evidence; strength and applicability of review-effort evidence; practical constraints; uncertainties; proposed local trial. Do not use a single blended score unless the maintainer supplies explicit tradeoffs.

## Separate output: empirical study protocol

Goal: plan a publishable empirical study of whether agent-assisted fixes reduce maintainer effort. No data are available yet. The protocol follows the memo; a completed study is outside the one-week scope.

Proposed comparison: agent-assisted issue fixing versus fixing without a coding agent under comparable issue conditions. Record total maintainer effort, including setup, review, testing, rework, and unsuccessful attempts. Report review effort separately to preserve the decision objective.

A correct accepted fix is the outcome unit of interest, but failed and rejected attempts must remain in the analysis. Define issue eligibility, validation, assignment, timing, and analysis rules before collecting data. Publication suitability and novelty remain unverified.

## Current evidence status

No searches, source screening, agent trials, or empirical data collection have occurred. Agent performance, time savings, and relative rankings are unknown. All proposed measures and study choices are provisional design decisions, not findings.
