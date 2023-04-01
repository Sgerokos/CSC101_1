# Import's the random module

import random

# Import's the time module

import time

# Count's the number of correct answers

correctAnswer = 0 

# Count's the number of incorrect answers

incorrectAnswer = 0 

# Check's the consistency of incorrect answer

incorrectCurrentStreak = 0 

# The longest streak of incorrect answer

longestCorrectStreak = 0 

# The current streak of correct answer's

currentCorrectStreak = 0 

# Start's the quiz

startTime = time.time() 

# The input from the user for the answer

answer = 0 

# Check's to see if the answer is correct

iscorrect = True 

#while loop for subtracting 1 point for each wrong answer

while(answer != -1):
    
# Check's to see if an incorrect answer was given 3 time's 
    
    if incorrectCurrentStreak != 3 :
        
# Generate's two random integers
        
        number1 = random.randint(0,9)
        
        number2 = random.randint(0,9)
        
# If number1 is less then number2, swap number1 with number2 
        
        if number1 < number2 : 
            
            number1, number2 = number2, number1
            
# Prompt the student to answer "What is number1 - number2?" 
        
        answer = eval(input("what is " + str(number1) + " - " + str(number2) + "? "))
        
# Grade's the answer and display the result for the user
        
        if number1 - number2 == answer :
            
            print("Your amswer is correct!")
            
# Add's plus one for a correct answer

            correctAnswer += 1 
            
            iscorrect = True 
            
        
        else:
            
            print("Your answer is incorrect. \n", number1, "-", number2, "is", number1 - number2)
            
# Add's plus one for a incorrect answer
            
            incorrectAnswer += 1  
            
            iscorrect = False
        
# If current answer is true  
        
        if iscorrect == True :
            
# Add's plus one for a correct streak
            
            currentCorrectStreak += 1 
            
            incorrectCurrentStreak = 0
            
# This check's if currentCorrectStreak is greater than the longest correctAnswer streak 
            
            if currentCorrectStreak > longestCorrectStreak :
                
                longestCorrectStreak = currentCorrectStreak
        
#if current answer is False    
        
        else:
            
# Add's plus one to incorrect streak
            
            incorrectCurrentStreak += 1
            
            currentCorrectStreak = 0 
            
        
# If the incorrect Streak become's 3   
    
    else:
        
# Break's out of the while loop
        
        break 
    
# Get's the end time and test time

endTime = time.time() 

testTime = int(endTime - startTime)

# Calculate's the toatal score

totalScore = correctAnswer + (longestCorrectStreak * 10)

# Print's result's for the user

print("The Total Score is ", totalScore, "\nTotal Correct Answer's is = ",correctAnswer, 
      
      "\nThe Total Incoorect Answer's is = ", incorrectAnswer, 
      
      "\nTime The Duration of Test is ", testTime, " seconds")