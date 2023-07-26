#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""


def convert_to_fah(celsius: int) -> float:
    """Converts temperature in Celsius to Fahrenheit"""
    fahrenheit: float = celsius * (9 / 5) + 32
    return fahrenheit


def main() -> None:
    """Prints temperatures in Celsius and equivalent in Fahrenheit"""
    # for loop prints temp equalities from -44 C to 106 C with 4 C increments
    for celsius in range(-44, 105, 4):
        fahrenheit: float = convert_to_fah(celsius)
        print(f"{celsius:>6.2f} C = {fahrenheit:>6.2f} F")
    # Prints temp equality for 106 C as assigned
    print(f"106.00 C = {convert_to_fah(106):>6.2f} F")


if __name__ == "__main__":
    main()
