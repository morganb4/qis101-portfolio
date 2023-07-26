#!/usr/bin/env python3
"""prime_racer4.py"""

# Code adapted from @dbiersach, prime_racer3.py
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2005%20-%20Algorithmic%20Efficiency/prime_racer3.py

# Imports
from random import randint, seed
from time import process_time  # type: ignore
from sympy import prime  # type: ignore

# Pre-compute a list of all primes less than 1000 -- prime(168) = 997
prime_list: list[int] = [prime(p) for p in range(1, 169)]  # type: ignore


def is_prime(n: int) -> bool:
    """Returns True/False if the given number is prime"""
    if n % 2 == 0:
        return False
    return all(n % factor != 0 for factor in prime_list)


def main() -> None:
    seed(2016)  # Output will be the same each time code is run

    num_samples: int = 10_000  # Sets the number of random numbers to be generated
    min_val: int = 100_000  # Minimum value of random integers
    max_val: int = 1_000_000  # Maximum value of random integers

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    # List comprehension to create a list of random integers
    samples: list[int] = [randint(min_val, max_val) for _ in range(num_samples)]

    start_time: float = process_time()  # Starts timer
    # List comprehension to count number of primes in the list
    num_primes: int = [is_prime(n) for n in samples].count(True)
    elapsed_time: float = process_time() - start_time  # Calculate elapsed time

    # Print results
    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
