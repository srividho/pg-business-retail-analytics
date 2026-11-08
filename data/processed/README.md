# Processed data

This directory contains generated analytical outputs and the SQLite database.

Expected generated files include:
- `fmcg_analyzed.csv`
- `pg_analytics.db`

The database contains tables used by the SQL analysis, including `pg_financials` and `fmcg_retail`.

Regenerate these files from the source datasets using the Python scripts in `src/`. Run commands from the project root and follow the setup instructions in the main README.

Processed files are excluded from Git to avoid committing generated databases and potentially large data files. The scripts and SQL queries are intended to document the analysis workflow.
