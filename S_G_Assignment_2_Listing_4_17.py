# Import's random module

import random

userWins = 0

computerWins = 0

# Repeat’s loop while any of the two win's are greater than 2 times

while userWins <= 2 and computerWins <= 2:

# Ask's the user to choose one  number from the given list and generate's one number randomly for the computer
    
    user = int(input("scissor's (0), rock (1), paper (2): "))
    
    computer = random.randint(0, 2)

# Check who win's and increases the variable for user win’s and computer win’s if both are the same it is a draw and wont increase for either

    if user == 0 and computer == 1:
        
        print("The Computer is Rock. You are Scissor's. You Lost Sorry.")
        
        computerWins += 1
        
    elif user == 1 and computer == 0:
        
        print("The Computer is Scissor. You are Rock. You Win. Congradulation's")
        
        userWins += 1
        
    elif user == 1 and computer == 2:
        
        print("The Computer is Paper. You are Rock. You Lost Sorry.")
        
        computerWins += 1
        
    elif user == 2 and computer == 1:
        
        print("The computer is Rock. You are Paper. You Win. Congradulations!")
        
        userWins += 1
        
    elif user == 2 and computer == 0:
        
        print("The Computer is Scissor. You are Paper. You Lost Sorry.")
        
        computerWins += 1
        
    elif user == 0 and computer == 2:
        
        print("The Computer is Paper. You are Scissor. You Win. Congradulations!")
        
        userWins += 1
        
    elif user == computer == 0:
        
        print("The Computer is Scissor. You are Scissor. It is a Draw.")
        
    elif user == computer == 1:
        
        print('The Computer is Rock. You are Rock. It is a Draw.')
        
    else:
        
        print("The Computer is Paper. You are Paper. It is a Draw.")

# Print's the number of wins for user and computer

print("The Computer Win's" , computerWins, "times.")

print("You Win " , userWins, "times.")