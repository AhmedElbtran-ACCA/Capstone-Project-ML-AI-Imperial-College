# Reproducibility Status

## Execution Summary

This report records the latest repository execution pass.

| Item | Status | Notes |
| --- | --- | --- |
| Repository structure inspected | Complete | No `initial/` folder or separate original-code module was found. |
| Dependency installation | Complete | `pip install -r requirements.txt` completed successfully in the local `.venv`. |
| Python utility module | Complete | `src/bbo_utils.py` compiled successfully and passed a smoke test using a minimal in-memory example. |
| Notebook execution | Complete | `notebooks/BBO_Capstone_Method_and_Results.ipynb` executed successfully with the available schema template. |
| Documentation figure generation | Complete | `scripts/generate_documentation_figures.py` generated two high-resolution PNG figures. |
| Data-dependent result figures | Blocked | `data/raw/bbo_query_history.csv` is not present. |
| Model artifact generation | Blocked | No raw query history is available, so no fitted model artifact can be reproduced. |
| Final metrics and score tables | Blocked | Numeric results require the final query-response history. |

## Executed Commands

```bash
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m compileall src
.venv\Scripts\python scripts\generate_documentation_figures.py
.venv\Scripts\python -m nbconvert --to notebook --execute notebooks\BBO_Capstone_Method_and_Results.ipynb --inplace --ExecutePreprocessor.timeout=180
```

`src/bbo_utils.py` was also smoke-tested with a minimal in-memory query history to validate query parsing, Gaussian Process fitting and candidate recommendation.

The notebook execution completed without runtime errors. It correctly skipped modelling, evaluation and result plotting because the query history file is absent.

## Generated Figures

| Figure | Source | Status |
| --- | --- | --- |
| `figures/bbo_workflow.png` | `scripts/generate_documentation_figures.py` | Generated |
| `figures/bbo_strategy_evolution.png` | `scripts/generate_documentation_figures.py` | Generated |
| `figures/best_so_far_by_round.png` | Notebook section 4 | Pending data |
| `figures/output_distribution_by_function.png` | Notebook section 4 | Pending data |

## Generated Model Artifacts

None. This is intentional until the final query-response history is available.

## Dependency Notes

The initial active Python environment did not have `pandas` or `jupyter` available. A local `.venv` was created and the execution dependencies were installed there. The project `requirements.txt` now includes `nbconvert` and `ipykernel` for command-line notebook execution.

## Current Blocking Item

To complete numeric results, add the permitted final query history file:

```text
data/raw/bbo_query_history.csv
```

Expected columns:

```text
function_id,round,query,output,notes
```
