#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

# Based on scripts written by @dbiersach:
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2008%20-%20Early%20Quantum%20Mechanics/spectrum_bohr.py
# https://github.com/dbiersach/qis101/blob/0aa4537a02ac7f71d62ce6bbaf54e1e3175a5d51/labs/Session%2008%20-%20Early%20Quantum%20Mechanics/spectrum_rydberg.py


def bohr_formula(init_orbit: int, final_orbit: int) -> float:
    """Calculates wavelength using Bohr formula given initial and final orbit"""
    # Constants
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    permittivity: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8

    # Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (
        8 * pow(permittivity, 2) * pow(h_plank, 2)
    )

    # Calculates wavelength in nanometers for given initial and final orbit
    # Initial energy level
    e_i: float = -e_0 / pow(init_orbit, 2)
    # Final energy level
    e_f: float = -e_0 / pow(final_orbit, 2)
    # Formula for waveLength in nanometers
    wave_length: float = h_plank * speed_light / (e_i - e_f) * 1e9

    return wave_length


def rydberg_formula(init_orbit: int, final_orbit: int) -> float:
    """Calculates wavelength using Rydberg formula given initial and final orbit"""
    # Constants
    rydberg_constant: float = 1.0967757e7

    # Calculates wavelength in nanometers for given initial and final orbit
    wave_length: float = (
        1
        / (rydberg_constant * (1 / pow(final_orbit, 2) - 1 / pow(init_orbit, 2)))
        * 1e9
    )

    return wave_length


def text_lengthen(string: str, length: int) -> str:
    """Adds spaces to a string until it is desired length"""
    if len(string) < length:
        # Adds spaces to string according to initial string length
        string += " " * (length - len(string))
    return string  # Returns the new, longer string


def hydrogen_table_maker(final_orbit1: int, final_orbit2: int) -> None:
    """Prints a table of wavelengths calculated using Bohr and Rydberg
    formulas using given range of final orbit levels"""

    # Print title for the table
    print("\nWavelengths for Hydrogen Spectral Lines, Pfund and Humphreys Series\n")

    # Store headers for the columns
    header: list[str] = ["Change in Energy Level", "Rydberg Formula", "Bohr Formula"]

    # Modify column headers to have length 24 and print
    for item in header:
        print(text_lengthen(item, 24), end="")
    print("\n")

    # Iterates through changes in energy levels corresponding to each series
    # Prints wavelengths using Rydberg and Bohr equations
    for final_orbit in range(final_orbit1, final_orbit2):
        # Iterate through initial orbits for each series
        for init_orbit in range(final_orbit + 1, final_orbit + 6):
            # Store lengthened string indicating energy level change
            change_in_level: str = text_lengthen(f"{init_orbit:2} -> {final_orbit}", 24)
            # Store lengthened string with Rydberg wavelength
            rydberg_soln: str = text_lengthen(
                f"{rydberg_formula(init_orbit, final_orbit):.0f} nm", 24
            )
            # Store lengthened string with Bohr wavelength
            bohr_soln: str = text_lengthen(
                f"{bohr_formula(init_orbit, final_orbit):.0f} nm", 24
            )
            # Print each of the above strings on same line
            print(change_in_level, end="")
            print(rydberg_soln, end="")
            print(bohr_soln)
        print()  # Add return between differing series


def main() -> None:
    hydrogen_table_maker(5, 7)  # Draw table for hydrogen spectral lines


if __name__ == "__main__":
    main()
