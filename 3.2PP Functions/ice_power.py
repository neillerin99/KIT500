"""
3.3PP Functions: Engine Power
This program computes the Engine power of a vehicle and also shows how functions work
"""

__author__ = "NEIL EDRIANE LERIN"

import math as m


def power_output(torque: float, rpm: int) -> float:
    """
    This function computes the power output of a internal combustion engine.
    Takes torque and rpm as parameters and returns the computed power as a float.
    """
    power: float  # calculated power value
    
    # computes the power based on the formula provided
    power = torque * rpm * (2 * m.pi / 60000)
    return power


def main():
    torque: int  # variable to store torque value input
    rpm: int  # variable to store rpm value for input

    # printing of power based from static arguments
    print(f"Porsche 911 (999.2): {power_output(449,6500):.2f} kW")
    print(f"Toyota GR Corolla: {power_output(370,5550):.2f}")

    # assigning user prompts
    torque = int(input("Input torque (Nm): "))
    rpm = int(input("Input motor's rpm: "))

    # printing of power based from dynamic arguments
    print("Calculating...")
    print(f"Output: {power_output(torque, rpm):.2f} kW")


if __name__ == "__main__":
    main()
