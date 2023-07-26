#!/usr/bin/env python3
"""benfords_law.py"""

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import random

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """Demonstrates Benford's Law by displaying histogram of most significant digit
    probabilities for 100,000 very large random integers"""

    # Contains the total number of integers to be generated
    num_rand_int: int = 100_000

    # Generates random integers between 1 and 1_000_000 and raises them to 100th power
    # Stores random ints as strings in order to find the most significant digit
    rand_ints_strings: list[str] = [
        str(random.randint(1, 1_000_000) ** 100) for _ in range(0, num_rand_int + 1)
    ]

    # Creates list of the most significant digit of every number using array slicing
    # Converts most significant digits to integers
    msd_list: list[int] = [
        int(rand_ints_strings[i][:1:]) for i in range(len(rand_ints_strings))
    ]

    # Stores values 1-9 for x-axis of bar chart
    possible_msd: NDArray[np.int_] = np.arange(1, 10)
    # Calculates probability for each MSD by counting each MSD in msd_list
    probabilities: NDArray[np.float_] = np.asarray(
        [msd_list.count(i) / num_rand_int for i in range(1, 10)]
    )

    # Plots bar graph of probability (y-axis) vs MSD (x-axis)
    plt.bar(possible_msd, probabilities, zorder=2)

    # Set labels and tick marks for bar chart
    ax.set_title(
        (
            f"Benford's Law for Randomly Generated Integers Raised to 100th Power\n"
            f"(n = {num_rand_int:,})"
        )
    )
    ax.set_xlabel("Most Significant Digit")
    ax.set_ylabel("Probability")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.grid()


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())  # Calls plot function
    plt.show()  # Display plot created in plot function


if __name__ == "__main__":
    main()
