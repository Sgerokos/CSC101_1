def checkPassword(str1):

    countLtr = 0
    
    countDgt = 0

    for ch in str1:

# If the character is a digit increase to count the digit
        
        if ch.isdigit():        
            
            countDgt += 1
            
# If it is alphabetic increase to count the letter

        elif ch.isalpha():      
            
            countLtr += 1

# If it is anything else return false

        else:                  
            
            return False

# Check's if digit's are 2 and count of letter and digit are 8 return true or else false
    
    if (countDgt >= 2 and countLtr + countDgt >= 8):
        
        return True 
    
    else:
        
        return False


def main():

# Ask's the user to input password
    
    pwd = input("Please Enter Your Password: ")
    
    if checkPassword(pwd):
        
# Print's valid if valid or else invalid if not
        
        print("Valid Password")
        
    else:
        
        print("Invalid Password")

main()