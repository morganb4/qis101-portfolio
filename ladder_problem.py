#!/usr/bin/env python3
"""ladder_problem.py"""

# Calculates the maximum ladder length which will fit around a corner given hall widths.

# Referenced this video:  https://www.youtube.com/watch?v=mWBxCLxNPOI
# Also this article:  https://sites.math.washington.edu//~conroy/m124-general/pipeAroundCorner/pipeAroundCorner.pdf


# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator
from scipy.optimize import minimize  # type: ignore


if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def length(theta: NDArray[np.float_]) -> NDArray[np.float_]:
    """Stores equation for length of the ladder based on theta, given hallway 1
    is 2 meters wide and hallway 2 is 1 meter wide"""
    return 2 / np.sin(theta) + 1 / np.cos(theta)


def plot(ax: Axes) -> None:
    """Plots ladder length as a function of theta and marks local minimum which
    corresponds to the maximum ladder length which can fit around the corner"""

    # Finds min of length function which corresponds to max length to fit around corner
    # Uses 0.90 radians as an estimate for where the graph reaches its min
    max_len: float = minimize(length, 0.90)  # type: ignore

    # Creates array for theta values, with domain +/- 0.5 rad from the minimum
    theta: NDArray[np.float_] = np.linspace(  # type: ignore
        max_len.x - 0.5, max_len.x + 0.5, 100  # type: ignore
    )

    # Stores values of length for each value of theta using length function above
    lengths: NDArray[np.float_] = length(theta)  # type: ignore

    # Plot the length function
    ax.plot(theta, lengths)
    # Mark point where graph reaches local min (point with zero rate of change)
    ax.scatter(
        max_len.x,  # type: ignore
        max_len.fun,  # type: ignore
        color="red",  # type: ignore
        label=f"Max Ladder Length: {max_len.fun:.4f} m",  # type: ignore
        zorder=2,
    )

    # Set title, labels, and tick marks
    ax.set_title("Ladder Length as a Function of Theta")
    ax.set_xlabel(r"$\theta$ (rad)")
    ax.set_ylabel("Ladder Length (m)")
    ax.legend()
    ax.xaxis.set_major_locator(MultipleLocator(0.1))

    # Print maximum ladder length in terminal
    print(f"The maximum ladder length is {max_len.fun:.4f} m.")  # type: ignore


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())  # Call plot function
    plt.show()


if __name__ == "__main__":
    main()
