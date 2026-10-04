# Exploratory matched-input comparison

One no-skill control and one skill-enabled treatment ran in separate fresh subagents with the same opening task and three scripted user answers. Neither examined the other's artifacts. The prompts and actual generated artifacts are retained. Exact model IDs and usage for these subagents were not returned; both inherited the host's default model. These are single-context scripted walkthroughs, not a repeated interactive benchmark or blinded human study.

| Observable requirement | Control | Treatment |
| --- | --- | --- |
| Clarifies the vague topic and outcomes | Observed | Observed |
| Separates maintainer decision and empirical study | Observed | Observed |
| One focused question per goal | Observed | Observed |
| Preserves no-data empirical goal as future work | Observed | Observed |
| Queries and sources tailored per goal | Observed | Observed |
| No fabricated sources/results or executed-search claim | Observed | Observed |
| Durable project config/state and planned-record ledger | Not produced in control artifacts | Produced and helper-validated |
| Branch IDs and selected stage/search skills | Not part of control plan | Present in treatment plan |

The treatment made workflow handoffs and saved state inspectable. The control also produced useful questions and evidence guidance; this pair does not demonstrate better scientific conclusions, fewer errors, or lower user burden. Treatment added proposed planning constraints such as a review budget and screening caps; they are labeled proposals, not asserted user preferences. Human review of those tradeoffs is still needed in real use.

This comparison satisfies the pilot's requirement to inspect a with/without-skill case with matched raw user inputs. It provides no reliability estimate or statistically supported improvement claim. Future evaluations should use repeated trials, fixed source snapshots, pinned model/harness/budget, genuine multi-turn transport, and blinded human ratings.
