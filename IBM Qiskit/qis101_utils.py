"""qis101_utils.py"""

# Script written by @dbiersach:
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2014%20-%20Linear%20Algebra/qis101_utils.py
# Called in various scripts throughout the qis101-portfolio repository to display LaTeX

from __future__ import annotations

import typing

import numpy as np
from IPython.core.display import Math

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def as_latex(
    a: NDArray[np.int_ | np.float_ | np.complex_],
    places: int = 5,
    column: bool = False,
    prefix: str = "",
) -> Math:
    def strip(val: float) -> str:
        d: str
        # Handle common fractions
        if abs(np.round(val, 5)) == 0.25000:
            d = ""
            if val < 0:
                d += "-"
            d += r"\frac{1}{4}"
            return d
        if abs(np.round(val, 5)) == 0.50000:
            d = ""
            if val < 0:
                d += "-"
            d += r"\frac{1}{2}"
            return d
        if abs(np.round(val, 5)) == 0.57735:
            d = ""
            if val < 0:
                d += "-"
            d += r"\frac{1}{\sqrt{3}}"
            return d
        if abs(np.round(val, 5)) == 0.70711:
            d = ""
            if val < 0:
                d += "-"
            d += r"\frac{1}{\sqrt{2}}"
            return d
        if abs(np.round(val, 5)) == 0.8165:
            d = ""
            if val < 0:
                d += "-"
            d += r"\sqrt{\frac{2}{3}}"
            return d
        if abs(np.round(val, 5)) == 0.86603:
            d = ""
            if val < 0:
                d += "-"
            d += r"\frac{\sqrt{3}}{2}"
            return d
        frmt: str = ":." + str(places) + "f"
        d = str("{v" + frmt + "}").format(v=val)
        while d[-1] == "0":
            d = d[:-1]
        if d[-1] == ".":
            d = d[:-1]
        if float(d) == 0:
            d = "0"
        return d

    m: NDArray[np.complex_] = np.copy(a)
    if len(m.shape) == 1:
        m = m[np.newaxis, :]
        if column:
            m = m.T
    prec: float = 1 / 10**places
    s: str = r"\begin{bmatrix}"
    for row in range(m.shape[0]):
        for col in range(m.shape[1]):
            v: np.complex_ = m[row, col]
            real_comp: float = float(np.real(v))
            imag_comp: float = float(np.imag(v))
            is_imag_neg: bool = imag_comp < 0
            is_real_zero: bool = bool(np.isclose(real_comp, 0, atol=prec))
            is_imag_zero: bool = bool(np.isclose(imag_comp, 0, atol=prec))
            is_imag_one: bool = bool(np.isclose(abs(imag_comp), 1, atol=prec))
            if is_real_zero:
                if is_imag_zero:
                    s += "0"
            else:
                s += strip(real_comp)
            if not is_imag_zero:
                if is_imag_one:
                    if is_imag_neg:
                        s += r"-i"
                    else:
                        if not is_real_zero:
                            s += "+"
                        s += r"i"
                else:
                    if not is_real_zero and not is_imag_neg:
                        s += " + "
                    s += strip(imag_comp) + "i"
            if col < m.shape[1] - 1:
                s += " &"
        if row < (m.shape[0] - 1):
            s += r"\\[1em]"
        else:
            s += r"\\"
    s += r"\end{bmatrix}"
    return Math(r"\large" + prefix + s)  # type: ignore
