#!/usr/bin/env python3
"""lcm_gcd.py"""

# Note: LCM formula obtained via Wikipedia:  https://en.wikipedia.org/wiki/Least_common_multiple

# Import gcd from math module
from math import gcd


def main() -> None:
    """Calculates the LCM of two positive integers using their GCD"""
    # Variables num_1 and num_2 store the two positive integers in question
    num_1: int = 447618
    num_2: int = 2011835
    # Calculates LCM using formula involving GCD
    lcm: float = num_1 * num_2 / gcd(num_1, num_2)
    print(f"The LCM is {lcm:,}")


if __name__ == "__main__":
    main()
