# References and acknowledgments

Reviewed 18 October 2026. These are design references, not dependencies installed by the workflow. No upstream implementation or skill text was vendored. Original tools/templates are independently written. Repository features below are author-described and were not independently benchmarked.

| Reference | Design lesson used | Reuse decision |
| --- | --- | --- |
| [Econ Research Workflow](https://github.com/tsdfs930514/econ-research-workflow) | Explicit economics tasks, complete outputs and separated review | Inspiration; do not inherit a Stata-only stack or copy its credential handling |
| [EconAgentSkills](https://github.com/JonasWeinert/EconAgentSkills) | Data discipline, modern econometric choices, modular skills | Inspiration; selectively adapt only after checking the current license and method |
| [Pedro Sant'Anna's workflow](https://github.com/pedrohcgs/claude-code-my-workflow) | Persistent context, replication records, quality review | Inspiration; keep this personal workflow small and avoid automatic agent councils |
| [CSMAR–CNRDS MCP](https://github.com/Thlookingatyou/csmar-cnrds-mcp) | Existing local institutional-data bridge | Separate optional connector; do not duplicate or bundle sessions |
| [CSMAR Web MCP](https://github.com/xuan-wei/csmar-web-mcp) | Alternative campus-IP connector | Comparison option; no claim either backend is universally superior |
| [Official skills documentation](https://learn.chatgpt.com/docs/build-skills) | Repository skills in `.agents/skills` | Canonical local discovery mechanism; no global configuration change |
| [Official AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Small shared instructions plus task-specific context | Repo-local operating defaults |

## Verified starting literature for AI trading

These are public reading leads, not empirical evidence for a new study. A source page/abstract was checked; full equations and replication code must be read before implementation. Verify the version again when starting a study.

- Dou, Goldstein and Ji, **AI-Powered Trading, Algorithmic Collusion, and Price Efficiency**. [NBER Working Paper 34054](https://www.nber.org/papers/w34054); [author page](https://finance-faculty.wharton.upenn.edu/wdou/2023/05/19/ai-powered-trading-algorithmic-collusion-and-price-efficiency/). A starting point for learning, strategic behavior and price informativeness.
- Dou, Goldstein, Li and Yang, **The Limits of AI Trading**. [SSRN record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5866104); [author research list](https://finance-faculty.wharton.upenn.edu/wdou/publications/). A starting point for information access and benchmark sophistication. Working-paper versions change.
- Goldstein, **Information in Financial Markets and Its Real Effects**. [Review of Finance, DOI](https://doi.org/10.1093/rof/rfac052). A bridge from price information to real economic decisions.
