# Exhibits and mentor packets

Keep semantic IDs independent of table numbers. Each exhibit maps to run ID, script, configuration, input identity, complete result file, label, sample and inference. The artifact tool checks file existence/checksum and records the run linkage; scientific validation remains a separate task.

Regression order: focal variable, interaction, controls, constant; then N, appropriate fit, effects and inference/time/cluster information. Distinguish omitted, absorbed, unavailable and not included. Parentheses must identify standard errors or t-statistics. Display selectively while preserving full outputs.

Use consistent units, labels and precision; readable fonts/notes, restrained color and legible legends. Include uncertainty when meaningful. Ensure common-sample comparisons and note sample changes. Do not manually retype regression values when they can be generated from full output.

A mentor packet can contain: the question, one design diagram/timeline if helpful, key comparisons, diagnostics, interpretations and open decisions. If exhibits-only is requested, honor it. Compile LaTeX/PDF using the actual engine/preamble and visually inspect changed pages. Overleaf bundles need all permitted sources/assets and no local absolute paths. Do not claim a PDF was checked based only on successful compilation.

Place draft exhibits in `review/packets/<delivery-id>/` and curated reader deliverables in `outputs/<delivery-id>/`, with a short packet README and an entry in the paper's `WORKSPACE.md`. Canonical estimates remain in their run directory. Follow [the organization layout](workspace-layout.md).
