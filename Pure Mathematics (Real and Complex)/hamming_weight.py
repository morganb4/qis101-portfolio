#!/usr/bin/env python3
"""hamming_weight.py"""


# Calculates the Hamming Weight of a given integer without using built-in functions
def hamming_weight_basic(n: int) -> int:
    h_weight: int = 0  # Initializes Hamming Weight to 0
    # Follows the Divide by 2 algorithm to convert integer to binary
    while n > 0:  # Loops until n = 0
        if n % 2 == 1:  # Adds 1 to h_weight if there is a remainder of 1
            h_weight += 1
        n = n // 2  # Performs floor division to create new n
    return h_weight


# Calculates Hamming Weight using Python's built-in functions
def hamming_weight_efficient(n: int) -> int:
    # Returns number of 1's which appear in binary representation of n
    return bin(n).count("1")


def main() -> None:
    # Takes an integer to find the Hamming Weight using two methods
    n: int = 95_601
    print(f"The Hamming Weight of {n:,} is...")
    print(f"{hamming_weight_basic(n)} according to the function created from scratch.")
    print(f"{hamming_weight_efficient(n)} according to functions available in Python.")


if __name__ == "__main__":
    main()
