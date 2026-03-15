"""
3.3PP Functions: Loan Repayments
This program computes the loan payments prompted by the user.
This prgoram shows how functions can be implemented.
"""

__author__ = "NEIL EDRIANE LERIN"


# Define your new function here
def calc_monthly_payment(principal: int, months: int, annual_rate: float) -> float:
    """Function to compute the anual rate based from the formula"""
    
    annual_rate = annual_rate / 1200 # calculate the new annual rate by diving the parameter by 1200
    return (annual_rate * principal) / (1 - (1 + annual_rate) ** -months)


def main():
    principal: int  # principal rate for the loan
    years: int  # number of year
    rate: float  # rate of the loan

    # printing of power based from static arguments
    print(f"Monthly repayment 1: {calc_monthly_payment(826000, 240, 6.25)}")
    print(f"Monthly repayment 2: {calc_monthly_payment(648000, 360, 5.87)}")

    # getting and assigning user prompts
    principal = int(input("Input principal ($): "))
    rate = float(input("Input interest rate (percent): "))
    years = int(input("Input loan duration (years): "))

    # printing of power based from dynamic arguments
    print("Calculating...")
    years = years * 12
    print(f"Monthly repayment: {calc_monthly_payment(principal, years, rate)}")


if __name__ == "__main__":
    main()
