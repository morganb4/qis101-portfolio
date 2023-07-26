#!/usr/bin/env python3
"""maze_search.py"""

# File written by @dbiersach:
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2014%20-%20Linear%20Algebra/maze_search.py

# Uses depth-first search to solve the maze stored in maze.csv.pickle.
# The maze stored in maze.csv.pickle forces the depth-first search to
# take the maximum  possible number of steps to solve the maze.

from __future__ import annotations

import os
import pickle
import sys
import typing

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection, PatchCollection
from matplotlib.patches import Rectangle

if typing.TYPE_CHECKING:
    import numpy as np
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot_cell_walls(ax: Axes, maze: NDArray[np.int_]) -> None:
    for y in range(10):
        bottom: int = (9 - y) * 10
        top: int = bottom + 10
        for x in range(10):
            left: int = x * 10
            right: int = left + 10
            cell: int = maze[y, x]
            if cell & 1 == 1:
                lc = LineCollection(
                    [[(left, top), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore
            if cell & 2 == 2:
                lc = LineCollection(
                    [[(right, bottom), (right, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore
            if cell & 4 == 4:
                lc = LineCollection(
                    [[(left, bottom), (right, bottom)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore
            if cell & 8 == 8:
                lc = LineCollection(
                    [[(left, bottom), (left, top)]], color="black", linewidth=3
                )
                ax.add_collection(lc)  # type: ignore


def plot_steps(ax: Axes, steps: list[tuple[int, int, int]]) -> None:
    for s in steps:
        y, x, _ = s
        bottom: int = (9 - y) * 10
        left: int = x * 10
        patch = Rectangle((left + 4, bottom + 4), 2, 2)
        ax.add_collection(PatchCollection([patch], facecolor="blue"))  # type: ignore


def plot_maze(
    ax: Axes, maze: NDArray[np.int_], steps: list[tuple[int, int, int]]
) -> None:
    ax.axis("off")
    ax.set_aspect("equal")
    ax.set_xlim(-5, 105)
    ax.set_ylim(-5, 105)
    ax.set_title(f"{len(steps)} steps")

    # Plot enter and exit cells
    entrance = Rectangle((0, 90), 10, 10)
    ax.add_collection(PatchCollection([entrance], facecolor="tan"))  # type: ignore
    exit = Rectangle((90, 0), 10, 10)
    ax.add_collection(PatchCollection([exit], facecolor="orange"))  # type: ignore

    # Plot cell corner circles
    for x in range(0, 110, 10):
        for y in range(0, 110, 10):
            ax.scatter(x, y, color="black")

    plot_steps(ax, steps)

    plot_cell_walls(ax, maze)


def in_path(steps: list[tuple[int, int, int]], y: int, x: int) -> bool:
    for s in reversed(steps):
        sy, sx, _ = s
        if sy == y and sx == x:
            return True
    return False


def search_maze(maze: NDArray[np.int_], steps: list[tuple[int, int, int]]) -> bool:
    y, x, dir = steps.pop()

    if x == 9 and y == 9:
        steps.append((9, 9, 0))
        return True

    if dir == 0:
        steps.append((y, x, 1))
        if maze[y, x] & 1 != 1 and not in_path(steps, y - 1, x):
            steps.append((y - 1, x, 0))
        return False

    if dir == 1:
        steps.append((y, x, 2))
        if maze[y, x] & 2 != 2 and not in_path(steps, y, x + 1):
            steps.append((y, x + 1, 0))
        return False

    if dir == 2:
        steps.append((y, x, 4))
        if maze[y, x] & 4 != 4 and not in_path(steps, y + 1, x):
            steps.append((y + 1, x, 0))
        return False

    if dir == 4:
        steps.append((y, x, 8))
        if maze[y, x] & 8 != 8 and not in_path(steps, y, x - 1):
            steps.append((y, x - 1, 0))
        return False

    return False


def main(file_name: str) -> None:
    with open(file_name + ".pickle", "rb") as file_in:
        maze: NDArray[np.int_] = pickle.load(file_in)

    # Steps is list of tuples, where each tuple contains the
    # (y, x, last direction tried) for each step along current path
    steps: list[tuple[int, int, int]] = [(0, 0, 0)]

    while not search_maze(maze, steps):
        pass

    plt.figure(file_name)
    plot_maze(plt.axes(), maze, steps)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        file_name: str = os.path.dirname(sys.argv[0]) + "/maze.csv"
    else:
        file_name = sys.argv[1]

    main(file_name)
