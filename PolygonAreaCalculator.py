# Import's math library

import math

# Ask's the user for the number side's

number = eval(input("Please Enter the Number of Sides: "))

# Ask's the user for the length of the side's

sideLength = float(input("Please Enter the Length of the Sides: "))

# Calculate's the area using the number and sideLength's

area = number * sideLength * sideLength / math.tan(math.pi /number) /4

# Print's the area on screen for the user

print("The Area of the Polygon is " + str(area))