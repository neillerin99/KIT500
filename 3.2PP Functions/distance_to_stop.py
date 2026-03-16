"""
3.3PP Functions: Distance to Stop
This program shows the distance to stop computation and also hows how functions work in Python
"""

__author__ = "NEIL EDRIANE LERIN"


def calculate_distance(velocity:float, time: float) -> float:
    """
    This function computes the distance it takes to stop a vehicle
    """
    FRICTION: float = 0.7 # Friction value constant
    GRAVITY: float = 9.81 # Gravity value constant
    distance: float # variable to store distance value
    
    distance = velocity * time + velocity ** 2 / (2 * FRICTION * GRAVITY)
    return distance


def main():
    velocity: float # variable declaration to store veloctity (speed)
    time: float # variable declaration to store time
    
    # printing of distance base from static values
    print(f"Distance to stop 1: {calculate_distance(22.22, 1.75)} m")
    print(f"Distance to stop 1: {calculate_distance(8.33, 3.1)} m")
    
    # assigning user prompts
    velocity = float(input("Input initial velocity (m/s): "))
    time = float(input("Input reaction time (seconds): "))
    
    # printing of distance base from dynamic/input values
    print("Calculating...")
    print(f"Distance to stop: {calculate_distance(velocity, time):.2f} m")


if __name__ == "__main__":
    main()
