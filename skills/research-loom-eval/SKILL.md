---
name: research-loom-eval
description: Use before shipping Research Loom skills or changing their graph, project memory, search provenance, or paper data contracts.
---

# Research Loom Eval

Evaluate observable behavior and artifacts before installing a release. Use isolated temporary projects. Keep the installed bundle and user projects untouched while testing. Read the selected bundle's orchestrator and changed stage skills; record their content hashes, model, tools, date, and constraints.

## Deterministic checks

Run `python3 ../research-loom/evals/test_project_config.py` and `python3 ../research-loom/evals/test_research_data.py` using paths resolved from this skill directory. Validate each skill's frontmatter and referenced files with an available skill-creator validator; for Claude Code also run `claude plugin validate --strict <skill-root>`. Report host-specific validation separately from behavioral checks. Run helper CLIs in a real isolated project; restart them in new processes and verify persisted state. Do not grade instruction headings or keywords as functional success.

## Behavioral checks

Read [../research-loom/evals/scenarios.json](../research-loom/evals/scenarios.json). Select scenarios covering every changed behavior and retain transcripts, actual artifacts, assertions, and judgments. Test multi-goal interviewing, question agreement, per-goal search routing, evidence limits, and interruption/resume. Use separate agents when authorized; otherwise record evaluator/target context overlap. Label simulated user answers and synthetic sources; do not equate them with real user approval or live search results.

For a novel skill or major workflow change, compare isolated with-skill and no-skill/previous-version runs on identical tasks and raw fixtures. Give graders the rubric and raw evidence, not expected conclusions. Report single-run results as observations; use repeated trials before estimating reliability or improvement. Judge question fidelity, useful narrowing, source/claim traceability, appropriate inference, and user burden. A source URL or successful JSON validation does not establish scientific support. For paper synthesis changes, check method fidelity, reported validation, topic fit, and justified triage. Distinguish validation absent in inspected material from validation that cannot be assessed due to access. Audit per-goal/version assessment records and verify proposed experiments are not represented as performed.

## Release gate

Save a report with bundle identity, cases attempted, raw artifact links, per-assertion verdicts, failures, limitations, and decision. A release passes only when deterministic checks pass and behavior checks for changed requirements have actual supporting evidence. Missing selected skills, cross-project leakage, fabricated results/sources, search before required question agreement, unsupported claim links, and incomplete nodes falsely marked complete are blocking defects.

Fix observed defects, then rerun affected cases and the deterministic suite. Do not discard failed trials or present synthetic comparisons as model benchmarks. Distinguish untested optional paths from verified requirements. If a required path is untested or a blocking defect remains, report `not ready` and do not install it. Passing this gate authorizes no publishing or external messages beyond the user's scope.
