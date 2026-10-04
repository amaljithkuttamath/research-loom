# Project configuration

Keep project configuration at `<project>/.research-loom/config.json`. The initializer copies the bundled asset and sets a stable UUID project identity and records its resolved directory. Stage selections are skill names, not executable commands. Search branches contain an ID, selected skill, and source; add any number of entries. `auto` instructs search planning to select actual sources and expand branches per goal.

The user can select a skill for any stage through conversation. Persist that choice in this project's configuration, keeping other stages unchanged. For multiple goals, optionally give each goal `stages` overrides and its own `search_branches`; absent overrides inherit the project choices. Each goal needs a stable `id` and agreed `question` once narrowed. Store interview answers and confirmation status in state; an empty goals list means interviewing has not yet established them.

Environment overrides:

- `RLOOM_PROJECT`: project directory when `--project` is omitted.
- `RLOOM_STAGE_INTERVIEW`, `RLOOM_STAGE_NARROW`, `RLOOM_STAGE_SEARCH_PLAN`, `RLOOM_STAGE_SYNTHESIZE`, `RLOOM_STAGE_OUTLINE`, `RLOOM_STAGE_DRAFT`, `RLOOM_STAGE_REVIEW`: selected skill name for that stage.
- `RLOOM_SEARCH_BRANCHES`: JSON array of branch objects with `id`, `skill`, and `source`.

Resolve with `python3 scripts/project_config.py resolve --project /path/to/project`. Add `--goal <id>` to resolve goal-specific choices. Order: live user instruction (handled by agent), environment, selected goal override, project configuration, bundled default. Environment choices are reported but never saved by resolution. Project relocation requires explicitly updating `project_root` after verifying identity and artifact paths; a copied config is rejected. No credentials belong in these files.

To remember a conversational selection, edit configuration and record the decision in state. Do not save a temporary environment override as a permanent choice without the user's request. Do not silently migrate choices between projects. New projects use bundled defaults; copying another project's profile requires a user request. Missing selected skills are a stage blocker, not grounds for silently replacing them.
