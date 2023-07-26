#!/usr/bin/env python3
"""ifs_hexagonal.py"""

# Modified code written by @dbiersach:
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2019%20-%20Dynamical%20Systems/ifs_triangle.py

# Calls ifs_tasks.py and simple_screen_tasks.py

from ifs_tasks import IteratedFunctionSystem
from pygame import Color
from simple_screen_tasks import SimpleScreen
from math import sqrt

ifs = IteratedFunctionSystem()


def plot_ifs(ss: SimpleScreen) -> None:
    """Plot the iterated function system using Pygame"""
    iterations = 200_000  # Iterating the transformation of a pixel 200,000 times
    # Initial pixel location
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        # Return new x, y, and color, then create new x, y, color
        x, y, clr = ifs.transform_point(x, y)  # Randomly pick transformation matrix

    # Iterate as above, but now draw pixel location to create an image of stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)


def main() -> None:
    # Size of the original image
    ifs.set_base_frame(0, 0, 30, 30)

    # Uniform probability for all sides of the hexagon
    p: float = 1 / 6

    # Var h represents half the height of the hexagon
    h: float = 5 * sqrt(3)

    # Create 6 mappings corresponding to the 6 sides of the hexagon
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + h, Color("red"), p)
    ifs.add_mapping(20, 15 + h, 15, 15, 10, 15 + h, Color("pink"), p)
    ifs.add_mapping(10, 15 + h, 15, 15, 5, 15, Color("purple"), p)
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - h, Color("green"), p)
    ifs.add_mapping(10, 15 - h, 15, 15, 20, 15 - h, Color("orange"), p)
    ifs.add_mapping(20, 15 - h, 15, 15, 25, 15, Color("blue"), p)

    # Generate matrices
    ifs.generate_transforms()

    # Draw the IFS
    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),  # Size of base frame
        screen_size=(900, 900),  # Set screen size (not necessary)
        draw_function=plot_ifs,  # Specify what to plot
        title="IFS Hexagon",
    )
    ss.show()


if __name__ == "__main__":
    main()
