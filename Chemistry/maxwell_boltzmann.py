#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

# PDF formula from Wikipedia: https://en.wikipedia.org/wiki/Maxwell–Boltzmann_distribution

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def pdf(x: NDArray[np.float_], a: int) -> NDArray[np.float_]:
    """Returns array of PDF function values given an a value and an array of x values"""
    return (  # type: ignore
        sqrt(2 / np.pi) * (x**2 / a**3) * np.exp(-(x**2) / (2 * a**2))
    )


def plot(ax: Axes) -> None:
    """Plot the PDF of the Maxwell-Boltzmann distribution for various a values"""

    # Store values for a
    a_vals: list[int] = [1, 2, 5]

    # Define domain for each PDF
    x: NDArray[np.float_] = np.linspace(0, 20, 1000)

    # Store PDF function values for each a value using pdf helper function
    pdf_1: NDArray[np.float_] = pdf(x, a_vals[0])
    pdf_2: NDArray[np.float_] = pdf(x, a_vals[1])
    pdf_3: NDArray[np.float_] = pdf(x, a_vals[2])

    # Plot each PDF and create labels containing a values
    ax.plot(x, pdf_1, color="purple", label=f"a = {a_vals[0]}")
    ax.plot(x, pdf_2, color="blue", label=f"a = {a_vals[1]}")
    ax.plot(x, pdf_3, color="green", label=f"a = {a_vals[2]}")

    # Set labels and axis limits
    ax.set_title("PDF of Maxwell-Boltzmann Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability")

    ax.set_xlim(0, 20)
    ax.set_ylim(0, 0.6)

    # Create legend to display previously defined labels for a values
    ax.legend(loc="upper right")

    ax.grid()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())  # Calls plot function
    plt.show()  # Display plot created in plot function


if __name__ == "__main__":
    main()
