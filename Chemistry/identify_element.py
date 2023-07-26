#!/usr/bin/env python3
"""identify_element.py"""

# Identifies an unknown gas using linear regression of volume vs temperature data.

# Referenced this video:  https://www.youtube.com/watch?v=990ed9bsQlY
# Also referenced this table:  https://instrumentationandcontrol.net/molecular-weight-common-fluids-table.html
# Confirmed linear regression using Desmos


# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
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
    temps_kelvin: NDArray[np.float_],
    vol__cubic_m: NDArray[np.float_],
    m: float,
    b: float,
    ax: Axes,
) -> None:
    """Plot the original data and its linear fit"""

    # Create domain to plot the linear fit based on the original data
    min_temp: float = float(np.min(temps_kelvin))
    max_temp: float = float(np.max(temps_kelvin))
    temp_lin_fit: NDArray[np.float_] = np.linspace(min_temp, max_temp, 500)

    # Plot the linear fit
    ax.plot(
        temp_lin_fit, m * temp_lin_fit + b, color="red", linewidth=2, label="Linear Fit"
    )

    # Plot the original data points using open circles
    ax.plot(
        temps_kelvin,
        vol__cubic_m,
        color="None",
        marker="o",
        mec="black",
        mfc="None",
        ms=4,
        label="Original Data",
    )

    # Set title, axis labels, and legend
    ax.set_title("Volume of Gas vs Temperature")
    ax.set_xlabel("Temperature (Kelvin)")
    ax.set_ylabel("Volume ($m^3$)")
    ax.legend()

    plt.show()


def main() -> None:
    """Plot the given data and its linear fit, and use the linear fit to identify
    the unknown gas"""

    # Vars for pressure of the gas, molar gas constant, and mass of gas
    pressure: float = 2  # atm
    gas_constant: float = 8.21e-5  # (atm * m^3)/(mol * K)
    gas_mass: float = 50  # g

    # Store temperature data in Celsius
    temps_celsius: NDArray[np.float_] = np.linspace(-50, 150, 5)
    # Convert the temperature data from Celsius to Kelvin
    temps_kelvin: NDArray[np.float_] = np.array(
        [temp + 273.15 for temp in temps_celsius]
    )

    # Store volume data in liters
    vol_liters: NDArray[np.float_] = np.array([11.6, 14, 16.2, 19.4, 21.8])
    # Convert volume data to m^3
    vol_cubic_m: NDArray[np.float_] = np.array([vol * 10e-4 for vol in vol_liters])

    # Find the linear fit for the data
    m: float  # Var for linear slope
    b: float  # Var for y int
    m, b = fit_linear(temps_kelvin, vol_cubic_m)

    # Calculate the number of moles of gas (n) using m (Volume / Temperature)
    # based on the Ideal Gas Law
    n: float = pressure / gas_constant * m

    # Calculate the molecular weight of the gas using n and the gas's mass
    mol_weight: float = gas_mass / n

    # Print the calculated data and the identified element on screen
    print(
        f"There are {n:.2f} moles of gas in the sample.\n"
        f"The molecular weight of the gas is {mol_weight:.1f} grams per mole.\n"
        "Based on this data, the mystery gas is Argon."
    )

    plt.figure(__file__)

    # Plot the data and its linear fit
    plot_data(temps_kelvin, vol_cubic_m, m, b, plt.axes())


if __name__ == "__main__":
    main()
