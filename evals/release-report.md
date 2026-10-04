# v0.1.0 release evaluation

Decision: scoped v0.1.0 pilot release; required checked paths pass after fixes. This is not a statistical reliability certification.

## Executed checks

- 12 project-configuration CLI tests pass: fresh-process persistence, separate projects, temporary environment overrides, goal-specific selections, many search branches, malformed/duplicate input rejection, and state preservation.
- 11 paper-data tests pass: linked records, dangling references, duplicate IDs, abstract/full-text boundaries, verified support, executed-search records, versions, repeat discovery, and contradictions.
- 3 installer tests pass: dry-run, idempotent complete installation, and conflict rejection before writes.
- All 10 skills pass the available Codex frontmatter validator. This validates packaging only, not behavior.
- A simulated-user interview walkthrough produced two focused goals and seven source-specific branches. Nine artifact assertions passed; this is one walkthrough, not nine independent trials.
- A separately initialized no-skill control produced useful goal separation and questions too. A later fresh treatment used the exact same opening and scripted answers as that control. Both produced useful questions and per-goal plans; the treatment also produced helper-validated project state and twelve planned ledger records. See comparison.md. These single-context walkthroughs do not establish measured reliability or research-quality improvement.
- Astra independently exercised interrupted output, temporary selections, preserved evidence after selection changes, missing selected skill, and the synthesis-only endpoint. Fixtures were synthetic and evaluator/target context overlapped. No graph-service runtime is implied.
- Live tooling dogfood searched official LangChain OpenWiki material, retained 3 source records and 4 evidence-linked claims, and finished at synthesis. Original 3 search/access records include a disclosed plan-after-search deviation. A subsequent attempt reran both queries from the saved plan, appending 2 actual searches rather than rewriting history. Direct URL access is labeled separately. Mutable source URLs and approximate initial times remain visible.
- Claude Code 2.1.289 loaded the personal skill and asked focused questions for two goals. The test allowed reading/skill loading only; it explicitly reported that it could not persist state with write tools disabled.
- A namespaced Claude plugin invocation also succeeded and entered interviewing for the new project.
- An isolated Claude marketplace installation succeeded and reported all 10 skills. No hooks, agents, MCP servers, or LSP servers are included. Marketplace and plugin manifests pass strict validation with no warnings.

- Codex registered the local catalog and installed `research-loom@research-loom` version 0.1.0 through its native plugin CLI. Remote GitHub installation is verified separately after publication.

## Defects found and fixed

1. The initial graph described sufficient evidence as always leading to paper outlining. The graph and synthesis instructions now finish research briefs at synthesis.
2. State instructions could mark evidence stale solely when a selected skill changed. Selection changes now affect future runs; actual input/question changes determine invalidation.
3. Recovery lacked an explicit link from an obsolete interrupted attempt to its replacement. `superseded_by` is now part of the contract.
4. A referenced configuration script was initially absent. It is implemented and directly tested.
5. Nonacademic source records and direct inspections were awkwardly implicit. The data contract now documents `source_type` and `query_type` without adding a database or new mandatory collections.

6. Strict Claude marketplace validation initially warned about its missing description. The description was supplied and strict validation now passes.

## Release scope and remaining uncertainty

The validated scope is host-driven interviewing, goal narrowing, planning, simple configuration/data integrity, source provenance, and synthesis/resume edge cases. Optional manuscript drafting, statistical analyses, systematic-review completeness, reviewer-response quality, broad discipline transfer, automatic-trigger precision, and repeated reliability are not certified. State transitions and semantic source support are checked by the agent/evaluator, not enforced by a graph engine. JSON validation does not verify live URLs, timestamp formats, goal existence, or scientific truth.

The pilot includes its eval skill, fixtures, and failures so changes can be evaluated again. Future quality claims require matched clean-session controls, held-out cases, repeated trials, and human ratings. Published fixture user agreement is simulated, never real user consent. No fabricated studies or research findings are reported.

## Architecture sources

- [LangChain OpenWiki](https://github.com/langchain-ai/openwiki): agent research separated from durable bookkeeping.
- [OpenWiki DeepSWE](https://github.com/langchain-ai/openwiki/tree/main/evals/deepswe): paired controlled runs.
- [OpenWiki LEDGER](https://github.com/langchain-ai/openwiki/tree/main/evals/ledger): longitudinal claim audits.
- [Agent Skills evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills): observable outputs, baselines, and iteration.
