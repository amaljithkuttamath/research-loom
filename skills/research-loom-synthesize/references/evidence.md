# Evidence and citations

## Search and source ledger

Use supplied sources and connected libraries first. Search academic indexes and authoritative publisher, repository, or institutional pages as appropriate to the field. Browse for source verification and current literature when available; if access is unavailable, clearly bound the work to supplied evidence.

Record queries, search locations, dates, scope, and selection rationale. Search competing explanations and contradictory findings, not only support for the intended thesis. Trace relevant references backward and citing work forward when useful. Treat discovery snippets as leads.

Maintain one ledger row per source with:

- Stable identifier or URL and verified bibliographic metadata.
- Publication/version status: preprint, accepted, published, correction, or retraction when ascertainable.
- Access level: metadata only, abstract read, or full text read.
- Relevant claim, finding, methods/population, and limitations.
- Page, section, table, or other locator for the supporting passage.
- Verification gaps and the manuscript claims using this source.

A DOI confirms identity, not that a paper supports a claim. Verify titles, authors, dates, and publication details against an authoritative record before generating final bibliography entries. Distinguish preprints from later published versions and avoid counting versions as separate studies.

## Synthesis and drafting

Organize synthesis by questions, themes, methods, and disagreements. Explain how differences in setting, design, measurement, or population affect comparison. Separate what the source reports from the author's inference.

Abstract-only sources support only claims explicitly present in the abstract. Do not infer effect sizes, methods details, subgroup findings, or limitations from inaccessible full text. State access limits; use an appropriate abstract-level claim or flag full-text verification.

For quotations, verify exact wording and locator and respect applicable quotation limits. Cite paraphrases as well as quotations. Prefer original studies for empirical claims; use reviews to establish the landscape and locate originals. Preserve contradictory evidence.

## Citation audit

Check that each citation resolves to the intended work and supports the nearby claim; audit important numbers and causal statements first. Ensure every in-text citation has a reference and remove unused bibliography entries unless the venue requests a broader bibliography. Verify generated BibTeX metadata rather than trusting model memory. Keep unresolved sources visible and exclude invented or unverified entries from a final verified bibliography.

Describe novelty narrowly relative to the search performed. Never treat an unsuccessful search as proof that a study is the first of its kind. Report coverage and access limitations when making gap claims.

## Methods, validation, and topic fit

For each paper, capture the method, reported validation, and relevance to the user's focused question. Where reported and relevant, include dataset or population, task/setting, comparators or baselines, metrics, uncertainty, and robustness checks. Cite inspected passage locators; label missing or inaccessible details explicitly. An author's validation claim does not by itself establish usefulness for the user's topic.

Use four triage categories:

- `direct`: validation addresses the relevant question and setting; preserve remaining limitations.
- `indirect`: validation exists in a different task, population, or setting; explain the transfer gap.
- `absent`: inspected material reports no relevant validation; bound this judgment to what was read.
- `cannot_assess`: available material is insufficient to determine validation; do not label it absent.

Record the reason and next action: deeper reading or supplement access, independent replication search, a proposed topic-specific experiment, or deprioritization. Retain useful background/proposals; triage is not automatic exclusion. Proposed experiments must remain distinct from experiments actually performed. Assessment is per goal and source version, since relevance and validation can change.

When using the shared JSON ledger, add a small `assessments` array to the paper record as described in the paper data contract. Keep the output concise and adapt the presentation to the user's needs.
