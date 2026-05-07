"""Reusable helpers for the Black-Box Optimisation capstone workflow."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel


REQUIRED_COLUMNS = ("function_id", "round", "query", "output")


def parse_query_vector(query: str | Iterable[float]) -> np.ndarray:
    """Parse and validate a query vector with values in the interval [0, 1]."""
    if isinstance(query, str):
        query = query.strip()
        if query.startswith("-") or query.endswith("-") or "--" in query:
            raise ValueError("Query strings must use hyphens only as separators.")
        values = [float(part) for part in query.split("-") if part != ""]
    else:
        values = [float(value) for value in query]

    vector = np.asarray(values, dtype=float)
    if vector.size == 0:
        raise ValueError("Query vector is empty.")
    if not np.all(np.isfinite(vector)):
        raise ValueError("Query vector contains non-finite values.")
    if np.any((vector < 0) | (vector > 1)):
        raise ValueError("Query vector values must be between 0 and 1.")
    return vector


def format_query_vector(values: Iterable[float]) -> str:
    """Format a numeric query vector for the challenge portal."""
    vector = parse_query_vector(values)
    return "-".join(f"{value:.6f}" for value in vector)


def expand_query_vectors(df: pd.DataFrame, query_column: str = "query") -> pd.DataFrame:
    """Return a copy of the data with parsed query values expanded into x columns."""
    expanded = df.copy()
    vectors = [parse_query_vector(query) for query in expanded[query_column]]
    dimensions = {vector.size for vector in vectors}
    if len(dimensions) != 1:
        raise ValueError("All query vectors in one modelling table must have the same dimension.")

    matrix = np.vstack(vectors)
    for idx in range(matrix.shape[1]):
        expanded[f"x{idx}"] = matrix[:, idx]
    return expanded


def load_query_history(path: str | Path) -> pd.DataFrame:
    """Load and validate a BBO query-response CSV."""
    df = pd.read_csv(path)
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if df.empty:
        return df

    df = df.copy()
    df["round"] = pd.to_numeric(df["round"], errors="raise").astype(int)
    df["output"] = pd.to_numeric(df["output"], errors="raise")
    return expand_query_vectors(df)


def fit_gp_surrogate(
    function_df: pd.DataFrame,
    alpha: float = 1e-6,
    random_state: int = 42,
) -> tuple[GaussianProcessRegressor, np.ndarray, np.ndarray]:
    """Fit a Gaussian Process surrogate for one black-box function."""
    feature_columns = sorted(
        [column for column in function_df.columns if column.startswith("x")],
        key=lambda column: int(column[1:]),
    )
    if not feature_columns:
        function_df = expand_query_vectors(function_df)
        feature_columns = sorted(
            [column for column in function_df.columns if column.startswith("x")],
            key=lambda column: int(column[1:]),
        )

    if len(function_df) < 2:
        raise ValueError("At least two observations are required to fit a surrogate model.")

    x_train = function_df[feature_columns].to_numpy(dtype=float)
    y_train = function_df["output"].to_numpy(dtype=float)

    kernel = ConstantKernel(1.0, constant_value_bounds=(1e-3, 1e3)) * Matern(
        length_scale=np.ones(x_train.shape[1]),
        length_scale_bounds=(1e-2, 1e2),
        nu=2.5,
    ) + WhiteKernel(noise_level=alpha, noise_level_bounds=(1e-8, 1e-1))

    model = GaussianProcessRegressor(
        kernel=kernel,
        normalize_y=True,
        random_state=random_state,
        n_restarts_optimizer=3,
    )
    model.fit(x_train, y_train)
    return model, x_train, y_train


def generate_candidate_points(
    dimensions: int,
    n_candidates: int = 5000,
    random_state: int = 42,
) -> np.ndarray:
    """Generate bounded random candidate points for acquisition scoring."""
    if dimensions < 1:
        raise ValueError("dimensions must be at least 1.")
    rng = np.random.default_rng(random_state)
    return rng.random((n_candidates, dimensions))


def expected_improvement(
    model: GaussianProcessRegressor,
    candidates: np.ndarray,
    best_y: float,
    xi: float = 0.01,
) -> np.ndarray:
    """Compute Expected Improvement scores for candidate query points."""
    mean, std = model.predict(candidates, return_std=True)
    std = np.maximum(std, 1e-12)
    improvement = mean - best_y - xi
    z_score = improvement / std
    return improvement * norm.cdf(z_score) + std * norm.pdf(z_score)


def upper_confidence_bound(
    model: GaussianProcessRegressor,
    candidates: np.ndarray,
    kappa: float = 2.0,
) -> np.ndarray:
    """Compute Upper Confidence Bound scores for candidate query points."""
    mean, std = model.predict(candidates, return_std=True)
    return mean + kappa * std


def recommend_candidates(
    model: GaussianProcessRegressor,
    dimensions: int,
    acquisition: str = "ei",
    best_y: float | None = None,
    n_candidates: int = 5000,
    top_k: int = 5,
    random_state: int = 42,
) -> pd.DataFrame:
    """Rank random candidate points using EI or UCB acquisition scoring."""
    candidates = generate_candidate_points(dimensions, n_candidates, random_state)

    if acquisition == "ei":
        if best_y is None:
            raise ValueError("best_y is required for Expected Improvement.")
        scores = expected_improvement(model, candidates, best_y=best_y)
    elif acquisition == "ucb":
        scores = upper_confidence_bound(model, candidates)
    else:
        raise ValueError("acquisition must be either 'ei' or 'ucb'.")

    mean, std = model.predict(candidates, return_std=True)
    ranked_idx = np.argsort(scores)[::-1][:top_k]
    ranked = candidates[ranked_idx]
    return pd.DataFrame(
        {
            "query": [format_query_vector(row) for row in ranked],
            "acquisition": acquisition,
            "score": scores[ranked_idx],
            "predicted_mean": mean[ranked_idx],
            "predicted_std": std[ranked_idx],
        }
    )


def summarise_best_by_function(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise the best observed output for each black-box function."""
    if df.empty:
        return pd.DataFrame(columns=["function_id", "round", "query", "output"])

    best_idx = df.groupby("function_id")["output"].idxmax()
    return (
        df.loc[best_idx, ["function_id", "round", "query", "output"]]
        .sort_values("function_id")
        .reset_index(drop=True)
    )
