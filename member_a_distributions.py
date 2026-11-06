"""Descriptive plots of the supplied smoking data (Member A)."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

DATA_PATH = Path("data/smoking_data.csv")


def load_data(path: str | Path = DATA_PATH) -> pd.DataFrame:
    """Read the supplied raw data; do not alter the team's cleaning choices."""
    return pd.read_csv(path)


def plot_numeric_distributions(data: pd.DataFrame) -> Figure:
    """Plot age and observed salary, stating the available sample size."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for ax, column, label, bins in (
        (axes[0], "age", "Age (years)", range(15, 91, 5)),
        (axes[1], "salary", "Salary (units unspecified)", 20),
    ):
        values = data[column].dropna()
        ax.hist(values, bins=bins, color="#31788e", edgecolor="white")
        ax.set_title(f"{label}\nObserved: {len(values):,} / {len(data):,}")
        ax.set_xlabel(label)
        ax.set_ylabel("Number of people")
        ax.grid(axis="y", alpha=0.2)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle("Age and salary distributions", fontsize=15, fontweight="bold")
    fig.tight_layout()
    return fig


def plot_categorical_distributions(data: pd.DataFrame) -> Figure:
    """Show counts and percentages of all rows, including missing categories."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.5))
    for ax, column, title in zip(
        axes, ("smoker", "outcome", "gender"),
        ("Smoking status", "Outcome", "Gender"),
    ):
        counts = data[column].fillna("Missing").value_counts()
        bars = ax.bar(counts.index.astype(str), counts.values, color="#cd7559")
        ax.bar_label(
            bars,
            labels=[f"{n:,}\n({n / len(data):.1%})" for n in counts],
            padding=3,
        )
        ax.set_ylim(0, max(counts.max() * 1.2, 1))
        ax.set_title(title)
        ax.set_ylabel("Number of people")
        ax.grid(axis="y", alpha=0.2)
        ax.set_axisbelow(True)
        ax.spines[["top", "right"]].set_visible(False)
    fig.suptitle(
        f"Sample composition (n = {len(data):,})", fontsize=15, fontweight="bold"
    )
    fig.tight_layout()
    return fig


def save_figures(data: pd.DataFrame, directory: str | Path = "figures") -> None:
    """Save the two figures separately from notebook output stripping."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    for name, figure in (
        ("member_a_numeric_distributions.png", plot_numeric_distributions(data)),
        ("member_a_categorical_distributions.png", plot_categorical_distributions(data)),
    ):
        figure.savefig(directory / name, dpi=180, bbox_inches="tight")
        plt.close(figure)


if __name__ == "__main__":
    save_figures(load_data())
