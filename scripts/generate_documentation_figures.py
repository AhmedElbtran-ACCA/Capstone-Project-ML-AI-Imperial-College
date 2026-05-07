"""Generate non-numeric documentation figures for the BBO capstone repository."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = PROJECT_ROOT / "figures"
FIGURES_DIR.mkdir(exist_ok=True)

FONT = "DejaVu Sans"
COLORS = {
    "blue": "#2F5D8C",
    "green": "#3C7D5A",
    "amber": "#B8832D",
    "red": "#A64646",
    "ink": "#232323",
    "line": "#5B6670",
    "panel": "#F7F8FA",
}


def add_box(ax, x, y, text, color, width=2.55, height=0.86):
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.03,rounding_size=0.06",
        linewidth=1.4,
        edgecolor=color,
        facecolor="#FFFFFF",
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=10.5,
        color=COLORS["ink"],
        fontname=FONT,
        wrap=True,
    )


def add_arrow(ax, start, end):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=1.4,
        color=COLORS["line"],
    )
    ax.add_patch(arrow)


def workflow_figure():
    fig, ax = plt.subplots(figsize=(13.8, 4.8))
    ax.set_xlim(0, 13.4)
    ax.set_ylim(0, 4.2)
    ax.axis("off")

    ax.text(
        0,
        3.95,
        "Black-Box Optimisation Workflow",
        fontsize=18,
        fontweight="bold",
        color=COLORS["ink"],
        fontname=FONT,
    )
    ax.text(
        0,
        3.55,
        "Conceptual workflow based on the capstone documentation; numeric result plots require the final query history.",
        fontsize=10.5,
        color=COLORS["line"],
        fontname=FONT,
    )

    boxes = [
        (0.15, 2.2, "Query-response\nhistory", COLORS["blue"]),
        (2.75, 2.2, "Per-function\nsurrogate update", COLORS["green"]),
        (5.35, 2.2, "Acquisition\nscoring", COLORS["amber"]),
        (7.95, 2.2, "Candidate query\nselection", COLORS["red"]),
        (10.55, 2.2, "Returned output\nfrom challenge", COLORS["blue"]),
        (5.35, 0.75, "Audit trail:\nround, rationale,\nmanual overrides", COLORS["green"]),
    ]
    for box in boxes:
        add_box(ax, *box)

    add_arrow(ax, (2.70, 2.63), (2.75, 2.63))
    add_arrow(ax, (5.30, 2.63), (5.35, 2.63))
    add_arrow(ax, (7.90, 2.63), (7.95, 2.63))
    add_arrow(ax, (10.50, 2.63), (10.55, 2.63))
    add_arrow(ax, (11.85, 2.15), (6.7, 1.62))
    add_arrow(ax, (5.35, 1.18), (1.45, 2.17))

    fig.tight_layout()
    output = FIGURES_DIR / "bbo_workflow.png"
    fig.savefig(output, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output


def strategy_evolution_figure():
    stages = [
        ("Early rounds", "Broad exploration\nto map unknown space", COLORS["blue"]),
        ("Middle rounds", "Function-specific\nrefinement", COLORS["green"]),
        ("Later rounds", "GP-guided\ncandidate ranking", COLORS["amber"]),
        ("Final reflection", "Controlled local search\nwith audit trail", COLORS["red"]),
    ]

    fig, ax = plt.subplots(figsize=(13, 4.8))
    ax.set_xlim(-0.5, len(stages) - 0.5)
    ax.set_ylim(0, 2.7)
    ax.axis("off")

    ax.text(
        -0.45,
        2.45,
        "Strategy Evolution Across Capstone Rounds",
        fontsize=18,
        fontweight="bold",
        color=COLORS["ink"],
        fontname=FONT,
    )
    ax.text(
        -0.45,
        2.15,
        "A qualitative summary consolidated from the submitted module reflections.",
        fontsize=10.5,
        color=COLORS["line"],
        fontname=FONT,
    )

    ax.plot([0, len(stages) - 1], [1.25, 1.25], color=COLORS["line"], linewidth=1.4)
    for index, (label, detail, color) in enumerate(stages):
        ax.scatter(index, 1.25, s=260, color=color, zorder=3)
        ax.text(
            index,
            1.68,
            label,
            ha="center",
            va="bottom",
            fontsize=11.5,
            fontweight="bold",
            color=COLORS["ink"],
            fontname=FONT,
        )
        ax.text(
            index,
            0.64,
            detail,
            ha="center",
            va="top",
            fontsize=10.5,
            color=COLORS["ink"],
            fontname=FONT,
        )

    fig.tight_layout()
    output = FIGURES_DIR / "bbo_strategy_evolution.png"
    fig.savefig(output, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output


def main():
    outputs = [workflow_figure(), strategy_evolution_figure()]
    for output in outputs:
        print(f"Saved {output.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
