# AI-trading and market-simulation research

This track supports computational economics and finance, including research related to Itay Goldstein. Distinguish simulated mechanisms from empirical evidence. Use verified references in REFERENCES.md, then read the selected paper/version before implementing it.

## Define the question

Distinguish individual forecasting/trading performance, strategic interaction among learners, market price informativeness/liquidity, and real effects of market information. A high Sharpe ratio alone answers none of the other questions. Specify the mechanism and an observable distinction from alternatives.

## Economic environment

Define fundamental process, public/private signals and their precision, action/inventory constraints, order types, pricing/clearing rule, noise/liquidity traders, timing, horizon, costs and welfare metrics. Separate what an agent observes from simulator-only latent state. Log the information available at each action; a reward computed after the outcome must not become an earlier observation.

## Baselines and identification inside the simulation

Recover the selected source model's benchmark or a solvable special case. Compare competitive/myopic or otherwise appropriate analytical/numerical baselines with human-sophistication benchmarks when relevant. Match information and constraints before attributing performance to AI capability. Validate market clearing, accounting identities, limiting cases and deterministic toy paths before large training. Distinguish a coding test from an economic test.

## Learning and evaluation

Separate training and evaluation seeds, freeze learned policies when testing, repeat independent runs, show convergence/stability and report across-run uncertainty. State whether learning continues at evaluation. Multi-agent learning may be nonstationary; record opponent populations and joint versus independent training. Reusing common random numbers can improve comparison but does not create additional independent runs.

Test strategic explanations against unilateral deviations, altered opponents, communication/information restrictions and competing nonstrategic explanations as appropriate. Coordinated-looking actions or supra-competitive profits alone do not establish a specific collusive mechanism. Validate the source's mechanism tests rather than adopting its label.

Distinguish agent profit, transaction costs, inventory risk, liquidity, price error/informativeness and welfare. Define every metric against the model's economic objects and benchmark. A simulation mechanism does not establish its empirical prevalence. Predeclare which parameters are calibration, sensitivity or fitted quantities; retain all material sweeps.

## Bridge to data

List observable predictions and available empirical proxies, plus identification threats and missing order/agent-level information. ETF holdings or thematic AI exposure do not directly identify an investor's use of a trading algorithm. Start with a feasible descriptive or predictive question if causal identification is unavailable.
