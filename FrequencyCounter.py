# Ask's the user to input a number from 1 to 100 than splits the number

n = input("Please Enter Integer's Between 1 and 100: ")

# Extracts numbers from the input of the user to add to the list

n = n.split()

n = [int(num) for num in n]

# Starts a list of 100 numbers with 0

c = 100 * [0]

# Counts the appearance of each number in the list

for i in range(len(n)):
    
    c[n[i] - 1] += 1
    
# Displays the appearance of each number

for i in range(len(c)):
    
    if c[i] > 0:
        
        if c[i] == 1:
            
            print(i + 1, "Appears 1 Time")
            
        else:
            
            print(i + 1, "Appears", c[i], "Times")