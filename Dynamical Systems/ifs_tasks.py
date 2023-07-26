"""ifs_tasks.py"""

# Script written by @dbiersach (ifs.py):
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2019%20-%20Dynamical%20Systems/ifs.py
# Called as helper script in ifs_hexagonal.py

from __future__ import annotations

import typing
from dataclasses import dataclass

import numpy as np
from pygame import Color

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


@dataclass
class Transform:
    def __init__(self) -> None:
        self.x1: float = 0.0
        self.y1: float = 0.0
        self.x2: float = 0.0
        self.y2: float = 0.0
        self.x3: float = 0.0
        self.y3: float = 0.0
        self.color: Color = Color("black")
        self.probability: float = 0.0
        self.m: NDArray[np.float_] = np.zeros((3, 3), dtype=np.float_)


@dataclass
class IteratedFunctionSystem:
    def __init__(self) -> None:
        self.transforms: list[Transform] = []
        self.affine_width: float = 0.0
        self.affine_height: float = 0.0
        self.cdf: float = 0.0

    # def __repr__(self) -> str:
    #    return str(f"IteratedFunctionSystem({self.transforms}")

    def set_base_frame(
        self, x_min: float, y_min: float, x_max: float, y_max: float
    ) -> None:
        self.affine_width = x_max - x_min
        self.affine_height = y_max - y_min
        return

    # fmt: off
    def add_mapping(self, x_left: float, y_left: float,
                     x_right: float, y_right: float,
                     x_top: float, y_top: float,
                     color: Color, probability: float) -> None:
    #fmt: on
        # Probabilities accumulate across mappings
        self.cdf += probability

        t = Transform()
        t.x1 = x_left
        t.y1 = y_left
        t.x2 = x_right
        t.y2 = y_right
        t.x3 = x_top
        t.y3 = y_top
        t.color = color
        t.probability = self.cdf
        self.transforms.append(t)

    def generate_transforms(self) -> None:
        for t in self.transforms:
            coeffs: NDArray[np.float_] = np.array(
                [[0, 0, 1], [self.affine_width, 0, 1], [0, self.affine_height, 1]]
            )

            # Solve systems of 3x3 equations to get transformation matrix
            vals: NDArray[np.float_] = np.array([t.x1, t.x2, t.x3])
            sol: NDArray[np.float_] = np.linalg.solve(coeffs, vals)
            t.m[0, 0] = sol[0]
            t.m[1, 0] = sol[1]
            t.m[2, 0] = sol[2]

            vals = np.array([t.y1, t.y2, t.y3])
            sol = np.linalg.solve(coeffs, vals)
            t.m[0, 1] = sol[0]
            t.m[1, 1] = sol[1]
            t.m[2, 1] = sol[2]

            # Last column in transformation matrix is always this
            t.m[0, 2] = 0
            t.m[1, 2] = 0
            t.m[2, 2] = 1

    def transform_point(self, x: float, y: float) -> tuple[float, float, Color]:
        p: float = np.random.random()
        for t in self.transforms:
            if p <= t.probability:
                xt: float = x * t.m[0, 0] + y * t.m[1, 0] + t.m[2, 0]
                yt: float = x * t.m[0, 1] + y * t.m[1, 1] + t.m[2, 1]
                return xt, yt, t.color        
        # This should never happen if the mapping
        # probabilities all sum to 1.0
        return 0, 0, Color("black")
