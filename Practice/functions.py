"""
Briefly describe the program
"""

__author__ = "Neil Edriane Lerin"


def greet_age(age: int) -> None:
    if age <= 20:
        print("You have a valid age")
    elif age >= 21 and age <= 50:
        print("You are a bit overaged")


def balance(age: int) -> int | None:
    if age <= 20:
        return 500
    elif age >= 21 and age <= 50:
        return 501
    else:
        return None


def main():
    age: int = 21
    # print("hello this is a greeting from the main function.")
    # greet_age(age)
    a: str = "dwarf"
    print(f"red {a}")
    print("balance " + a)


if __name__ == "__main__":
    main()
