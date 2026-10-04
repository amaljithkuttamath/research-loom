# Edge-case dogfood transcript

All user turns below are simulated evaluation inputs. Source material is synthetic and locally supplied. No live scientific search is claimed.

## Case 1: interrupted synthesis
Simulated user: Resume my brief. The previous run stopped while writing it.
Setup: actual init helpers ran; a running node and truncated artifact were seeded as the interruption fixture.

Actual assistant action: read persisted state and actual truncated artifact after a fresh init process; marked the attempt pending after inspecting missing required outputs. Retained artifact for recovery.

## Case 2: temporary override and terminal brief
Simulated user: For this run use research-paper-workflow for synthesis. Keep my saved preference. Finish this fixture brief; no paper requested.
Actual action: invoked resolver with RLOOM_STAGE_SYNTHESIZE and read selected installed skill plus its evidence reference.

Actual assistant actions: wrote a brief grounded in the inspected synthetic abstract; created one paper/version and one verified fixture claim; executed research_data validator, which passed; checked saved config byte-for-byte and fresh no-env resolution; marked the new synthesis node complete only after verification. No outline/draft/review node was created. Interrupted attempt remains preserved as superseded, never falsely complete.

## Case 3: persistent selection switch
Simulated user: Use research-paper-workflow as my future synthesis preference. Do not rerun the completed brief.
Actual action: changed saved synthesis selection only; preserved completed artifact, evidence and producing-skill run record.

## Case 4: nonexistent selected search skill
Simulated user: Use research-loom-nonexistent-edge-20261004 for my next search branch.
Actual action: persisted the explicit branch selection and began skill availability check.

Availability check executed with rg over bundle and skill roots; no matching SKILL.md, exit status 1.
Actual assistant response recorded for simulated user: The selected search skill research-loom-nonexistent-edge-20261004 is unavailable in the bundle and available local skill roots. This branch is blocked; no search was executed and no substitute was selected. Choose an installed replacement or provide the missing skill.
Actual action: marked only selected search branch blocked; no search record created and completed synthesis preserved.

## Case 5: native synthesis terminal after fix
Simulated user: For this check invoke the bundled synthesis skill and produce the fixture brief.
Actual action: read the updated native synthesis skill, its evidence reference and project research.json, then wrote a fresh brief with the fixture counts and evidence limits. Recorded the native skill hash and terminal completion; no outline, draft or review node was created.
