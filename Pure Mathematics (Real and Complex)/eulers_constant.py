#!/usr/bin/env python3
"""eulers_constant.py"""

# Numerically estimates Euler's constant and plots a line graph of
# (Euler's constant + ln(x)) over a step plot of the first 50 harmonic numbers
# Harmonic number formula from https://mathworld.wolfram.com/HarmonicNumber.html

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate  # type: ignore
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def eul_function(x: float) -> float:
    """Contains the inner portion of the integral to estimate Euler's Constant"""
    return np.emath.log(np.emath.log(1 / x))  # type: ignore


def plot(ax: Axes) -> None:
    """Plots Euler's constant + ln(x) over step plot of first 50 Harmonic Numbers"""

    # Store and print estimate for Euler's Constant
    eul_constant: float = -scipy.integrate.quad(eul_function, 0, 1)[0]  # type: ignore
    print(f"Estimate for Euler's Constant: {eul_constant}")

    # Stores array of first 50 natural numbers
    nat_numbers: NDArray[np.float_] = np.linspace(1, 50, 50)
    # Creates empty array for Harmonic Numbers
    harmonic_numbers: NDArray[np.float_] = np.asarray([])
    sum: float = 0  # Initializes variable sum to calculate Harmonic Numbers
    for i in nat_numbers:
        sum += 1 / i  # Add reciprocals of natural numbers to calculate Harmonic Numbers
        # Append Harmonic Numbers to harmonic_numbers array
        harmonic_numbers = np.append(harmonic_numbers, sum)

    # Create step plot of first 50 Harmonic Numbers
    plt.step(nat_numbers, harmonic_numbers, label="Harmonic Numbers")

    # Create domain and range for graph of Euler's Constant + ln(x)
    eul_x: NDArray[np.float_] = np.linspace(1, 50, 1000)
    eul_y: NDArray[np.float_] = eul_constant + np.emath.log(eul_x)  # type: ignore

    # Plot Euler's Constant + ln(x)
    ax.plot(eul_x, eul_y, label=r"$y = \gamma + ln(x)$")

    # Set axis limits and tick marks
    ax.set_ylim(1)
    ax.xaxis.set_major_locator(MultipleLocator(5))

    # Set titles and labels
    ax.set_title(r"$y = \gamma + ln(x)$ and Harmonic Numbers, $n = [1, 50]$")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())  # Call plot function
    plt.show()


if __name__ == "__main__":
    main()
