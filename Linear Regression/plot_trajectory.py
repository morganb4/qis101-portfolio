#!/usr/bin/env python3
"""plot_trajectory.py"""

# Plots final milliseconds of the trajectory of a secondary particle created by cosmic
# rays before it impacts Earth.  Models the data using a linear fit, and calculates the
# particle's velocity as well as its original height in the stratosphere.

# Used linear fit code from script written by @dbiersach:
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2017%20-%20Simulation%20and%20Modelling/quadratic_regression.py

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from sklearn.linear_model import LinearRegression  # Linear fit module

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def fit_linear(
    vec_x: NDArray[np.float_], vec_y: NDArray[np.float_]
) -> tuple[float, float]:
    """Find best linear fit for a given set of data"""
    # Boost the x vector so it is a matrix
    vec_x = vec_x[:, np.newaxis]
    # Fit the data using linear regression
    model: LinearRegression = LinearRegression().fit(vec_x, vec_y)
    # Extract slope and y-intercept from the model variable
    m: float = float(model.coef_[0])
    b: float = float(model.intercept_)  # type: ignore
    return m, b


def plot_data(
    times_actual_ms: NDArray[np.float_],
    y_vals_m: NDArray[np.float_],
    m: float,
    b: float,
    ax: Axes,
) -> None:
    """Plot the data from the .csv file and its linear fit in meters vs milliseconds"""

    # Plot the linear fit for the data as a line graph
    ax.plot(
        times_actual_ms,
        m * times_actual_ms + b,
        color="red",
        linewidth=2,
        label="Linear Fit",
    )

    # Plot the original data points using open circles
    ax.plot(
        times_actual_ms,
        y_vals_m,
        color="None",
        marker="o",
        mec="black",
        mfc="None",
        ms=4,
        label="Original Data",
    )

    # Set title, axis labels, and legend
    ax.set_title("Height of Particle vs Particle Lifetime")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Height (m)")
    ax.set_ylim(top=25)
    ax.legend()

    plt.show()


def main(file_name: str) -> None:
    """Plot the data in the given .csv file and find the line of best fit to determine
    the secondary particle's velocity and original height"""

    # Path variable to handle the file import
    data_file: Path = Path(__file__).parent.joinpath(file_name)

    # Generate a numpy array from the .csv file
    samples: NDArray[np.float_] = np.genfromtxt(data_file, delimiter=",")
    # Separate the time and the height values from the .csv into two arrays
    # Timestamps from csv stored in nanoseconds
    times_ns: NDArray[np.float_] = samples[:, 0]
    # Y vals from csv stored in centimeters
    y_vals_cm: NDArray[np.float_] = samples[:, 1]

    # Convert the time array to milliseconds
    times_ms: NDArray[np.float_] = np.array([time * 1e-6 for time in times_ns])
    # Convert the y value array to meters
    y_vals_m: NDArray[np.float_] = np.array([y_val * 1e-2 for y_val in y_vals_cm])

    # Store the particle's total lifetime in ms
    particle_lifetime_ms: float = 0.1743

    # Create new array to store the times in the particle's trajectory corresponding to
    # given data points by subtracting values of times_ms from the particle's lifetime.
    # Use np.flip to reverse order of generated array so times are lowest to highest
    times_actual_ms: NDArray[np.float_] = np.flip(
        np.array([particle_lifetime_ms - time for time in times_ms])
    )

    # Find the linear fit for the data
    m: float  # Var for linear slope
    b: float  # Var for y int
    m, b = fit_linear(times_actual_ms, y_vals_m)

    # Positive multiple of c which produces the velocity of the particle
    velocity_c: float = abs(m * 1000 / 2.9979e8)

    # Display the velocity with respect to c and the initial height of the particle
    # in km, each rounded to 4 decimal places, in the terminal
    print(
        f"The velocity of the particle is approximately "
        f"({velocity_c:.4f} * c) m/s downward."
    )
    print(f"The original height of the particle is {(b / 1000):.4f} kilometers.")

    plt.figure(__file__)

    # Plot the data from the .csv file and its linear fit
    plot_data(times_actual_ms, y_vals_m, m, b, plt.axes())


if __name__ == "__main__":
    main("ray.csv")
