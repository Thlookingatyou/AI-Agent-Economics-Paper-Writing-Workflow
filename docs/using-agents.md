# How to ask agents to follow this workflow

Open the local clone of your working repository as the agent's project folder. A link to the GitHub website alone does not provide your local files, database sessions or installed tools. For unpublished work, use a private working repository rather than this public template.

## Start or resume a chat

> Read AGENTS.md and profiles/researcher.md. Work on the paper `my-paper`. Read state.json and WORKSPACE.md, recover relevant prior decisions and artifacts, and follow the repository's applicable skills. My current task is [task]. Stop after [boundary]. Keep files organized and update the paper records when decisions change.

The current request sets scope. Historical task records and handoffs provide context; they do not authorize new execution. Replacing one old pause with a new explicit instruction is sufficient; the workflow does not require repeated permission inside an already authorized task.

## Choose the task and stopping point

| Task | Example request |
| --- | --- |
| Generate/evaluate ideas | Evaluate this idea against verified literature and actual available data. Return contribution, overlap, feasibility, falsification and the smallest useful pilot. No implementation yet. |
| Inspect data | Audit these exports, preserving original missingness and identifiers. Check disclosure completeness, joins, units, coverage and information timing. Return a precise gap list. |
| Implement a method | Build this version of the source method and show equations-to-code and deliberate adaptations. Code plus synthetic checks only; do not train yet. |
| Train a model | Run the agreed model protocol, retain seeds/configurations and checkpoints, and explain the validation comparison. Keep downstream economic selection separate. |
| Run economic tests | Run the agreed tests, preserve complete estimates and null results, and deliver separate review outputs. Keep the manuscript unchanged. |
| Diagnose | Inspect actual code, sample, timing and inference before explaining the unexpected result. Separate demonstrated explanations from unresolved alternatives. |
| Review writing | Correct grammar minimally, preserve my wording, and list logic/claim issues separately with exact locations and before/after wording. |
| Integrate reviewed work | Integrate these specific reviewed results into the designated manuscript. Update references/exhibits and give an exact change record. |
| Organize a task | Use workspace-organization; separate scratch files, experiment records, review packets and reader outputs. Give me one clear file to open first. |
| Learn a method | Explain the economic object, equations, training, worked example, actual code, baselines and failure modes so I can defend the method. |

## Skill discovery and missing tools

Codex discovers the checked-in `.agents/skills` structure. If a skill change is not visible, reopen the project/session. Other agents can read AGENTS.md, docs/skills.md and the selected SKILL.md explicitly. For Claude project-local discovery, run `python scripts/install_skills.py --target claude`; rerun with `--update` when deliberately refreshing generated local copies.

A skill supplies procedure, not authentication, computation or a connected database. Ask the agent to report missing tools/data honestly and use a precise manual export request or code-only deliverable where appropriate. It should not claim that configuration saved means a live integration was verified.

## End a task or change devices

Ask for the main conclusion, files to open, checks actually performed, unresolved issues and next useful step. Confirm that WORKSPACE.md, paper state, decisions and artifact links reflect substantive changes. Commit/push permitted shared sources and records to the private working repository, then pull on the next device. Ignored data/output/checkpoint files need separate transfer; chat history is not automatically synchronized.
