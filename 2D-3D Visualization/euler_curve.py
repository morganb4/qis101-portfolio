#!/usr/bin/env python3
"""euler_curve.py"""


# Formula for arc length (arc length == t) from Wikipedia: https://en.wikipedia.org/wiki/Fresnel_integral

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def x_integrand(u: float) -> float:
    """Integrand for the parametric function x(t)"""
    return np.cos(u**2)  # type: ignore


def y_integrand(u: float) -> float:
    """Integrand for the parametric function y(t)"""
    return np.sin(u**2)  # type: ignore


def plot(ax: Axes) -> None:
    """Plots the Euler curve in the interval [0, 12.34) as well as the point at the
    limit as t goes to infinity. Displays the arc length along the curve."""

    # Store upper and lower limit for t
    lower_lim: float = 0
    upper_lim: float = 12.34

    # Array of t values
    t: NDArray[np.float_] = np.linspace(lower_lim, upper_lim, 1000, endpoint=False)

    # Initialize arrays for x and y values
    x_vals: NDArray[np.float_] = np.array([])
    y_vals: NDArray[np.float_] = np.array([])
    # Iterate through t values to calculate x and y values based on the parametric
    # equations
    for t in t:
        x_vals = np.append(
            x_vals, scipy.integrate.quad(x_integrand, 0, t)[0]  # type: ignore
        )
        y_vals = np.append(
            y_vals, scipy.integrate.quad(y_integrand, 0, t)[0]  # type: ignore
        )

    # Plot Euler's curve using calculated x and y values
    ax.plot(x_vals, y_vals)

    # Plot point at the limit as t -> infinity (cannot use quad because sin and cos
    # are oscillatory functions)
    x_inf_lim: float = np.sqrt(np.pi / 2) / 2
    y_inf_lim: float = x_inf_lim

    # Plot the point at the limit as t -> infinity
    ax.scatter(
        x_inf_lim, y_inf_lim, color="red", label=r"$(x, y)$ limit as $t\to\infty$"
    )

    # Set title and axis labels, display arc length based on formula arc length == t
    ax.set_title(rf"Euler's Curve ($0 \leq t < 12.34$), Arc length = {upper_lim}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    ax.set_aspect("equal")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
