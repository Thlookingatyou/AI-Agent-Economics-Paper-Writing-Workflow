# AI Agent Economics Paper Writing Workflow

A reusable workflow of **11 AI-agent skills, research templates, and reproducibility tools** for economics and finance paper writing, with specialist support for asset embeddings and AI trading at the intersection of economics, finance, and computer science.

The researcher leads the scientific decisions and owns the writing. Agents help evaluate ideas, review literature, retrieve and audit data, implement methods, run experiments, diagnose results, check grammar and logic, and organize deliverables. The workflow keeps these tasks connected through explicit paper state, decisions, experiment records, and artifact provenance.

**[Start here](START_HERE.md)** · **[How to ask agents to work](docs/using-agents.md)** · **[Skills](docs/skills.md)** · **[Commands](docs/commands.md)** · **[Workspace organization](docs/workspace-layout.md)**

## Who this is for

Researchers who want consistent assistance across papers, chats, and computers, including empirical economics/finance projects and computational research on representations, market information, and learned trading strategies. The researcher profile is editable; adapt its defaults to your own topics and preferences.

This is a workflow toolkit. It does not independently establish a contribution, identify a causal mechanism, supply proprietary datasets, or automatically produce a validated paper. Its synthetic demonstration validates the workflow path; it is not a production BERT model or empirical replication.

## Quick start

**Explore locally:** clone or download this public repository, install Python 3.10+, and open the folder in your agent application. Core tools need no third-party Python packages, API keys, database accounts, or model calls. Your agent application and chosen research software have their own setup requirements.

```sh
git clone https://github.com/Thlookingatyou/AI-Agent-Economics-Paper-Writing-Workflow.git
cd AI-Agent-Economics-Paper-Writing-Workflow
python research.py doctor
python research.py demo
```

Use `python3` on macOS/Linux or `py -3` on Windows if `python` is unavailable.

**Start actual research:** create a private repository from this template before adding unpublished questions, notes, decisions, manuscript sources, or real-data artifacts. Choose **Use this template → Create a new repository → Private**, then clone that private working repository. If that option is unavailable, use the alternative in [the setup guide](START_HERE.md). A public fork remains public; it is not a private paper workspace.

```sh
python research.py new my-paper --title "My research question" --track embeddings
python research.py context my-paper
```

Choose `embeddings`, `ai-trading`, or `general`. No paper workspaces or private research records are shipped. The only included datasets are explicitly fictional fixtures in `examples/`.

## Ask the agent to use the workflow

Open your working copy as the agent's project folder and say:

> Read AGENTS.md, profiles/researcher.md, and the state.json and WORKSPACE.md for `my-paper`. Recover existing work and use the relevant repository skills. My task is: [describe the task]. My stopping point is: [evaluate only / code only / run and return separate results / edit the requested manuscript]. Keep working files and outputs organized, preserve full results, and update the research records when decisions change.

Normal language is enough; naming individual skills is optional. Codex uses the checked-in `.agents/skills` location. Other agents can read the same instructions explicitly; Claude project-local discovery copies are available with `python scripts/install_skills.py --target claude`. See [agent instructions and example requests](docs/using-agents.md).

## Research cycle

**Idea and literature → feasible design and data audit → model implementation → separate economic tests → diagnosis and review → researcher-written paper → grammar/logic checks → exhibits and replication.**

The cycle is iterative. Unexpected findings can reopen measurement or design. Define information timing, benchmarks, model selection and inference before broad searches; label exploratory changes and retain failed and null results. Model quality and economic significance are separate evaluations. Manuscript drafting or integration follows the current request, with minimal edits for grammar-only tasks.

## Included capabilities

| Area | What the workflow provides |
| --- | --- |
| Ideas and literature | Verified-source reading records, contribution/overlap checks, feasibility and falsification prompts |
| Research context | Editable researcher profile, paper state, decision/task history, artifact index and continuation briefs |
| Data and timing | Field/identifier mappings, units, missingness, disclosure completeness, joins and point-in-time audit |
| Asset embeddings | Method fidelity, leakage checks, independent validation, matched baselines and separate downstream tests |
| AI trading | Information structures, simulation primitives, strategic benchmarks, training/evaluation separation and mechanism checks |
| Experiments | Code/configuration snapshots, input hashes, logs, status, preserved failed runs and documented resume requirements |
| Results and writing | Evidence-based diagnosis, exact grammar changes, separate logic/claim review and author-controlled integration |
| Organization and delivery | Scratch work, canonical runs, review packets, curated outputs and a WORKSPACE.md navigation map |
| Teaching and replication | Layered method explanations, mentor packets, exhibit provenance and reviewed release procedures |

[Browse all 11 skills](docs/skills.md). Skills guide reasoning; they do not grant permissions or make unavailable tools appear.

## Tidy workspace, traceable outputs

```text
papers/<paper>/
  WORKSPACE.md        # navigation and delivery history
  research/           # question, literature, decisions and protocols
  code/ and configs/  # maintained implementation and specifications
  manuscript/         # designated authoring source
  work/<task-id>/     # local scratch, previews and builds
  runs/<run-id>/      # local complete experiment records and outputs
  review/packets/     # local draft/review packets
  outputs/           # local reader-facing deliverables with a short README
```

Create directories only as needed. Keep generated files out of the root, preserve authoritative sources and earlier results, and identify one clear file for the reader to open first. [Organization guide](docs/workspace-layout.md).

## Proprietary data and optional integrations

Use your own permitted datasets or the separate [CSMAR–CNRDS MCP connector](https://github.com/Thlookingatyou/csmar-cnrds-mcp). Connector installation, institution/VPN access, subscriptions, and authentication are established separately on each computer. This toolkit contains no vendor credentials or datasets and does not bundle a logged-in browser. Manual exports remain supported. [Database integration](docs/database-integration.md).

## Work across computers

Commit and push allowed sources, protocols, metadata, decisions and manuscript sources **to your private working repository**; pull before continuing elsewhere. Git does not synchronize chats, running jobs, installed software, or uncommitted changes. Raw/processed data, model weights, run outputs, local paths and sessions are excluded by default and need separate permitted transfers. Some research notes and manuscript sources are tracked, so `.gitignore` alone does not make a public working copy private. [Device guide](docs/multiple-computers.md).

## Customize the workflow

Edit `profiles/researcher.md` for researcher preferences and `AGENTS.md` for shared operating rules. The CLI and skills use this generic profile; replace its contents with your own defaults in a private working copy. Record each paper's authoritative manuscript, data contracts, model protocol and economic-test protocol. Current user instructions override defaults. [Customization guide](docs/customization.md).

## Verification and development

```sh
python -m unittest discover -s tests -v
python research.py validate
python research.py demo
```

The 20-test suite covers input/code drift, run scope and preserved failures, artifact integrity, declared timing errors, partial holdings, leading-zero identifiers and deterministic synthetic outputs. CI checks Python 3.10/3.12 on Windows, macOS and Linux. See [validation scope](docs/validation.md) and [build evidence](docs/build-report.md). No live vendor connection, historical empirical result, arbitrary trainer resumption, or manuscript layout is certified by these tests.

Contributions should be focused, preserve research provenance, and pass the checks above. See [CONTRIBUTING.md](CONTRIBUTING.md). Original code/templates are **MIT licensed**; third-party papers, services and datasets retain their own rights. Design references are acknowledged in [REFERENCES.md](REFERENCES.md).
