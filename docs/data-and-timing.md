# Actual-data and information-timing audit

Deliver an inventory of files, units of observation, keys, units/scales, frequencies, coverage, missingness, duplicates, merge cardinality and sample attrition. Preserve raw inputs. Record Chinese/vendor/analysis names, leading-zero identifiers, quarterly versus cumulative accounting flows, restatements, adjusted prices, share classes and universe inclusion. Distinguish fund NAV from net assets and holding value from trades.

Build a timeline with report_period, observed_at, available_at, training_cutoff, score_date, decision_date, outcome_start and outcome_end. For supervised training, include label availability and validation/tuning windows. Unknown availability is an unresolved design issue, not a date to guess. Specify close/open/timezone conventions if events are intraday; the included CSV checker accepts ISO calendar dates only and cannot decide economic timing.

`audit-timing` checks declared `training_cutoff <= score_date`, `available_at <= score_date`, and `score_date < outcome_start <= outcome_end`. These necessary checks do not prove absence of leakage; each source's actual information set still needs audit. Same-day outcomes require a finer-grained documented analysis, not a relaxed checker.

For partial holdings use a disclosure-completeness flag and distinguish observed zero from undisclosed. For empirical comparisons provide common-sample and coverage effects. Inspect date/entity distributions of the actual export; never infer full coverage solely from a requested query. Preserve original missingness unless an economic/measurement design justifies transformation.

Deliver an exact gap list with the best defensible design currently possible, optional extra data and expected benefit. Avoid demanding expensive new data before checking what exists.
