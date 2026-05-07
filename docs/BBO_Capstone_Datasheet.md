# Datasheet: BBO Query-Response Log

This datasheet documents the dataset used in the Black-Box Optimisation capstone project. The raw challenge data is not committed to the repository; only a schema template is provided in `data/sample/`.

## 1. Motivation

- Dataset name: BBO query-response log.
- Created by: Query submissions made during the Imperial College ML and AI capstone challenge, with outputs returned by the challenge system.
- Used for: Modelling unknown black-box functions and selecting future query points.
- Intended audience: Assessors, peers, recruiters and technical reviewers who need to understand the optimisation workflow.

## 2. Composition

- Number of records: Not committed. The capstone reflections mention the dataset growing from early rounds to 18 or more observations per function.
- Number of functions: Eight unknown black-box functions.
- Target variable: `output`, the returned scalar function value.
- Feature types: Numeric query vector values between 0 and 1.
- Unit of observation: One query submitted for one function in one round.
- Expected columns: `function_id`, `round`, `query`, `output`, `notes`.
- Missing data: Missing outputs should be treated as incomplete submissions and excluded from modelling until resolved.
- Sensitive or personal data: No personal data is expected in the query-response log.

## 3. Collection Process

- Original source: The capstone challenge portal or submission workflow.
- Collection method: Iterative query submissions; one output is observed after each submitted query.
- Collection date range: Programme period; exact dates are not documented in the repository.
- Sampling method: Adaptive sampling based on previous outputs, uncertainty, local refinement and exploration-exploitation judgement.
- Consent and permissions: The query history should only be shared if permitted by the programme and assessment rules.

## 4. Preprocessing

- Removed records: Remove duplicate records, invalid queries and rows without returned outputs.
- Missing-value handling: Do not impute missing outputs for model fitting; treat them as unresolved observations.
- Outlier handling: Retain unusual outputs for review because they may indicate real high-performing regions, noise or discontinuities.
- Feature engineering: Parse each hyphen-separated query into numeric feature columns such as `x0`, `x1`, `x2`.
- Encoding or scaling: Query values are already bounded between 0 and 1; no categorical encoding is required for the core query vector.
- Train/test split: A random split is not the primary evaluation method because this is a sequential optimisation problem. Use chronological analysis and best-so-far metrics.

## 5. Recommended Uses

- Appropriate uses: Reconstructing query decisions, fitting surrogate models, comparing acquisition strategies and visualising best-so-far improvement.
- Inappropriate uses: Claiming global optimality, making high-stakes decisions, or reporting final numeric performance without the complete query history.
- Users who may benefit: Students, reviewers and practitioners interested in small-data optimisation under uncertainty.

## 6. Limitations and Bias

- Known limitations: Sparse observations, limited query budget and incomplete coverage of high-dimensional search spaces.
- Potential sources of bias: Later queries are concentrated around regions that looked promising earlier, so the dataset reflects the search strategy as well as the function behaviour.
- Under-represented cases: Under-sampled regions, boundary combinations not tested, and higher-dimensional interactions.
- Impact on model results: Surrogate models may overfit local patterns, understate uncertainty or miss narrow optima.

## 7. Distribution and Maintenance

- Is the dataset stored in this repository? No raw dataset is committed. A schema template is included.
- External data link: Not publicly documented.
- Licence or terms of use: Subject to the capstone programme and challenge rules.
- Maintainer: Ahmed Elbatran.
- Update plan: Add the final query history locally under `data/raw/` if sharing is permitted; commit only allowed summaries or anonymised samples.

## 8. Ethical Considerations

- Privacy risks: Low, provided no personal identifiers are added to the query notes.
- Fairness risks: Low for the capstone challenge itself; real-world BBO applications would require domain-specific fairness review.
- Security risks: Avoid publishing restricted challenge data, credentials or private assessment materials.
- Human oversight required: A reviewer should validate model recommendations before any query submission or real-world deployment.

## 9. Contact

- Project owner: Ahmed Elbatran.
- Repository: `https://github.com/AhmedElbtran-ACCA/Capstone-Project-ML-AI-Imperial-College`
