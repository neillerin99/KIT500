"""
4.1PP Selection and Repetition
"""

__author__ = "NEIL EDRIANE LERIN"

import timeit # used for timing the execution of code
from random import randint # used for generating random values


def show_heading(heading: str):
    """
    Displays the given heading in ALL CAPS, underlined by plus (+) symbols
    and followed by a blank line.
    """
    print(f"{heading.upper()}")
    print("+" * len(heading))
    print()


def one_attempt(num1: int, num2: int) -> bool:
    """
    Tests the user's ability to answer a given problem, providing feedback on
    the attempt. Returns True if they answer correctly, False otherwise.
    """
    attempt: int # the user's typed answer
    correct: bool = True # identifier if the user's answer is correct 
    answer: int # variable to hold the current the answer
    attempt = int(input(f'What is {num1} - {num2}? '))

    answer = num1 - num2
    
    if attempt == answer: 
        print('Correct')
    else:
        print(f'Incorrect. The correct answer is {answer}')
        correct = False
        
    return correct


def run_tutorial(max: int, target: int) -> int:
    """
    Tests the user's maths ability by having them answer a series of
    problems correctly until a target number is answered correctly.
    Returns the total number of attempts.
    """
    attempts: int = 0 # the total number of attempts made by the user
    correct: int = 0 # variable to store the number of correct answers
    a: int # random operand A
    b: int # random operand B
    
    while correct < target: 
        a = randint(1, max)
        b = randint(1, max)
        attempts+=1
        if one_attempt(a, b):
            correct+=1 
        print(f'Current correct: {correct}')
        print(f"Current attemps: {attempts}")

    return attempts


def main():
    MAX = 20 # maximum operand value of random numbers
    REQUIRED = 5 # required number of correct answers
    start_time: float # start time of tutorial
    end_time: float # end time of tutorial
    attempted: int # number of problems user attempted before solving REQUIRED problems

    show_heading("Maths Tutorial")
    print("You need to correctly solve subtraction problems as quickly as you can.")
    print(f"You need to answer {REQUIRED} problems correctly before the tutorial ends.")
    print(f"The operand values will be between 1 and {MAX}.")
    print()

    #Run the tutorial session
    input("Press Enter to start the timed test")
    start_time = timeit.default_timer()
    attempted = run_tutorial(MAX, REQUIRED)
    end_time = timeit.default_timer()

    #Report on the user's performance
    print()
    print("Attempts:", attempted)
    print(f"Accuracy: {(100 * REQUIRED / attempted):.1f}%")
    print(f"Total time: {(end_time - start_time):3.1f} s")
    print()
    show_heading("Keep practicing to improve your skills!")


if __name__ == "__main__":
    main()
