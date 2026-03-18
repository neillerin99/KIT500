"""
3.2PP Fill in the Blanks: Paris Olympics

This program displays the medal tally with their corresponding countries,
This also shows how inputs in python works
"""

__author__ = "NEIL EDRIANE LERIN"


def main():
    first_place: str # country variable with the most gold medals
    capital_city: str # capital city of the country in first place
    second_place: str  # country with the second most gold medals currently
    gold_medals_1: int # number of gold medals won by the country in first place
    gold_medals_2: int # number of gold medals won by the country in second place
    margin: int # difference between gold medal counts

    # display program title
    print("PARIS OLYMPICS DAILY GOLD TALLY")
    print()

    # Prompt the user to enter the required information
    first_place = input("Enter the name of the country in first place: ")
    capital_city = input("Enter the capital city of the first place country: ")
    second_place = input("Enter the name of the country in second place: ")
    gold_medals_1 = int(input("How many gold medals has the first-placed country won? "))
    gold_medals_2 = int(input("How many gold medals has the second-placed country won? "))

    # compute margin
    margin = gold_medals_1 - gold_medals_2

    # display dynamic output base on stored variables
    print(f"{first_place} currently tops the 2024 Paris Olmypics' medal tally with {gold_medals_1} gold.")
    print(f"Citizens of {capital_city} are overjoyed at beating arch-rivals {second_place}.")
    print(f"Their lead of {margin} gold looks secure with only competitive programming left.")


if __name__ == "__main__":
    main()