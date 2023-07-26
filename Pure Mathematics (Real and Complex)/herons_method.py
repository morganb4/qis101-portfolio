#!/usr/bin/env python3
"""herons_method.py"""

# Import mean function in order to carry out Heron's method
from statistics import mean

# Import randint function from random module
from random import randint


def heron_sqrt(s: int) -> float:
    """Returns estimate of the square root, r, of an integer, s, using Heron's method"""
    r: float = s / 2  # r (represents best guess for sqrt) initialized to s / 2
    epsilon: float = abs(
        s - r**2
    )  # epsilon tracks the accuracy of r during iterations
    # Iterates through Heron's formula until epsilon is <= 1e-8
    while epsilon > 1e-8:
        r = mean([s / r, r])
        epsilon = abs(s - r**2)
    return r


def main() -> None:
    """Chooses a random integer and returns the integer along with its square root"""
    s: int = randint(1_000_000, 2_000_000)  # Chooses a random int to calculate sqrt
    print(f"Original integer (s): {s:,}")
    print(f"Square root estimate (r): {heron_sqrt(s):,.8f}")


if __name__ == "__main__":
    main()
