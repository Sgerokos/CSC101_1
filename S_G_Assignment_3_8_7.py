# Return's the number associated with an alphabet

def getNum(uppercaseLetter):

    numMap = (("A","B","C"),("D","E","F"),("G","H","I"),("J","K","L"),\
	
    ("M","N","O"),("P","Q","R","S"),("T","U","V"),("W","X","Y","Z"))

# Take's each inner tuple

    for num in numMap:

# Take's each alphabet in inner tuple
        
        for letter in num:

# Check's whether alphabet is equal to alphabet passed
            
            if letter == uppercaseLetter:

# Return's the assoicated number
                
                return numMap.index(num) + 2

# Get's the new phone number

def letterToNum(word):

# Gte's number's associated with letters
    
    pNum = ""

# Take's each character

    for letter in word:

# Get's number associated with the letter
        
        pNum += str(getNum(letter.upper()))
		
    return pNum
    
def main():

# Ask's the user to input a phone number with or without dashes then read's the input and splits

    phoneNum=input(" Please Enter a Phone Number With or Without Dashes: ").split("-")
    
# Look's to see if it contains the symbol

    if len(phoneNum) == 3:
	
        print("%s-%s-%s" %(phoneNum[0],phoneNum[1],letterToNum(phoneNum[2])))

# Look's to see if it is with or without dashes

    else:
	
        print("%s%s" %(phoneNum[0][:4],letterToNum(phoneNum[0][4:])))

if __name__ == "__main__":

    main()