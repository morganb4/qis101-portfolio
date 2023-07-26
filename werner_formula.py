#!/usr/bin/env python3
"""werner_formula.py"""

# Found code to set tick marks at multiples of pi (using pi character) here:
# https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib

# Werner's formula from Wikipedia: https://en.wikipedia.org/wiki/Prosthaphaeresis

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Plot two sine waves and their product using direct multiplication as well as
    Werner's Product-to-Sum Formula"""

    # Create x domain in the interval [-3 * pi, 3 * pi]
    x: NDArray[np.float_] = np.linspace(-3 * np.pi, 3 * np.pi, 100)
    # Create two new arrays containing wave number times x for each sinusoid
    a: NDArray[np.float_] = 0.8 * x
    b: NDArray[np.float_] = 0.5 * x

    # Pass a and b arrays into separate sine functions
    f1: NDArray[np.float_] = np.sin(a)
    f2: NDArray[np.float_] = np.sin(b)

    # Calculate the product of both sine functions and store as new array
    f3: NDArray[np.float_] = f1 * f2

    # Calculate the product of the sine functions using Werner's Product-to-Sum formula
    f4: NDArray[np.float_] = (np.cos(a - b) - np.cos(a + b)) / 2

    # Plot all four function arrays in different colors with LaTeX labels
    ax.plot(x, f1, color="red", linewidth=2, label=r"$f_1(x) = sin(0.8x)$")
    ax.plot(x, f2, color="blue", linewidth=2, label=r"$f_2(x) = sin(0.5x)$")
    ax.plot(x, f3, color="orange", linewidth=2, label=r"$f_1(x) * f_2(x)$")
    ax.plot(
        x,
        f4,
        color="None",
        marker="o",  # Plot f4 using open circles
        mec="black",  # Set marker edge color
        mfc="None",  # Set marker fill/face color
        ms=5,  # Set marker size
        label=r"Werner $f_1(x) * f_2(x)$",
    )

    # Set axis lines
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    # Set x axis limits, and set tick marks to be multiples of 3 * pi
    ax.set_xlim(-3 * np.pi, 3 * np.pi)
    ax.xaxis.set_major_formatter(tck.FormatStrFormatter(r"%g$\pi$"))
    ax.xaxis.set_major_locator(tck.MultipleLocator(3))
    ax.xaxis.set_minor_locator(tck.AutoMinorLocator())

    # Set title and labels
    ax.set_title(
        "Superposition of Two Sine Waves Using Werner's Product-to-Sum Formula"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
