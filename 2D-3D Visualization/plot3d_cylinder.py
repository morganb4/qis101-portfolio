#!/usr/bin/env python3
"""plot3d_cylinder.py"""

# Referenced this video: https://www.youtube.com/watch?v=2f2wStPr3PY

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot a wireframe cylinder with unit radius and height 2 centered at (0,0,0)"""

    # Radius of cylinder
    radius: int = 1

    # Theta to sweep around the cylinder walls
    theta: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 100)

    # Set range for z values (height of the cylinder)
    z_range: NDArray[np.float_] = np.linspace(-1, 1, 100)

    # Calculate x and y values using cylindrical -> Cartesian coordinate conversion
    x: NDArray[np.float_] = radius * np.cos(theta)  # type: ignore
    y: NDArray[np.float_] = radius * np.sin(theta)  # type: ignore

    # Using meshgrid, create array of z values which holds a z value corresponding to
    # each theta for each z in z_range
    z: NDArray[np.float_]
    _: NDArray[np.float_]
    _, z = np.meshgrid(theta, z_range)

    # Set axis labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    # Plot the wireframe cylinder
    ax.plot_wireframe(x, y, z)  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))  # Set matplotlib projection to 3d
    plt.show()


if __name__ == "__main__":
    main()
