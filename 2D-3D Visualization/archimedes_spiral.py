#!/usr/bin/env python3
"""archimedes_spiral.py"""

# Formula for arc length from this website: https://web.ma.utexas.edu/users/m408s/m408d/CurrentWeb/LM10-4-4.php

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def arc_length_inner(r: float) -> float:
    """Contains the inner portion of the polar arc length formula (without integral)"""
    return np.sqrt(r**2 + 1)  # type: ignore


def plot(ax: Axes) -> None:
    """Plots an Archimedes Spiral with formula r = theta"""

    # Contains lower and upper limit of domain
    lower_lim: float = 0
    upper_lim: float = 8 * np.pi

    # Store theta values
    theta: NDArray[np.float_] = np.linspace(lower_lim, upper_lim, 1000)
    # Store radius as a function of theta
    radius: NDArray[np.float_] = theta

    # Calculate arc length using Scipy integrate
    arc_length: float = scipy.integrate.quad(  # type: ignore
        arc_length_inner, lower_lim, upper_lim
    )[0]

    # Draw Archimedes spiral
    ax.plot(theta, radius)
    # Set aspect ratio
    ax.set_aspect("equal")
    # Set plot title
    ax.set_title(f"Archimedes Spiral, Arc Length = {arc_length:.2f}")
    # Print arc length in terminal
    print(f"Arc Length: {arc_length:.2f}")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes(projection="polar"))  # Calls plot function with polar projection
    plt.show()  # Display plot created in plot function


if __name__ == "__main__":
    main()
