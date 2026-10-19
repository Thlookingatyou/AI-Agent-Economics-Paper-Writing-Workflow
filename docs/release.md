# Replication and release

This upstream repository is a public workflow template. Keep actual unpublished papers in private working repositories. Public-code authorization does not authorize distributing licensed inputs, fitted embeddings/checkpoints, private empirical outputs, chat transcripts or unpublished paper content. `.gitignore` is a practical default, not a license or complete leak detector. It does not untrack previously committed files.

Make a separate release from an explicit allowlist: original source, environment lock files, data-interface specification, synthetic fixtures, run instructions and reviewed documentation. Inspect the staged files and history before publishing. A fresh release repository avoids carrying accidental private history. Do not upload private source documents or conversation exports.

State whether the package is a synthetic demonstration, a method validation, an approximate reconstruction or a numerical reproduction. A successful synthetic run is not replication of paper estimates. Include input requirements, source/query definitions, versions, runtime/hardware, seeds, exact table/figure-to-script map, expected outputs and known discrepancies.

For private collaborators, verify data permissions separately. Prefer logical dataset IDs and checksums over copying vendor files. Check outputs for disallowed disclosure using actual applicable policies; do not invent blanket restrictions on all aggregate estimates. Keep permitted paper outputs shareable through an explicit reviewed decision.
