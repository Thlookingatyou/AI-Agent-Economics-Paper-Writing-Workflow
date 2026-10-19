---
name: data-design-audit
description: "Inspect research exports, map database fields, audit disclosure completeness, joins, sample construction and information timing before finance/economics estimation."
---

# Data Design Audit

Read the data contract and actual files. Use an available CSMAR/CNRDS connector or prepare a precise manual export request; verify connection and access rather than assuming tools exist. Record keys, units, leading-zero IDs, full/partial disclosure, coverage, missingness, duplicate/merge checks and source mappings. Keep raw inputs intact and preserve missing values unless a documented design justifies treatment. Build the availability-to-outcome calendar, including training/tuning information. Run the timing checker on declared dates, while acknowledging it cannot prove the underlying declarations. Deliver the best feasible design and exact gaps, not hypothetical unavailable fields.

Read [the relevant protocol](../../../docs/data-and-timing.md) when carrying out this workflow. Read `profiles/researcher.md` and the active paper context for preferences; current user instructions prevail.
