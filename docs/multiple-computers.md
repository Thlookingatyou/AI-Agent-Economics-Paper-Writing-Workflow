# Working across computers

## First setup

For real research, create a private working repository from the public template first, then clone that private copy using GitHub Desktop or your normal authenticated Git client. Clone the public template only to explore or contribute reusable workflow changes. See [START_HERE.md](../START_HERE.md) for both routes. Open the cloned folder in Codex. Run `python research.py doctor`. Repository skills live in `.agents/skills`, so a clone brings the shared rules and skills without overwriting global preferences. Restart/reopen the project if a new skill is not visible. For another agent, ask it to read AGENTS.md and docs/skills.md; automatic discovery varies.

Optional Claude project-local copies: `python scripts/install_skills.py --target claude`. Re-run after a workflow update; changed copies are not overwritten unless `--update` is supplied. No global directories, API keys or permission settings are changed.

Configure a per-machine data location:

```sh
python research.py configure --data-root "/path/to/private/research-data"
```

Windows example: `py -3 research.py configure --data-root "D:\ResearchData"`. This saves `.local/machine.json`, which Git ignores. Each paper's `data/README.md` describes the relative inputs underneath that root. Database authentication is established separately on each computer.

## Switching devices

1. Update paper state, decisions and artifacts. Run `context PAPER` for a continuation brief.
2. Review changed files in GitHub Desktop or `git status`; commit and push shared records/code/manuscript sources. Check that no private data or session files are staged.
3. On the other device, pull before editing. Configure its data root and transfer allowed inputs/checkpoints separately. Check hashes against run manifests before reuse.
4. Run `context PAPER` and inspect referenced artifacts. A missing private artifact must be reported as missing rather than treated as replicated.

Keep one active writer per paper when possible. Use branches for simultaneous work. Do not resolve state/decision conflicts by discarding one history: preserve both dated decisions and identify which supersedes which. Task scope from an old device is historical context until the current request establishes what to do.

## What Git does not transfer

Licensed data, browser sessions, installed tools, running processes, uncommitted changes, ignored run outputs and chat transcripts. A copied checkpoint needs the same model architecture, code/config/input fingerprints, optimizer/RNG state, dependencies and compatible hardware to resume faithfully. Run manifests help check these; the workflow does not magically resume arbitrary trainers.

No automatic pull/merge is performed while jobs run. Pin each paper's analysis dependencies separately (for example requirements.lock or renv.lock), and record the actual hardware/library versions for GPU experiments. The core tools themselves use only Python's standard library.

Per-paper `WORKSPACE.md` files synchronize navigation. Scratch work, review packets and output bundles stay local by default; use the map to identify which permitted deliverables need transfer. See [workspace organization](workspace-layout.md).
