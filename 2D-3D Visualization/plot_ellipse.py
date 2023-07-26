#!/usr/bin/env python3
"""plot_ellipse.py"""

from __future__ import annotations

import typing

# Import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot an ellipse"""

    # Set major and minor axis of the ellipse
    maj_ax: float = 100.0
    min_ax: float = 50.0

    # Create an array for theta
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 1000)

    # Create an array for the radius at each value for theta
    radius: NDArray[np.float_] = (maj_ax * min_ax) / np.sqrt(
        (maj_ax**2 - min_ax**2) * (np.sin(theta)) ** 2 + min_ax**2
    )

    # Create arrays for x and y (Cartesian)
    x: NDArray[np.float_] = radius * np.cos(theta)
    y: NDArray[np.float_] = radius * np.sin(theta)

    # Plot x and y values
    ax.plot(x, y)

    # Change scale of y-axis to improve readability
    ax.set_ylim(-60, 60)

    # Set titles and labels
    ax.set_title(f"$x^2/{maj_ax}^2 + y^2/{min_ax}^2 = 1$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Add grid and axis lines
    ax.grid()
    ax.axhline(0, color="red")
    ax.axvline(0, color="red")

    # Set aspect ratio
    ax.set_aspect("equal")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    # Display plot on screen
    plt.show()


if __name__ == "__main__":
    main()
