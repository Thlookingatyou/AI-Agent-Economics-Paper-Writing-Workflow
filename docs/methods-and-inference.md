# Methods, experiment contracts and inference

A protocol states question, estimand, unit, measurement, sample, transformations, timing, primary specification/benchmark, inference, validation, selection criterion and falsification. Freeze or date substantive changes before a broad search; later exploration is useful when labeled. A primary designation written after seeing results is retrospective.

Keep separate model/training and economic-test protocols. Choose a model using its declared validation objective; economic p-values are not a hyperparameter search target. Report effects and uncertainty, failed runs, null results and material variants. Multiple comparisons and overlapping windows need explicit handling appropriate to the design.

Match methods to assumptions: explain the independent variation and dependence dimensions; choose relevant clustering/HAC/block bootstrap or randomization inference rather than defaults. Fama–MacBeth time-series inference, overlapping returns, panel within variation, event-window overlap and multiple agents within a shared simulated market need different reasoning. Do not encode a universal lag length, clustering rule or significance threshold.

Use trusted, documented estimation packages and capture versions. Unit-test fragile transformations and economic identities; validate source estimators against their original equations/code and a known example. Do not replace production econometrics with the synthetic demo's point estimates.

Full outputs include specification, sample counts/attrition, coefficient estimates, standard errors/covariance or documented inference output, confidence intervals, relevant fit statistics, fixed effects, time and cluster counts, transformations, exclusions and software warnings. Mark unavailable quantities explicitly. Save the estimation sample where permitted.

For resumability, trainer checkpoints should include model, optimizer, scheduler, RNG states, completed periods/steps and input/config/code identity. Atomic checkpoint writes and an explicit resume command are responsibilities of the analysis implementation. The workflow runner preserves status and logs but is not a scheduler or checkpoint engine.
