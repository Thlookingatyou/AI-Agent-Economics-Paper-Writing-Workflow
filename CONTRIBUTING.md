# Contributing

Contributions are welcome for focused workflow improvements, clearer research instructions, portable tooling and meaningful synthetic tests. Explain the concrete problem, the changed behavior and the validation performed.

- Keep skills scoped and concise; link detailed procedures instead of duplicating them.
- Preserve researcher authorship, current task scope, original inputs, null results and reproducibility records.
- Use Python 3.10+ and the standard library for core tools unless a justified dependency is discussed.
- Use fictional or redistributable fixtures. Do not upload unpublished manuscripts, vendor exports, fitted embeddings, session profiles, credentials, private run logs or private source documents.
- Keep changes to public reusable functionality. A private research task should not become an upstream issue or pull request containing its research details.

Before submitting, run:

```sh
python -m unittest discover -s tests -v
python research.py validate
python research.py demo
```

State any checks not performed. Tests of synthetic data do not establish empirical or causal validity. If adapting third-party materials, verify their license and retain required attribution. Contributions to original project code/templates follow the repository's MIT license; third-party data rights remain separate.
