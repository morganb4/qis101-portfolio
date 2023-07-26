#!/usr/bin/env python3
"""sum_squares.py"""


def gauss_sum(num: int) -> float:
    """Returns the sum of squares of first 'num' natural numbers using Gauss formula"""
    calc_sum: float = (2 * num**3 + 3 * num**2 + num) / 6  # Gauss's formula
    return int(calc_sum)  # Returns sum as an integer to make formatting uniform


def main() -> None:
    """Sums the squares of the first 1000 natural numbers using two approaches"""
    # Calculation using loop
    total_sum = 0  # Contains the total running sum
    # Updates total sum by adding the squares of the first 1000 natural numbers
    for n in range(1, 1_001):
        n_square: int = n**2
        total_sum += n_square
    print(f"The total sum using loop calculation is {total_sum:,}")
    # Calculation using functional equation for Gaussian summation
    print(f"The total sum using Gauss's functional equation is {gauss_sum(1_000):,}")


if __name__ == "__main__":
    main()
