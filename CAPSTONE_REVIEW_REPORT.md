# Capstone Review Report

## Summary of Review Performed

I reviewed the current GitHub repository and compared it against the available capstone-related Word document:

- `README.md`
- `notebooks/BBO_Capstone_Method_and_Results.ipynb`
- `docs/BBO_Capstone_Datasheet.md`
- `docs/BBO_Capstone_Model_Card.md`
- `data/README.md`
- `presentation/README.md`
- `.gitignore`
- `requirements.txt`
- External source document: `C:\Users\ahmed\OneDrive\Desktop\Capstone-Project-ML-AI-Imperial-Cont.docx`

The Word document contains multiple module submissions and reflections for the Black-Box Optimisation capstone. The consistent project story across those submissions is that the capstone is a black-box optimisation challenge involving limited query budgets, unknown functions, exploration-exploitation trade-offs, Gaussian Process/Bayesian optimisation ideas, and iterative strategy refinement.

## Key Consistency Issues Found

1. The repository README was still a generic template with bracketed placeholders rather than a project-specific BBO portfolio README.
2. The notebook described a standard supervised classification workflow using a target column and a random forest classifier. This contradicted the capstone materials, which describe a sequential optimisation task rather than a classification task.
3. The datasheet and model card were also generic templates and did not document the actual query-response dataset, Gaussian Process surrogate workflow, assumptions, or limitations.
4. The repository did not reflect several useful prior module contributions, especially:
   - strategy evolution from broad exploration to controlled local refinement;
   - treating each of the eight functions separately;
   - Gaussian Process modelling and acquisition functions such as Expected Improvement and UCB;
   - SVM and neural network ideas as supporting or future methods;
   - transparency, interpretability, duplicate checking and audit-trail concerns.
5. Some prior module text was duplicated or overlapping, particularly later reflections on exploration-exploitation, PCA-style simplification and reinforcement-learning analogies. These ideas were consolidated rather than copied repeatedly.
6. The final numeric query history, returned outputs, best score table and final plots are not present in the repository, so numeric performance claims could not be verified or added.
7. `requirements.txt` did not explicitly include `scipy`, even though the capstone materials refer to SciPy and the implemented acquisition helpers use it.

## Changes Made to the Repository

- Rewrote `README.md` as a professional portfolio README for the Black-Box Optimisation capstone.
- Reframed the project objective, dataset, methodology, models, metrics, limitations and future work around BBO rather than generic supervised ML.
- Rewrote `notebooks/BBO_Capstone_Method_and_Results.ipynb` into a clean BBO workflow notebook that:
  - loads a local query-response history if available;
  - falls back to a schema template if raw data is absent;
  - validates the workflow without inventing results;
  - supports best-so-far analysis and Gaussian Process candidate ranking once data is added.
- Rewrote `docs/BBO_Capstone_Datasheet.md` to document the BBO query-response log.
- Rewrote `docs/BBO_Capstone_Model_Card.md` for the Gaussian Process surrogate optimisation workflow.
- Added `docs/BBO_Technical_Foundations.md` to capture the technical foundations and strategy evolution from the module submissions.
- Added `src/bbo_utils.py` with reusable helpers for:
  - parsing and formatting query vectors;
  - loading and validating query history;
  - expanding query vectors into numeric feature columns;
  - fitting Gaussian Process surrogate models;
  - scoring candidates with Expected Improvement and UCB;
  - summarising best results by function.
- Added `data/sample/bbo_query_history_template.csv` as a safe schema template.
- Updated `data/README.md` with the expected local data layout and schema.
- Updated `presentation/README.md` with a BBO-specific presentation outline.
- Added repository folders and guidance files for `figures/`, `models/`, `reports/`, and `queries/`.
- Updated `requirements.txt` to include the dependencies needed by the revised workflow.
- Updated `.gitignore` to better protect raw data, processed data, local environments, generated model artifacts and cache files.

No important files were deleted. Generic placeholder files were rewritten in place because they were templates rather than completed project evidence.

## Validation Performed

- `python -m compileall src` passed.
- `python -m json.tool notebooks/BBO_Capstone_Method_and_Results.ipynb` passed, confirming the notebook JSON is valid.
- `git diff --check` passed with only Git line-ending warnings on Windows.
- A scan for the original template placeholders and classifier references found no remaining project-template terms.

Follow-up execution pass:

- A local `.venv` was created and the execution dependencies were installed.
- `pip install -r requirements.txt` completed successfully in the local `.venv`.
- `src/bbo_utils.py` passed a smoke test using a minimal in-memory example.
- `notebooks/BBO_Capstone_Method_and_Results.ipynb` executed successfully with the available empty schema template.
- `scripts/generate_documentation_figures.py` generated the committed documentation figures in `figures/`.
- Data-dependent result figures, score tables and model artifacts remain blocked because `data/raw/bbo_query_history.csv` is not present.

## Recommendations Not Implemented Automatically

- Add the complete final query-response history to `data/raw/bbo_query_history.csv` if programme rules allow it.
- Add final best-observed outputs and best-so-far plots after the query history is available.
- Add a final score summary under `reports/`.
- Add final presentation slides or a shareable presentation link under `presentation/`.
- Add submitted query records or query rationale under `queries/` if sharing is permitted.
- Add automated tests for `src/bbo_utils.py` if the repository will be used as a longer-term technical portfolio.
- Consider adding a small, permitted synthetic example dataset if the real challenge data cannot be shared but reviewers need to see the notebook run through the full modelling path.

## Files That Still Require Manual Review

- `data/raw/bbo_query_history.csv`: missing locally from the repository; needed for final numeric results.
- `reports/`: needs final score tables and exported summaries.
- `figures/`: needs final plots once data is available.
- `presentation/`: needs final slide deck or hosted link.
- `queries/`: optional, but useful if submitted query points can be shared.
- External Word document: contains useful reflection material but should not be copied wholesale into the repository.

## Final Assessment of Repository Readiness

The repository is now structurally aligned with the capstone project and presents a much clearer, more professional BBO portfolio narrative. It is suitable as a cleaned project scaffold and technical documentation base.

It is not yet fully final for assessment or recruiter review because the repository still lacks the actual query-response history, final numeric results, plots and presentation materials. Once those are added, the notebook and documentation are ready to support a complete final review.
