# Consistency Check

## Scope

Checked consistency between:

- `README.md`
- `notebooks/BBO_Capstone_Method_and_Results.ipynb`
- `docs/BBO_Capstone_Datasheet.md`
- `docs/BBO_Capstone_Model_Card.md`
- `docs/BBO_Technical_Foundations.md`
- `figures/README.md`
- `models/README.md`
- `reports/REPRODUCIBILITY_STATUS.md`

## Findings

| Area | Status | Notes |
| --- | --- | --- |
| Project objective | Consistent | Repository consistently describes a black-box optimisation task, not a supervised classification task. |
| Dataset description | Consistent with limitation | All docs identify the missing raw query-response history as the blocker for numeric results. |
| Methodology | Consistent | Gaussian Process surrogate modelling and acquisition scoring are described as the main reproducible approach. |
| Evaluation metrics | Consistent | README and notebook use optimisation metrics such as best-so-far improvement, not classification accuracy. |
| Figures | Consistent | Committed figures are labelled as documentation visuals; result plots are marked pending data. |
| Model artifacts | Consistent | No fitted model is claimed or committed because no raw query history is present. |
| Reports | Consistent | Reports explain what ran, what was generated and what remains blocked. |

## Contradictions or Mismatches

No direct contradictions were found after the update. The main unresolved gap is the absence of the final numeric query-response history, which prevents generation of real performance figures, final metrics and reproducible fitted model artifacts.

## Naming Conventions

Current naming is standardised around:

- `bbo_` prefix for repository-level BBO outputs.
- lowercase, underscore-separated generated filenames.
- `data/raw/bbo_query_history.csv` as the canonical local data path.
- `figures/` for image outputs and `reports/` for table/report outputs.
