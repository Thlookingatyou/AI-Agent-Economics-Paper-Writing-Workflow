# Customize your working copy

1. **Create a private copy for real research.** This upstream repository is public. Manuscript sources, questions and decisions are tracked by default; ignored data folders alone do not protect unpublished notes.
2. **Set researcher preferences.** Edit `profiles/researcher.md` for language, explanation depth, authorship, editing scope, table conventions and delivery style. The generic profile is shared by the CLI and skills. The supplied defaults are editable rather than universal requirements. Set manuscript author fields only in your own working copy.
3. **Create a paper.** Use `research.py new`; choose a track, formulate the actual question and identify existing artifacts before proposing reruns. The sample paper folders are illustrative and can be left unused. Do not delete real work to match a layout.
4. **Design before broad searches.** Complete the model and economic-test protocols separately. Set each paper's authoritative manuscript in state.json when identified, and maintain WORKSPACE.md as its navigation map.
5. **Configure private data locally.** Use `research.py configure --data-root PATH` for a real directory on each computer. Do not commit machine paths, credentials, browser profiles or licensed files. Database connectors and analysis dependencies are separate installations.
6. **Adapt methods deliberately.** No estimator, embedding dimension, journal style, inference lag or model provider is mandatory. Document deviations from source methods and validate the design using appropriate tools.
7. **Share the right layer.** Contribute reusable code, templates and synthetic tests to the public toolkit. Keep your paper's private state and findings in its private repository. Build a separately reviewed public replication release when ready.

The default maintains researcher authorship while allowing requested drafting/integration. Current user instructions supersede profile defaults; task records are not a new approval process. Repository-local rules do not change unrelated global agent settings.
