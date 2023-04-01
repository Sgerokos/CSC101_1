# Ask's the user to input social security number

# Ask's the user to enter a social security number

SSN=input("Please Enter a Social Security Number: ")

# Variable to verify the number

valid=True

if len(SSN)!= 11:

# If length is not 11 it will return false
    
    valid = False

elif SSN[3]!= "-" or SSN[6]!= "-":

# If the dashes are not at correct places return false
    
    valid = False

elif not (SSN[:3].isdigit() and SSN[4:6].isdigit() and SSN[7:].isdigit()):

# If the numeric parts do not consists of numbers return false
    
    valid = False

if valid:

    print("Valid SSN")

else:

    print("Invalid SSN")