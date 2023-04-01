# Import time library from python

import time

# Ask's the user to input the investmant amount

investmantAmount = eval(input("Please Enter Investment Amount: "))

# Ask's the user to input Annual Interest Amount

annualInterestRate = eval(input("Please Enter Annual Interest Amount: "))

# Ask's user to input number of year's of interest

numberOfYears = eval(input("Please Enter Number of Year's: "))

# Calculates the ammount based off of interest and number of year's

futureInvestmentValue = investmantAmount *(1 +(annualInterestRate / 1200)) ** (numberOfYears * 12)

# Print's the value on screen for the user

print("The Accumulated Value is ", round(futureInvestmentValue , 2))