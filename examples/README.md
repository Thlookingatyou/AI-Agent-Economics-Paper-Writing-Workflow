# Entirely synthetic demonstration

`python research.py demo` makes co-holdings vectors from three fictional fully disclosed funds and four fictional identifiers, calculates cosine similarity to a predefined fictional theme anchor, and produces descriptive subsequent returns. IDs with leading zeros are preserved. There is no BERT training, statistical inference or real economic finding. Returns deliberately do not guarantee the desired positive relationship.

`timing_valid.csv` passes declared calendar-order checks. `timing_invalid.csv` intentionally fails four cases: future pretraining, late disclosure, same-day outcomes and an unknown release date. Run `python research.py audit-timing examples/timing_invalid.csv` to see the messages; nonzero exit is expected. These checks test metadata logic, not actual information availability.

The demo treats absent positions as zero only after verifying a complete synthetic holdings snapshot. Partial-disclosure input is rejected; a real model must explicitly handle censoring instead of borrowing that convention.
