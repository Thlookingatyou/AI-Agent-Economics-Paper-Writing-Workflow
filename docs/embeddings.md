# Asset-embedding research protocol

Read this when a paper trains, compares or uses embeddings; it is not a fixed BERT design.

## Economic object first

Explain what closeness represents: shared ownership, substitution, technological exposure, information similarity, or another construct. Portfolio co-occurrence identifies a statistical representation, not an economic mechanism by itself. Decide whether the paper contributes a representation method, a validated measure, an application, or identification. State independent validation and simple baselines before architecture search.

## Input and timing audit

Record portfolio/asset universe, funds entering/leaving, full versus partial holdings, report period versus release date, tokenization, ordering/permutation rule, duplicated holdings, weights and training window. Chinese Q1/Q3 top-ten disclosures are censored observations: no observation does not imply zero. Do not reconstruct trades from holding-value changes without price/flow and disclosure treatment.

For prediction, training, vocabulary construction, scaling, feature selection, theme labels, hyperparameter selection, early stopping and validation must all respect the information set. An early score produced by pooled full-sample pretraining remains retrospective. Check pretraining corpora and pretrained models too. Point-in-time data may be revised; use appropriate vintages or acknowledge limitations.

## Model protocol

Record objective/equations; architecture and dimensions; initialization; masking/negative sampling; weights; seed list; optimizer; schedules; stopping; data splits; checkpoint/optimizer/RNG state; training cutoffs and score dates. Map equations to functions and document departures from source code. Unordered portfolios need permutation-invariance treatment or a justified order.

Compare simple co-holding/cosine/PCA or other justified baselines, then candidate models on the same eligible sample, data budget and validation protocol. Align independently trained embedding spaces before comparing coordinates; within-space cosine/rank comparisons answer different questions. Raw similarity, rank, theme vector, export type and score universe require separate names. An AI-relatedness rank is not AI spending or an investment percentage.

## Evaluation

Separate representation diagnostics (stability, coverage, independent labels, neighborhood plausibility, seed variation) from downstream economic evaluation. Use time-ordered validation and a held-out final test appropriate to overlapping outcome horizons. Show coverage and common-sample versus expanded-sample comparisons. A better predictive score is not proof of a causal channel; economic significance and inference are separate.

For returns, record score vintages, availability lag, outcome dates, portfolio formation/rebalancing, transaction costs and delisting treatment. Monthly outcomes can reuse semiannual scores; report both monthly cross-sections and distinct score vintages. In Fama–MacBeth work, record the coefficient time series and temporal dependence treatment rather than treating all firm-month rows as independent.

Export complete outputs and per-method descriptions. A workbook may have a description sheet followed by quarter sheets sorted by identifier, but keep machine-readable data alongside it when practical. Inspect existing model artifacts before repeating expensive training.
