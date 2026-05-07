# Model Card: BBO Gaussian Process Surrogate Workflow

This model card describes the surrogate modelling workflow used to support the Black-Box Optimisation capstone project. It documents the intended use, limitations and evaluation approach for Gaussian Process based Bayesian optimisation in a small-data setting.

## 1. Model Details

- Model name: BBO Gaussian Process surrogate workflow.
- Model type: Regression surrogate for black-box optimisation.
- Algorithm: Gaussian Process regression with acquisition scoring such as Expected Improvement or Upper Confidence Bound.
- Version: Portfolio repository version, May 2026.
- Developed by: Ahmed Elbatran.
- Repository: `https://github.com/AhmedElbtran-ACCA/Capstone-Project-ML-AI-Imperial-College`

## 2. Intended Use

- Primary purpose: Estimate the response surface of each unknown function and support the next query decision.
- Intended users: The project owner, capstone assessors, peers and technical reviewers.
- Intended context: Educational optimisation challenge with bounded numeric inputs and limited query budget.
- Out-of-scope uses: Production automation, high-stakes decision-making, or claiming verified global optima.

## 3. Training Data

- Dataset: BBO query-response log.
- Source: Iterative capstone challenge submissions and returned outputs.
- Training period: Programme period; exact dates are not documented in the repository.
- Training/test split: Not a standard random split. The workflow evaluates sequential improvement and best-so-far performance.
- Key preprocessing steps: Validate query bounds, parse query vectors, separate functions, check duplicates and preserve round order.

## 4. Evaluation Data

- Test dataset: The next unseen query result returned by the challenge system is the practical evaluation signal.
- Evaluation approach: Track best observed output, best-so-far improvement, query efficiency and consistency of local refinements.
- Important subgroups checked: Each black-box function is reviewed separately because dimensionality, smoothness, noise and local structure may differ.

## 5. Metrics

| Metric | Current Repository Value | Why It Matters |
| --- | --- | --- |
| Best observed output by function | Not available until query history is added | Main optimisation objective |
| Best-so-far improvement | Notebook-ready, pending data | Shows whether strategy improves over rounds |
| Query efficiency | Notebook-ready, pending data | Measures improvement under limited query budget |
| Duplicate or near-duplicate checks | Implemented as a recommended review step | Prevents wasting scarce queries |
| Qualitative interpretability | Documented in README and technical notes | Explains why a query was chosen |

## 6. Results Summary

The submitted capstone reflections show a clear strategy evolution: broad exploration in early rounds, per-function refinement in later rounds and a final emphasis on evidence-based local search with controlled exploration. The repository does not yet contain the final numeric query log, so numeric performance claims should be added only after the complete data is available.

## 7. Explainability

- Main drivers of recommendations: Current best observed point, local stability, model-predicted mean, model uncertainty, distance from previous queries and remaining query budget.
- Interpretation method: Best-so-far plots, acquisition scores, per-function summaries and review of local versus exploratory movement.
- Non-technical explanation: The model uses past attempts to estimate where a better result might be found, while keeping track of uncertainty so it does not focus too narrowly too early.

## 8. Limitations

- Data limitations: Sparse observations and incomplete coverage of the search space.
- Model limitations: Gaussian Processes can overfit local patterns, struggle in higher dimensions or misrepresent discontinuous functions.
- Generalisation limits: The workflow is designed for this capstone challenge and similar small-data optimisation tasks.
- Known failure cases: Noisy outputs, narrow ridges, sharp discontinuities, misleading early high scores and excessive concentration around one region.

## 9. Ethical and Responsible Use

- Fairness risks: Low in the educational BBO setting, but real-world optimisation could create unequal impacts depending on the domain.
- Privacy risks: Low if no personal data is added to query notes.
- Human oversight: Required before acting on model recommendations.
- Recommended safeguards: Keep an audit trail, document manual overrides, monitor duplicate distance and avoid unsupported claims of optimality.

## 10. Recommendations

- Use the workflow for: Educational BBO analysis, query history review, surrogate modelling and candidate ranking.
- Do not use the workflow for: Production deployment or high-stakes decisions without domain validation.
- Before deployment: Add complete data, benchmark against random search and simple local-search baselines, and validate stability across functions.
- Future improvements: Trust-region Bayesian optimisation, formal acquisition benchmarking, automated duplicate checks and optional BoTorch or GPyTorch experiments for larger datasets.
