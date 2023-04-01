# Import's math library

import math

# Ask's the user to enter the number of boxe's they want to buy

print("Please Enter the Number of Boxes to Buy: ")

#accepting the quantity 

while(1):

    quantity = int(input())

# if Greater then 200 then it will ask the user to enter a number under 200

    if(quantity > 200):

        print("Please Enter Less then 200 ")

    else:

        break

# Estimates the price 

amount = quantity * 1.50

print("Please Enter a Shipping Location:")

shipping = input()

# If NY it will autimaticly add 8.75% for the taxes

if(shipping == "NY"):

    amount += amount * 0.0875

if(quantity > 50):

    amount -= amount * 0.2

print("What Type of Shipping Mode Would you Like? Please Enter Air or Ground : ")

# Ask's user for Shipping mode

shippingMode = input()

# Estimating the price of the shipping mode

if(shippingMode == "Air"):

    amount += 50

else:

    amount += 10

# Print's the result's

print(" The Total Amount is: " + str(round(amount , 2)))
