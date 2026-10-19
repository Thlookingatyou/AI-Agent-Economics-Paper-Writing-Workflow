# Toolkit verification

The public repository contains reusable skills, blank paper templates, standard-library workflow tools, and explicitly fictional datasets. It contains no paper workspaces, manuscripts with research content, licensed datasets, empirical estimates, or trained models.

## Local checks

Run the following from the repository root with Python 3.10 or newer:

```sh
python -m unittest discover -s tests -v
python research.py validate
python research.py demo
```

The 20 automated tests cover input/code drift, run scope and preserved failures, artifact integrity, declared timing errors, partial holdings, leading-zero identifiers, and deterministic synthetic outputs. Repository validation checks the 11 skills and the structure of any locally created paper workspaces. The synthetic example exercises the tooling without downloading data or training a real model.

## Hosted checks

The [GitHub Actions checks](https://github.com/Thlookingatyou/AI-Agent-Economics-Paper-Writing-Workflow/actions) run the same suite, validation, and synthetic demonstration on Windows, macOS, and Ubuntu with Python 3.10 and 3.12. Inspect the run for the version you use; an earlier successful run does not certify later changes.

These checks validate workflow behavior. They do not certify a live vendor connection, an empirical finding, a model's scientific validity, arbitrary trainer resumption, or manuscript layout. See [validation scope](validation.md).
