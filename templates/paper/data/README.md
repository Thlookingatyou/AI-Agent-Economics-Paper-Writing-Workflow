# Data contract

Raw and processed inputs stay outside Git. Configure the per-machine private-data root with `research.py configure`. Keep relative logical paths below that root; do not commit absolute user paths.

| Dataset ID / relative path | Vendor/table/query | Variable mappings | Observation key | Units/frequency | Coverage | Release/availability rule | Full/partial disclosure | Rights/receipt/hash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Audit duplicates, leading-zero IDs, missingness, merge cardinality and attrition. Preserve original files. Document unknown dates instead of guessing. Required private artifacts missing on this machine:
