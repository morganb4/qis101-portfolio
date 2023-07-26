#!/usr/bin/env python3
"""sum_multiples.py"""


def main() -> None:
    """Prints sum of nat numbers in interval [1, 1900) that are divisible by 7 & 11"""
    total_sum: int = 0
    # Adds the number 'num' to total_sum if num is divisible by 7 and 11
    for num in range(1, 1900):
        if num % 7 == 0 and num % 11 == 0:
            total_sum += num
    print(f"The sum is {total_sum:,}")  # Prints total sum


if __name__ == "__main__":
    main()
