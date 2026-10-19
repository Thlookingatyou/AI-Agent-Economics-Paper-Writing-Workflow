# Adopting an existing paper without restarting it

1. Create a paper metadata workspace with `new`; leave original files in place. Inventory existing code, checkpoints, workbooks and review packets before proposing reruns.
2. Identify the current authoritative manuscript explicitly. Set `state.json`'s `authoritative_manuscript` to a repository-relative path when possible; otherwise record a logical artifact ID and put the machine path only in `.local`. Do not choose by timestamp alone.
3. Add stable artifact IDs and a data dictionary. Register old run records as `historical-unverified` with source pointers; do not pretend the new run tool executed them.
4. Copy only allowed source/code and carefully reviewed metadata into Git. Keep vendor data, model weights and numerical outputs outside it.
5. Reproduce one important exhibit before a larger migration. Distinguish exact reproduction, approximate reconstruction, a deliberate adaptation and a synthetic smoke test.
