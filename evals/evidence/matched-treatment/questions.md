# Agreed question records

Confirmation: simulated user turn 3 accepted the proposed one-question-per-goal plan. Revision 1. Quantitative scope parameters remain unresolved.

## G1 / Q1 — maintainer decision

**Question:** For maintainers of small Python repositories, which AI coding-agent configurations best support correct issue fixes within a limited maintainer review budget?

Context: Python repositories selected by a measurable small-repository rule to be set before execution. Phenomenon: agent-generated issue fixes. Outcome: correct accepted fixes given a review budget, with review/correction effort reported for comparison. Do not assume tests passing establish correctness.

Key concepts and synonyms: coding agent, software engineering agent, autonomous programmer; issue resolution, bug fixing, patch generation; patch correctness, functional correctness, regression; review effort, human validation, correction time, rework; Python project, small repository.

Evidence needed: original evaluations with task/version provenance; benchmark construction and limitations; task-level correctness evidence; human review or correction effort measurements; verified capabilities and constraints for candidate configurations; counterexamples/failure analyses.

Exclusions: unsupported global rankings, extrapolation from large repositories or completion-only studies without flagging context mismatch, correctness inferred solely from developer satisfaction or pass rate.

Completion criterion: a bounded decision memo with transparent candidate comparison, inspected supporting/contrary sources, applicability limits, and an actionable conditional choice or documented evidence insufficiency. A one-week budget may require a provisional memo rather than a definitive ranking.

## G2 / Q2 — empirical study protocol

**Question:** For issue-fix tasks in small Python repositories, does an agent-assisted workflow reduce total maintainer effort per correct accepted fix compared with a maintainer-only workflow?

Context: same bounded repository/task population; study participants and tasks still to be defined. Relationship: workflow condition versus total human effort conditional on correct accepted fixes, with all failures and effort retained in analysis.

Key concepts and synonyms: agent assisted, AI assisted, human AI collaboration; developer effort, maintainer effort, time on task, review time, repair time, rework; controlled experiment, crossover, paired tasks, software maintenance; patch acceptance, functional correctness, regression testing.

Evidence needed: original controlled/observational workflow studies; effort instrumentation and correctness assessment methods; baseline design, task difficulty, learning effects, tool familiarity, task contamination, selection bias, and appropriate statistical/reporting methods. Collect new data later to answer the question.

Exclusions: declaring effort reduction from benchmark pass rates; treating accepted fixes alone as the sample and hiding failed-task effort; substituting a review paper for the empirical goal.

Completion criterion: a protocol specifying task/population criteria, conditions, correctness assessment, instrumentation, failure handling, design/assignment, analysis plan, feasibility and sample-size rationale, validity threats, and data/reproducibility plan. Protocol completion does not mean empirical confirmation or publishability is guaranteed.
