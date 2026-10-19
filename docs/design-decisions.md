# Why this workflow differs from the previous process

The user authorizes revising the process. These choices preserve authorship and improve inference without turning every step into an approval gate.

| Previous friction or risk | Chosen improvement | Practical cost |
| --- | --- | --- |
| Ideas advance before their data exist | Early feasibility memo using actual exports | A short audit before implementation |
| Models trained before evaluation criteria are clear | Separate representation and economic protocols | Explicit outcomes/benchmarks up front |
| Surprising results invite many variants | Preserve nulls and a specification ledger; compare on common samples | More complete internal records |
| Broad training can leak into predictions | Point-in-time audit of training, tuning and scoring | Restricts predictive claims unless inputs permit them |
| Work scattered across chats/devices | Paper state, decision history, artifact index, portable brief | Update a small record when decisions change |
| Agent polishing can change meaning | Grammar and logic outputs separated; exact edit log | A reviewable patch |
| An attractive plot hides incomplete inference | Retain full results, covariance, N, time/cluster counts | Keep machine-readable outputs |
| Long jobs are expensive to repeat | Run snapshots, logs, checkpoints and explicit resume contract | Training code must implement its own checkpoints |

Implementation is a small standard-library CLI, Markdown/JSON state and modular skills, not an autonomous agent framework. It does not lock the researcher to a particular model provider, language, estimator or journal. Human decisions about contribution, identification and interpretation stay visible.

The upstream repository is a public, reusable workflow template. Actual unpublished research belongs in private working copies; paper replication releases should be separately assembled and reviewed. There is no automatic publication, retraining, manuscript rewriting or scheduled external job.
