import math

# use of long string to show initial output user will see
# this was explained in the example 10 of task 2 example.py
print(
'''
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

''')

# Take user input from the above menu and determine what they chose
# convert user input to lowercase
chosenCalculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# investment selected
if chosenCalculation == 'investment':

    # store user inputs for investment calculation in their own variables
    # variables converted to integer and float for later calculations
    deposit = int(input("Enter deposit amount: "))
    interestRate = float(input("Enter interest rate(%): "))
    yearsOfInterest = int(input("Enter amount of years you plan on investing: "))

    # User choice if they want simple or compound interest
    # determines which interest formula calculation is used 
    # if no valid input then display error message
    interest = input("Do you want 'simple' or 'compound' interest: ").lower()

    if interest == 'simple':
        # calculate total amount with interest for simple interest and display result
        totalAmountWithInterest = deposit * (1 + ((interestRate/100) * yearsOfInterest))
        print(f"\nTotal amount with interest is {totalAmountWithInterest}")

    elif interest == 'compound':
        # calculate total amount with interest for compound interest and display result
        totalAmountWithInterest = deposit * math.pow((1 + (interestRate/100)), yearsOfInterest)
        print(f"\nTotal amount with interest is {totalAmountWithInterest}")

    else:
        print("Invalid selection, please start again.")

# bond selected
elif chosenCalculation == 'bond':

    # store user inputs for bond calculation
    houseValue = int(input("Enter value of the house: "))
    interestRate = float(input("Enter the interest rate(%): "))
    monthsToRepay = int(input("Enter number of months you plan to take to repay the bond: "))

    # calculate monthly interest rate and use within monthly repayment formula, display result
    monthlyInterest = (interestRate / 100) / 12
    monthlyRepayment = (monthlyInterest * houseValue) / (1 - (1 + monthlyInterest)**(-monthsToRepay))

    print(f"\nMonthly repayments are {monthlyRepayment}")

else:
    print('Invalid selection, please start again.')