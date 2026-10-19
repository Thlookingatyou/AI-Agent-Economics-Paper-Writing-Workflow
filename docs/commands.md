# Command reference

Run from anywhere using the path to `research.py`; paths below are resolved inside the clone, not the terminal's current directory. Python 3.10+; standard library only. Use `python research.py COMMAND --help`.

| Command | Behavior |
| --- | --- |
| `doctor` | Reports Python/platform, optional tools, local data-root status and skill validation; does not authenticate vendors |
| `configure --data-root PATH` | Records this device's private-data root in ignored local configuration |
| `new SLUG --title TITLE --track embeddings` | Creates a paper's state and research/model/test/review templates; refuses overwrites |
| `context SLUG` | Prints a portable continuation brief and points to missing local inputs |
| `task SLUG --mode MODE --request TEXT [--stop-after TEXT]` | Records current request and boundary, archiving earlier tasks; does not itself grant authority |
| `decision SLUG --text TEXT --source TEXT [--kind user-decision]` | Appends a dated decision/suggestion/evidence record with unique ID |
| `prepare-run SLUG --config FILE [--input FILE ...] [--script FILE ...]` | Makes an immutable registration/snapshot and returns its run ID; no computation |
| `run SLUG --run-id ID -- COMMAND ...` | Executes a registered run without a shell; captures status/stdout/stderr; requires recorded run scope and unchanged snapshots |
| `artifact SLUG --id ID --run-id ID --path PATH --kind table --label LABEL` | Registers a real existing output with checksum and provenance |
| `check SLUG` | Reports missing/unverified state, registered output integrity and run status; does not establish scientific validity |
| `audit-timing FILE.csv` | Checks declared training/availability/outcome dates; exits nonzero on invalid or unknown timing |
| `demo` | Runs an entirely synthetic, point-in-time co-holdings demonstration under `.local/demo` |
| `validate` | Checks skill frontmatter, required docs and templates |

Example experiment:

```sh
python research.py task my-paper --mode run --request "Run the specified synthetic smoke test" --stop-after "Separate outputs; no manuscript changes"
python research.py prepare-run my-paper --config papers/my-paper/configs/experiment.json --script papers/my-paper/code/analysis.py --input examples/timing_valid.csv
python research.py run my-paper --run-id RETURNED_ID -- python papers/my-paper/code/analysis.py
```

`prepare-run` requires the config to state question, purpose, design, timing, inference and selection criteria. `unknown` inference is allowed for a coding smoke test with `purpose=synthetic-demo`, not for a paper-ready empirical run. Templates must be completed. Relative command arguments use the repository root. Record every code dependency with `--script`; the workflow snapshots those files and the config, and hashes inputs without copying licensed data. Also capture package locks/imported helper code.

Run records are ignored by Git. They retain input paths privately and include an `environment.json` (platform/Python/Git revision), code snapshots, logs and a manifest. No credentials should appear in command arguments or configs. Environment variables are not dumped.

A prepared run executes once. For changed inputs/config/code or a retry/resume, create a new registration; include `parent_run` and checkpoint details in its config. Failed/interrupted runs stay intact. A killed process may leave status `running`; `check` warns that liveness is unverified. No automatic restart or job cancellation is attempted. Trainers should atomically save checkpoints and completed periods.
