---
name: experiment-and-method
description: "Implement research methods or register and run authorized experiments with method fidelity, complete outputs, reproducibility and checkpoint records."
---

# Experiment And Method

Read model and economic-test protocols separately. Map source equations to implementation and label faithful replication/adaptation. Complete the experiment config before registration. Use `prepare-run` to preserve code/config/input identity; `run` only within current user-authorized scope. Snapshot helper code and package locks as well as entrypoints. Preserve failure/null outputs, logs and complete estimates. For long jobs, implement model/optimizer/RNG checkpoints and a tested resume procedure; the runner does not provide those automatically. After changes/resume make a new run linked through parent_run. Explain inference based on the design rather than imposing a universal estimator.

Read [the relevant protocol](../../../docs/methods-and-inference.md) when carrying out this workflow. Read `profiles/researcher.md` and the active paper context for preferences; current user instructions prevail.
