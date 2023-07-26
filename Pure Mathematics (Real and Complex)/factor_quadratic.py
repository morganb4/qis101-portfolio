#!/usr/bin/env python3
"""factor_quadratic.py"""


# Code adapted from @dbiersach, factor_quadratic.py:
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2004%20-%20Experimental%20Mathematics/factor_quadratic.py


# Import square root from math module
from math import sqrt

# Import numpy
import numpy as np


def factor_quadratic(h: int, i: int, j: int) -> None:
    """Displays factors of the quadratic polynomial Hx^2 + Ix + J"""

    print(f"Given the quadratic: {h}x^2 + {i}x + {j}")

    # Will be used to prevent repeated factorizations in output
    found_factor: bool = False

    # Calculates the discriminant of the quadratic
    disc: int = i**2 - 4 * h * j
    # Checks if the discriminant is a perfect square
    if sqrt(disc) - int(sqrt(disc)) != 0:
        # If discriminant is not a perfect square, prints 'equation can't be factored'
        print("Sadly, this equation can't be factored.")

    # Finds the GCD of the factors before factoring
    gcd: int = int(np.gcd(h, np.gcd(i, j)))
    if gcd > 1:  # Divides each factor by the GCD if the GCD is > 1
        h, i, j = h // gcd, i // gcd, j // gcd

    for a in range(1, h + 1):
        if h % a == 0:  # Checks for factors of h
            c: int = h // a  # Uses integer division to find corresponding factor of h
            for b in range(1, j + 1):
                if j % b == 0:  # Checks for factors of j
                    d: int = j // b  # Integer div to find corresponding factor of j
                    # Checks if middle term works out the right way
                    if a * d + b * c == i:
                        print("The factors are: ", end="")
                        if gcd > 1:
                            print(f"({gcd})", end="")
                        print(f"({a}x + {b})({c}x + {d})")
                        found_factor = True
                        break  # breaks out of the inner for loop
            # Breaks out of the outer for loop so no repetitive factors are printed
            if found_factor:
                break


def main() -> None:
    # Enter coefficients from the quadratic
    factor_quadratic(115425, 3254121, 379021)


if __name__ == "__main__":
    main()
