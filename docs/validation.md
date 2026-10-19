# Validation scope

Core tooling is exercised with temporary paper workspaces and synthetic inputs. Tests cover overwrite/path guards, protocol validation, input/code/config drift, run scope, process failures/logs, immutable completed runs, missing and tampered artifacts, timing failures, leading-zero identifiers, partial disclosure and reproducible synthetic outputs. `validate` checks skill structure and required templates; it is not behavioral or scientific certification.

CI is configured for Python 3.10 and 3.12 on Ubuntu, macOS and Windows. A checked-in matrix is not proof those hosted jobs have passed. Initial local and remote results are recorded in `docs/build-report.md` when verified.

Not validated by the core suite: live CSMAR/CNRDS access, vendor licenses, real-data estimates, pretrained BERT methods, full-scale reinforcement learning, econometric package outputs, arbitrary trainer resumption, manuscript PDF layout or correctness of any historical paper claim. No real research result or database connection is fabricated as a demonstration.

The synthetic example uses transparent co-holdings vectors, cosine scores and simple descriptive return spreads. It does not train a production BERT model, test a causal mechanism or report inferential significance.
