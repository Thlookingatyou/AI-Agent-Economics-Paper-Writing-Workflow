# Tidy research workspaces

The root is a navigation and source area. Workers should be able to recover how work was done; readers should be able to open a small, self-explanatory packet. Use the workspace-organization skill at the start of file-producing tasks and when preparing a delivery.

## Per-paper destination map

```text
papers/<paper>/
  WORKSPACE.md                 # tracked navigation: sources, review, deliveries
  state.json                   # tracked current research state
  artifacts.json               # tracked exhibit provenance and checksums
  research/                    # questions, literature, decisions, protocols
  code/                        # maintained analysis and training code
  configs/                     # maintained specifications and dependency locks
  data/README.md               # data contract; inputs remain private
  manuscript/                  # authoritative authoring sources when designated
  work/<task-id>/               # local scratch, previews and build files
  runs/<run-id>/                # local canonical experiment record and results
  review/
    edits.md                   # tracked edit decisions
    result-memo.md             # tracked evidence-review notes, as permitted
    packets/<delivery-id>/     # local review PDFs, comparisons and draft sources
  outputs/<delivery-id>/       # local, curated reader-facing delivery
    README.md                  # what to open, status, provenance, checks
    <descriptive-deliverable>  # only the requested outputs
  archive/private/             # optional retained local material, indexed
```

Create directories on demand. A one-file task needs only a sensible destination, not an empty folder hierarchy. New maintained code belongs in `code/`; a throwaway diagnostic belongs in `work/`. Original inputs and private data roots remain where the data contract says they are. Repository-wide development checks and demonstrations continue to use `.local/`.

Use the current task ID when available. Otherwise use a descriptive identifier such as `20261018-embedding-timing-review-v1`; add a suffix if it already exists. Delivery IDs identify revisions; labels such as `draft`, `delivered` and `superseded` describe status without inventing user approval. Avoid ambiguous `new`, `latest2` and `final_final` filenames.

## Review and delivery

A review packet is a decision aid; `outputs/` is the curated result of the requested task. Neither destination automatically means “ready for the paper” or “approved for publication.” For a draft-only request, the reader's entry point is its review packet and no final-copy step is necessary.

A useful packet guide fits on one screen:

```markdown
# Embedding timing review — draft v1
Open first: timing-review.pdf
Purpose: compare the declared score and outcome timeline.
Files: timing-review.pdf; source/ (editable figure and text sources).
Provenance: actual run/artifact IDs, or document-only with source/version.
Verified: list checks actually performed; identify unperformed checks.
Status: delivered for review; manuscript unchanged.
```

Use actual filenames and provenance, not these illustrative values. Include editable sources only when useful or requested. If copying sources for convenience, label them as a delivery snapshot and point back to the authoritative source. A manuscript build should use `work/<task-id>/build/` for auxiliary files and place only the finished deliverable in its packet. Do not duplicate trained models, raw data or complete run directories into delivery ZIPs.

## Traceability without clutter

Maintain `WORKSPACE.md` as the reader/worker map: designated authoring source, current task workspace, latest review packet, latest delivered packet, and a small delivery history with status and source/run IDs. Completed empirical exhibits should also enter `artifacts.json` through `research.py artifact`. Reader packets can refer to canonical full estimates in `runs/` rather than carrying another uncontrolled copy.

For legacy work, inventory files and references first; index existing authoritative sources in place. Reorganize only when links and reproducibility can be preserved. Record old path, new path, purpose and references repaired. Historical run manifests remain unchanged: if a relocation would invalidate their paths, retain the original canonical files and use navigation links instead. Preserve null results, checkpoints and older deliveries. Do not infer that intermediates are disposable.

## Across computers and release

The navigation file and maintained sources are tracked. `work/`, `runs/`, review packets, `outputs/` and private archives are ignored by Git. They do not appear automatically on another computer; record required transfers in `WORKSPACE.md` and report missing packets honestly. If a permitted lightweight source/output should be shared, explicitly review and opt it into an appropriate tracked location. Ignoring a folder neither encrypts it nor removes files already tracked.

Keep private working packets separate from a public replication release. Follow [release.md](release.md) for an explicit reviewed allowlist. A tidy output folder alone does not establish redistribution rights.
