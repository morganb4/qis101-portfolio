#!/usr/bin/env python3
"""random_walk_gamma.py"""


from __future__ import annotations

import typing

# Import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

# Import gamma function from scipy
from scipy.special import gamma  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def mean_distance(dimension: float) -> float:
    """Calculates mean distance for given dimension using Gamma function"""
    return (2 / dimension) * (  # type: ignore
        gamma((dimension + 1) / 2) / gamma(dimension / 2)
    ) ** 2  # type: ignore


def plot(ax: Axes) -> None:
    """Create line plot of expected final dist of uniform random walks on unit lattice
    with varying dimensions"""

    # Array to store dimension values
    d: NDArray[np.float_] = np.linspace(1, 25, 1000)

    # Array to store expected final distances
    y: NDArray[np.float_] = mean_distance(d)  # type: ignore

    # Plot d and y values
    ax.plot(d, y)
    # Reset y axis limits to improve readability of plot
    plt.ylim(0.6, 1.0)

    # Set title and labels
    ax.set_title(
        "Expected Final Distance of Uniform Random Walk on Unit Lattice vs Dimension"
    )
    ax.set_xlabel("Dimension (d)")
    ax.set_ylabel("Expected Final Distance")
    ax.grid()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())  # Calls plot function
    plt.show()  # Displays plot


if __name__ == "__main__":
    main()
