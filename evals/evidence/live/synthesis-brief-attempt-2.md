# OpenWiki ownership and durability synthesis

Dogfood fixture: the question and confirmation are simulated inputs, not actual user consent. This run uses real web queries and inspected primary sources.

OpenWiki places repository investigation, planning and page writing with the host coding agent. Its lifecycle layer manages queue durability, claim reconciliation, source drift and finalization (claim-001). [README](https://github.com/langchain-ai/openwiki/blob/main/README.md#coding-agent-integrations)

Workers submit sparse claim decisions. The system retains unaffected claims and verifies persisted state before accepting a completed page (claim-002). [Claim reconciliation](https://github.com/langchain-ai/openwiki/blob/main/openwiki/workflows/claims-reconciliation.md#per-page-reconciliation-the-sparse-decision-payload)

The implementation serializes bookkeeping separately from model work and rejects finalization while jobs remain pending (claim-003). [Implementation](https://github.com/langchain-ai/openwiki/blob/main/src/generation/repository-run.ts#L285)

Its current host-driven grounding boundary covers repository evidence; connector-derived facts remain outside that guarantee (claim-004). [README](https://github.com/langchain-ai/openwiki/blob/main/README.md#grounded-claims)

Interpretation: a Research Loom adaptation can keep research judgment in stage skills while deterministic helpers own validated artifacts and state transitions. This is an architectural inference, not a measured reliability result.

Limits: two site-restricted search branches and one direct code follow-up; relevant full-text sections inspected; mutable main references, no commit-pinned snapshots; no OpenWiki runtime executed; no completeness claim. The plan was persisted after initial searches, so this run does not establish compliance with the plan-before-execution instruction. The selected deliverable is adequately supported and finishes at synthesis without creating a paper.

Retest: both exact saved-plan queries were rerun after the plan existed, at 18:44:25–18:44:27 UTC. Existing full-text evidence was reused. Current synthesis instructions explicitly finish at synthesis for a research brief; no outline was requested or produced. Original attempt history and its plan-order limitation remain intact.
