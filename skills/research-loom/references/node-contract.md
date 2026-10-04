# Node handoffs and durable state

Each node receives project identity, goal/question IDs, selected skill, applicable constraints, upstream artifact paths, and unresolved decisions. A search node additionally receives a branch ID, source, exact queries, filters, and stopping criterion.

After execution, record selected skill, input/output paths, status (`pending`, `running`, `waiting_for_user`, `blocked`, `complete`, or `stale`), evidence/access limits, decisions, and next action in `.research-loom/state.json`. Create entries as nodes actually run. Use keys that distinguish goal, stage, branch, and iteration; separate search branches must not overwrite each other's state.

Keep top-level state fields for `project_id`, `brief`, `confirmed_questions`, `nodes`, `active_node`, and `next_action`. Initialize empty state only for a new project. Save concrete artifacts within the project using its existing conventions; paths in state can be project-relative. Write state safely and preserve unrelated records.

On resume, read configuration and state, validate the project identity and referenced files, and identify pending decisions and the next eligible node. A `running` entry after interruption is incomplete until its artifact is checked against the node completion criteria. If the artifact is missing or incomplete, record a recoverable pending attempt and its unresolved work; do not mark it complete. Do not rerun completed work solely because this is a new chat. If goals, question, or source corpus change, mark affected descendants stale and explain what requires rerunning. Keep past artifacts available.

Interview completion means the goal/context is understood, not that a question is confirmed. Narrowing completion requires a specific question agreed by the user. Search completion requires executed queries and provenance, not just a plan. Review completion records actual verification and remaining gaps, not guaranteed acceptance.

Skill invocation means loading the named skill's instructions and carrying out its contract with available tools. The graph itself does not grant permission to spawn agents, install plugins, obtain subscriptions, submit manuscripts, or contact other people.

Separate the selected stage role from node instances and execution attempts. Record `run_id`, `attempt_id`, `question_revision`, upstream node dependencies, input fingerprints, resolved skill path/content hash, effective configuration (including temporary overrides), and timestamps when nodes run. A stable UUID identifies the project; its current root is a location check. Only the orchestrator writes shared state, via atomic replacement; branch workers return separate artifacts. Validate required outputs before marking a node complete.

After recovery, set `superseded_by` on the interrupted attempt to its replacement attempt ID; resume must not select an obsolete pending attempt. Keep the original artifact and failure record for audit.
