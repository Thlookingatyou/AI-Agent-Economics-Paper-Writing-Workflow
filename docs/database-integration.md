# Institutional data integration

Use the existing [CSMAR–CNRDS connector](https://github.com/Thlookingatyou/csmar-cnrds-mcp) as a separate installation. The workflow's data-audit skill calls available tools or prepares an exact export request for the researcher. Skills are instructions; they do not establish authentication or expose tools by themselves.

On each device: follow the connector's current setup; establish campus/VPN access in its local browser; verify catalogue/table/field access and an authorized small export. An institution label or catalogue entry does not prove that the needed specialty table is subscribed. Do not copy browser profiles through Git.

Keep raw exports under the configured private-data root. Record provider, table, field codes, Chinese/English labels, query filters, units, date coverage, access restrictions, receipt and checksum. Actual file coverage, keys and missingness must be verified after download. An export receipt is provenance, not proof that the economic measure is valid.

If tools are unavailable, say so and provide an exact manual export request. Do not invent vendor codes, silently use another source, repeat jobs unnecessarily, or claim a connection is verified just because configuration exists. No connector installation or live database query is performed by this repository's doctor/demo/tests.
