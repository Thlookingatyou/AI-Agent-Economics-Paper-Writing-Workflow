---
name: workspace-organization
description: Organize research working files, review packets and final deliverables when starting file-producing tasks, packaging outputs, or tidying an existing paper workspace. Keep generated files out of the project root while preserving source paths and reproducibility.
---

# Workspace organization

Keep a clear separation between files used to do the work and files the researcher or another reader should open. Apply this alongside the relevant research skill whenever a task produces multiple files. Follow explicit requested destinations; adapt existing working layouts rather than imposing a reorganization.

## Before creating files

Read the active paper's `WORKSPACE.md`, `state.json`, artifact index and existing layout. Identify the authoritative sources and a descriptive task ID (reuse the current task ID if available). Choose destinations before generating material; create only the directories needed. For work that does not belong to a paper, use the repository's `.local/work/<task-id>/` and `.local/outputs/<delivery-id>/` or the user's chosen folder.

Use the [workspace layout](../../../docs/workspace-layout.md) as the destination map:

- `code/`, `configs/`, `research/` and `manuscript/` hold maintained sources and shared records.
- `work/<task-id>/` holds scratch scripts, temporary conversions, previews and build files.
- `runs/<run-id>/` retains canonical experiment manifests, logs, samples, complete results and checkpoints. Do not duplicate or relocate these just to make a delivery folder smaller.
- `review/packets/<delivery-id>/` holds organized drafts and exhibits awaiting review.
- `outputs/<delivery-id>/` contains only the requested reader-facing deliverables and their short reading guide. Delivery does not imply approval, numerical replication, public-release permission or manuscript integration.

Never scatter generated PDFs, screenshots, ZIPs, temporary scripts or variant files into the workspace root. Put compilations in a task build directory using the available tool's output-directory option. When a tool requires another location, record the exception and collect the deliverable without leaving unmanaged copies.

## Finish a delivery

Give files descriptive names and use a dated/versioned delivery directory instead of `final_final` names. Preserve previous deliveries; do not overwrite them silently. Avoid copying full run trees or private inputs into a reader packet.

Write a short `README.md` in each nontrivial packet: open-this-first file, purpose/status, file list, editable source or source pointer, originating run/artifact IDs, verification actually performed, and material limitations. Do not advertise a draft as approved or a synthetic check as empirical validation.

Update the paper's tracked `WORKSPACE.md` with the latest review and delivered packets, authoritative sources, and transfer requirements. Register empirical exhibits with the existing artifact tool when they have completed-run provenance; label other document deliveries explicitly rather than inventing a run. Link final responses to the files readers should open, not scratch directories.

## Tidy existing work carefully

Inventory dependencies before moving files. Keep raw inputs, authoritative sources, immutable run records, completed checkpoints and previous deliveries intact. If paths are referenced externally or uncertain, index them in place first. For a justified relocation, keep an old-to-new map, update internal references/configuration/artifact paths and recheck the affected workflow; changing a path invalidates existing path-dependent run records, so preserve those originals. Do not delete files merely because they look intermediate or duplicate. Cleanup and retention must preserve reproducibility.

Working directories and generated packets stay local by default. Shared source and navigation records synchronize through Git; private/large deliverables require a separate permitted transfer. Folder placement does not grant data-sharing permission. Read the linked layout for tracked versus local details.
