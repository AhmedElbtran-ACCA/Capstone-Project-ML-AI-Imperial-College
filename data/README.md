# Data Access Notes

The capstone data is an iterative query-response log from the Black-Box Optimisation challenge. The raw data is not committed because it may be assessment-specific or restricted.

## Expected Dataset

- Dataset name: BBO query-response log.
- Source: Capstone challenge submissions and returned outputs.
- Public link: Not publicly documented.
- Licence or access terms: Subject to the programme and assessment rules.
- File format: CSV.
- Expected local path: `data/raw/bbo_query_history.csv`.

## Expected Columns

| Column | Description |
| --- | --- |
| `function_id` | Identifier for one of the eight unknown functions |
| `round` | Query round or iteration number |
| `query` | Hyphen-separated query vector, for example `0.123456-0.654321` |
| `output` | Returned scalar output value |
| `notes` | Optional reasoning or context |

Use `data/sample/bbo_query_history_template.csv` as the schema template.

## Local File Layout

```text
data/
  raw/          # Local raw query history, not committed
  processed/    # Local cleaned files, not committed
  sample/       # Small shareable schema or permitted sample
```

## Reproducibility Notes

1. Export or assemble the query-response log as a CSV.
2. Save it locally as `data/raw/bbo_query_history.csv`.
3. Run `notebooks/BBO_Capstone_Method_and_Results.ipynb`.
4. Commit only permitted summaries, figures or anonymised samples.
