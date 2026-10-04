# Research Loom live tooling dogfood

Fixture question: How does LangChain OpenWiki separate agent research from durable queue and claim bookkeeping?

This is a simulated confirmed user brief with real web tooling. The simulated confirmation does not represent actual user consent. No install, OpenWiki execution, external mutation, or bundle edit occurred.

Outcome: project_config init and resolve succeeded; research_data init and validate succeeded. Three inspected primary sources, two actual site-limited queries plus a direct code follow-up, and four supported claim records were persisted. State ends at synthesis with next_action=complete; no outline/draft/review nodes were created.

Observed defects and limits:

1. Synthesis instructions still say to pass to outlining. This conflicts with the orchestrator's synthesis-only endpoint. I followed the explicit requested deliverable and orchestrator endpoint.
2. The contract represents repository documentation and source code as papers. It works structurally with authors=[], publication_status=unknown and optional source_type; neutral source terminology and source-kind documentation would fit better.
3. Direct-resource inspection is representable only as a search with an optional query_type field. It should be distinguished from search-engine retrieval in future UI counts.
4. Validation establishes reference integrity and reading-level consistency. It does not verify that evidence supports claim text, goals exist in config, URLs resolve, timestamps are ISO dates, or state nodes have their required outputs. This run manually checked claim locators and output existence.
5. Mutable main URLs lack a commit or byte-level source snapshot; checked_at and line locators help audit but do not guarantee future reproducibility.
6. I persisted the plan after initial queries, violating the plan-before-execution instruction in this dogfood. This is disclosed rather than hidden; stage completion means artifacts exist, not full protocol conformance. Query timestamps are approximate minute-level values rather than tool telemetry.
7. This run exercises two branches but not parallel worker isolation, interruptions, stale descendant handling, or scientific source/version deduplication. It is a tooling dogfood, not a benchmark or reliability claim.

Artifacts: .research-loom/config.json, .research-loom/state.json, .research-loom/research.json, search-plan.json, ownership-branch.json, durability-branch.json, synthesis-brief.md, validation-result.json.

## Post-fix retest

Current synthesis instructions were reread and now explicitly finish a research brief at synthesis. Both exact queries were rerun from the already persisted plan, with clock-tool brackets 2026-10-04T18:44:25Z to 18:44:27Z. Fresh search-004/search-005 and attempt-2 branch/state records were appended; original search-001/search-002/search-003 and first-attempt history were preserved. The retest stores the tool response in retest-search-response.json. Existing full-text claim evidence was reused rather than relabeling snippets as full text. Data validation passed: 3 sources, 5 searches/access records, 4 claims. A new synthesis brief was produced; state ends complete without paper nodes. This corrects the routing defect and demonstrates planned-query execution on the retest, without rewriting original noncompliance.

Recommendation: document optional source_type values for nonpaper material (repository_documentation, source_code, institutional_webpage) while retaining existing paper IDs for compatibility. No schema migration is required for this fixture.
