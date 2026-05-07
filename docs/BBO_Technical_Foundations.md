# Technical Foundations for the BBO Capstone

## Problem Framing

The capstone challenge is a black-box optimisation problem. Each function accepts a bounded numeric query vector and returns a scalar output, but the underlying formula is hidden. The objective is to maximise each function while using a limited number of queries.

This differs from a conventional supervised learning problem. There is no fixed labelled training set at the start, and the key question is not only "what does the model predict?" but "which point should be tested next?"

## Bayesian Optimisation

Bayesian optimisation is well suited to expensive black-box functions because it uses previous observations to choose informative future observations. The approach has two main components:

- A surrogate model that estimates the unknown response surface.
- An acquisition function that converts predicted value and uncertainty into a candidate-query score.

## Gaussian Process Surrogate Model

A Gaussian Process is useful in this project because the dataset is small and uncertainty matters. For each candidate query, the model estimates:

- Predicted mean: expected output at that point.
- Predicted uncertainty: how uncertain the model is because nearby evidence is limited.

This helps balance local refinement around promising points with exploration of under-sampled regions.

## Acquisition Functions

Expected Improvement prioritises points that are likely to improve on the current best result. It is useful when the current best score is known and the aim is to find a better value efficiently.

Upper Confidence Bound scores each point using predicted mean plus an uncertainty term. It is useful when the project needs a more explicit exploration-exploitation balance.

## Strategy Evolution

The module submissions show a consistent progression:

| Phase | Main behaviour | Reasoning |
| --- | --- | --- |
| Early rounds | Broad exploration | The function shapes were unknown and early overcommitment was risky |
| Middle rounds | Function-specific decisions | Some functions appeared smoother, noisier or more boundary-sensitive than others |
| Later rounds | Controlled local refinement | Query budget became more valuable and promising regions needed careful testing |
| Final reflections | Evidence-based optimisation | The strategy focused on efficient learning, duplicate avoidance and documented assumptions |

## Alternative Methods Considered

SVMs may help if query points are classified into high-performing and low-performing regions. An RBF kernel can represent non-linear boundaries, but SVMs do not naturally provide the same uncertainty estimates as Gaussian Processes.

Neural networks may become useful if the query history grows substantially or if higher-dimensional interactions dominate. For the current small-data setting, they create more overfitting and tuning risk than a Gaussian Process workflow.

## Key Assumptions

- Nearby points often have related outputs.
- Past observations are informative for future query choices.
- Each function should be modelled separately.
- Exploration remains necessary where the evidence is sparse, noisy or inconsistent.

These assumptions should be revisited when new data is added.
