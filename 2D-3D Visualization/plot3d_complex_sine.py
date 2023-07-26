#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

# Imports
from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm  # Import colormap

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def f(z: NDArray[np.complex_]) -> NDArray[np.complex_]:
    """Complex function to graph: f(z) = |sin(z)|"""
    return abs(np.sin(z))  # type: ignore


def plot(ax: Axes) -> None:
    """Plot f(z) = |sin(z)| for the complex region |Re(z)|<=2.5 and |Im(z)|<=1"""

    # Create real and imaginary z domain
    re_z: NDArray[np.float_] = np.linspace(-2.5, 2.5, 30)
    im_z: NDArray[np.float_] = np.linspace(-1, 1, 30)

    # Create meshgrid for the imaginary domain
    re_z, im_z = np.meshgrid(re_z, im_z)

    # Create array of function values
    f_z: NDArray[np.complex_] = f(re_z + im_z * 1j)  # type: ignore

    # Plot the function with a colormap
    surf: Any = ax.plot_surface(  # type: ignore
        re_z, im_z, f_z, cmap=cm.plasma, linewidth=0, antialiased=False  # type: ignore
    )

    # Set color legend
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    # Set axis labels
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    ax.set_zlabel(r"$|sin(z)|$")  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))  # Set matplotlib projection to 3d
    plt.show()


if __name__ == "__main__":
    main()
