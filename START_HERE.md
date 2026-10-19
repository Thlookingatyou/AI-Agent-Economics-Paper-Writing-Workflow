# Start here

This is the public **AI Agent Economics Paper Writing Workflow** template. It contains reusable tools, blank templates, and synthetic examples. Use a private copy for actual unpublished research.

## 1. Get a working copy

To explore the synthetic example, clone/download this repository and open its folder in your agent application. Install Python 3.10 or newer; the core workflow requires no extra Python packages. Run `python research.py doctor` and `python research.py demo` (or ask the agent to run them).

For a paper, use GitHub's **Use this template → Create a new repository** and select **Private**. Clone your new repository with GitHub Desktop or Git. Public forks remain public. If the template button is unavailable, create a new empty private repository, copy the template's source files into it without the original `.git` folder or ignored local files, then commit/push the copied files with your normal Git client. Do not send unpublished work as a pull request to this public upstream repository.

## 2. Set preferences and choose a paper

Edit `profiles/researcher.md` and the corresponding defaults in AGENTS.md for your own research. See [customization](docs/customization.md).

Create a new paper with `python research.py new my-paper --title "My research question" --track embeddings`. Available tracks are `embeddings`, `ai-trading`, and `general`.

No paper workspaces are included in the public template. Create and customize yours in the private working copy.

## 3. Start the agent

> Read AGENTS.md, profiles/researcher.md, and the state.json and WORKSPACE.md for `my-paper`. Recover existing work and use the relevant repository skills. Help me [task]. Stop after [boundary]. Keep files tidy and update the research records when decisions change.

You can evaluate an idea, inspect exports, implement code, run agreed tests, diagnose results, review grammar/logic, or organize a delivery. Specify whether to stop before training or manuscript integration when that matters. You do not normally need to name every skill. [Detailed agent guide and examples](docs/using-agents.md).

## 4. Find files and continue elsewhere

Each paper's `WORKSPACE.md` maps maintained sources, current working files, review packets and reader deliveries. Scratch/build files go in `work/`; complete experiments stay in `runs/`; reader-facing packets go in `outputs/` with an open-first guide. Create only the folders needed.

Push shared notes/code to your private working repository before switching computers, then pull on the other device. Transfer permitted data, output bundles and checkpoints separately. Run `python research.py context my-paper` to recover recorded context; inspect the underlying artifacts before trusting a historical report. [Multi-computer guide](docs/multiple-computers.md).
