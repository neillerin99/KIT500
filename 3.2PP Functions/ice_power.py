"""
3.3PP Functions: Describe the option you chose here
"""

__author__ = "NEIL EDRIANE LERIN"

# Add any imports here
import math as m


def power_output(torque: float, rpm: int) -> float:
    """This function computes power using the formula below"""
    return torque * rpm * (2 * m.pi / 60000)


def main():
    torque: int  # variable to store torque value input
    rpm: int  # variable to store rpm value for input

    print(f"Prosche 911 (999.2): {power_output(449,6500):.2f} kW")
    print(f"Toyota GR Corolla: {power_output(370,5550):.2f}")

    torque = int(input("Input torque (Nm): "))
    rpm = int(input("Input motor's rpm: "))

    print("Calculating...")
    print(f"Ouput: {power_output(torque, rpm):.2f} kW")


if __name__ == "__main__":
    main()
