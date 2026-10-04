# Research Loom release edge-case dogfood

Decision: scoped edge-case PASS after contract fixes. This report alone is NOT READY as a whole-bundle release gate because other required behaviors and the novel-skill baseline comparison are outside this evaluator's executed scope. Aggregate those independent results before installing.

## Actual execution

The current eval skill, orchestrator, node contract, configuration contract, paper-data contract, synthesis skill and its evidence reference were read. Helpers ran in fresh Python processes against this isolated project. Assistant actions produced real artifacts and state transitions; assertions inspect those outcomes rather than instruction keywords. All user turns and the source are explicitly synthetic. No live search or genuine scientific support is claimed.

| Case | Outcome | Raw evidence |
|---|---|---|
| Resume running node with truncated artifact | PASS: inspected artifact, recorded recoverable pending attempt, retained original, completed a distinct recovery attempt after output verification | interruption-before.json; interruption-after-inspection.json; ../artifacts/interrupted-brief.md; terminal-complete.json |
| Explicit nonexistent selected search skill | PASS: searched skill roots and bundle, explained absence, blocked only branch, no substitute or search results | transcript.md; effective-missing-skill.json; missing-skill-blocked.json |
| Saved skill preference switch | PASS: completed run and research.json remained unchanged; original producing skill retained | state-before-selection.json; research-before-selection.json; assertions.json |
| Brief finishes at synthesis | PASS: generated fixture brief via selected alternate skill, then a fresh native synthesis brief after fix; no outline/draft/review nodes | terminal-complete.json; native-synthesis-terminal.json; ../artifacts/native-synthesis-brief.md |
| Temporary env selection | PASS: actual resolver override appears in run effective configuration; saved config bytes unchanged during run; subsequent no-env process returns default | config-before-env-run.json; effective-with-env.json; effective-after-env.json; terminal-complete.json |
| Deterministic suite rerun | PASS: both actual suites returned exit 0 after contract fixes | test_project_config.log; test_research_data.log |

## Defects retained and retest

1. Pre-fix node contract said a changed selection makes descendants stale, contradicting orchestrator. Parent corrected it. Actual post-fix saved selection switch preserved state/evidence as expected.
2. Pre-fix synthesis skill instructed passing sufficient evidence to outlining, contradicting terminal brief path. Parent corrected it. Actual post-fix native synthesis produced a brief and no paper stages.

These two were discovered as contradictory executable instructions, not falsely reported as observed failed assistant outputs. The pre-fix wording was captured in the actual tool output before the parent correction. Hash collection began after the correction landed, so the saved initial/final hash manifests both describe the fixed bundle; they are not represented as pre-fix hashes. The observed pre-fix excerpts are retained in pre-fix-observed-excerpts.md.

## Limits

Single-run synthetic scenario observations, evaluator and target share context. No blinded evaluation, baseline comparison, repetition, real search, or scientific research-quality claim. This subreview does not cover interviewer, multi-goal behavior, question confirmation, branch discovery, real access limitations, manuscript writing/review, or skill frontmatter validation. The other reviewers must supply the remaining required evidence for a global gate. Exact backend model identity is not exposed to this evaluator; metadata says so.

Scripts are helpers, not a graph runner. The observed missing-skill check, output inspection, metadata recording, transitions and stop decisions were performed by the assistant following skill instructions. The report does not claim that project_config.py automates them.

One design note: interrupted attempt is preserved as pending with superseded_by pointing to successful recovery. On future resumption, orchestrator should honor supersession; adding this convention to the state contract would make it less ambiguous, but no false completion occurred here.

## Bundle changes during the test
