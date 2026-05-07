# Manual Review TODO

These items come from `CAPSTONE_REVIEW_REPORT.md` and could not be completed automatically without external data or programme-specific judgement.

| Item | Status | Required Action |
| --- | --- | --- |
| Add complete final query-response history | Manual input required | Add `data/raw/bbo_query_history.csv` if programme rules allow sharing or local reproduction. |
| Add final best-observed outputs | Pending data | Run the notebook after adding the query history; review `reports/bbo_evaluation_summary.csv`. |
| Add final best-so-far plots | Pending data | Run the notebook after adding the query history; review `figures/best_so_far_by_round.png`. |
| Add output distribution plot | Pending data | Run the notebook after adding the query history; review `figures/output_distribution_by_function.png`. |
| Add final score summary under `reports/` | Pending data | Export or write a concise final result summary once numeric outputs are available. |
| Add presentation deck or link | Manual input required | Add slides or a hosted link to `presentation/README.md` if sharing is permitted. |
| Add submitted query records or rationale | Manual input required | Add files under `queries/` only if allowed by programme rules. |
| Add automated tests | Optional improvement | Add tests for `src/bbo_utils.py` if the repository will be maintained beyond submission. |
| Add synthetic example data | Optional improvement | Only add synthetic data if it is clearly labelled and not confused with challenge results. |

The current repository deliberately avoids fabricated metrics, plots or model artifacts.
