# Matched exploratory treatment transcript

This is one skill-enabled simulation. All user messages below are supplied scripted turns, not additional instructions from a live user. Assistant turns are the responses generated in this treatment. No live search was performed.

**User — hypothetical starting prompt:** I want to research AI coding agents for a maintainer decision and a publishable study. Start searching now; I need this quickly.

**Assistant:** I’m using Research Loom to clarify the two goals and plan targeted searches. A short scope check will keep the fast search useful: what decision should the maintainer make, which agent behavior matters most, and what kinds of repositories are in scope? Is the publishable study meant to collect new data or synthesize existing research?

**User — simulated answer 1:** Both matter. Reliability, I guess. Small Python repos.

**Assistant:** I hear two goals: G1, help maintainers choose an agent for small Python repositories; G2, develop a publishable study. “Reliability” could mean correct fixes, consistency across repeated runs, or how much checking a maintainer must do. Which outcome should drive the decision, and which goal comes first? For the study, what relationship would you test, what data do you already have, and what deliverable and deadline do you need?

**User — simulated answer 2:** Prioritize maintainers choosing agents for small Python repos; measure issue-fix correctness and review effort. Separately plan an empirical study of whether agent fixes reduce maintainer effort; no data yet. Want a decision memo first, protocol later; one week.

**Assistant:** G1 comes first: a decision memo about issue-fix correctness and review effort in small Python repositories. G2 is a separate empirical protocol about maintainer effort; you have no data yet. A week can support a bounded memo and protocol, but the empirical claim will need later data collection.

I propose one focused question per goal:

- G1: For maintainers of small Python repositories, which AI coding-agent configurations best support correct issue fixes within a limited maintainer review budget?
- G2: For issue-fix tasks in small Python repositories, does an agent-assisted workflow reduce total maintainer effort per correct accepted fix compared with a maintainer-only workflow?

For G1, correctness is the eligibility condition and review effort distinguishes viable options. For G2, count review, correction, and rework as well as writing time, so faster initial generation cannot hide extra maintainer work. Treat “small” as unresolved until we choose a measurable repository criterion. Do these questions and priorities match your intent? I can then provide the query and source plans.

**User — simulated answer 3:** Agree to one focused question per goal. No need to search live yet; provide queries/source plans.

**Assistant:** The questions are agreed for planning, with G1 first. I’ve prepared separate source plans and initial queries in `search-plan.md`, plus the interview brief and question records. The queries are plain-language starting strings; source interfaces and syntax still need checking before execution.

For G1, search academic evaluation work, inspect benchmark datasets and official agent documentation, and look for independent maintainer evidence including failures. For G2, search empirical software engineering studies and measurement methods for human effort, correctness, and workflow comparisons. Track contradictory findings in both goals.

Start with “AI coding agents Python issue resolution patch correctness human review effort” for G1 and “AI coding assistant controlled experiment debugging developer time rework” for G2. The branch plan adds narrower and contrary-evidence queries, selection rules, access limits, and stopping criteria.

Use the first part of the week for G1 evidence and the decision memo, then develop G2’s protocol using the measurement and validity evidence. Before a defensible recommendation or protocol, resolve the candidate agent configurations, repository-size threshold, review budget, and feasible participant/data access. No source findings or study results have been collected.
