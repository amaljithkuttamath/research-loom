# Interview brief

## User answers and priorities

Topic: AI coding agents. Context: small Python repositories. Initial outcome “reliability” was vague; the follow-up established issue-fix correctness and review effort.

- G1, primary: help maintainers choose agents for small Python repositories. Deliverable: decision memo first.
- G2, secondary: plan an empirical study of whether agent fixes reduce maintainer effort. Deliverable: protocol later; retain an empirical study goal, not a literature review substitution.

Deadline: one week for the requested planning/memo work. No empirical data exists yet. User explicitly requested query/source plans without live searching after agreeing to one focused question per goal.

## Decisions and assumptions

The two goals use separate questions and search tracks. G1 informs candidate configurations, task selection, and risks for G2; existing agent benchmark scores alone cannot establish reduced maintainer effort. Correctness is a condition for useful fixes, with effort used to compare viable workflows. “Total effort per correct accepted fix” is proposed wording accepted with the question; its exact measurement and handling of failures remain protocol choices.

No exact agents, repository definition, review time budget, existing resources, participant access, or publication venue were supplied. The plan uses accessible academic metadata and original resources when available; it does not assume subscriptions or recruitment capacity.

## Unresolved material choices

1. Candidate agents, versions, model configurations, costs, and permissible tool access.
2. Operational definition of small (for example source size and active contributors), review budget, and eligible issue types.
3. G2 participants and tasks; feasibility of human baseline and repeated/counterbalanced workflow comparisons.
4. Venue, power/sample-size rationale, evaluation rubric, and failure accounting.

## Exclusions for this first pass

Large-repository generalization, non-Python generalization, broad code-completion/productivity claims detached from issue fixes, agent rankings based solely on marketing, and claims of empirical effort reduction without new data. These are proposed scope boundaries for the agreed context; exact thresholds remain open.

Next handoff: use questions.md for goal-specific planning. No decision memo recommendation is supportable until evidence is inspected.
