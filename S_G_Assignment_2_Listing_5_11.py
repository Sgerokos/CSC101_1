# Ask's the user to enter the number of student's

num = eval(input("Please Enter the Number of Student's: "))

first = 0

second = 0

for i in range(num):
    
# Ask's the user for the score's of the student
    
    score = eval(input("Please Enter the Student's Score's: "))
    
# Compare's current score with first, and second score

if score > first:
    
# New highest score
    
    second = first
    
# Last highest scroe becomes second    
    
    first = score 
    
elif score <= first and score > second:
    
# New second highest scroe    
    
    second = score 
    
# Display's highest and second highest scores to the user

print("The Highest score is " + str(first))

print("The Second Highest Score is " + str(second))