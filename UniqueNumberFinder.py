# Ask's the user to add 10 number's

n = input("Please Enter 10 Number's: ")

# Extracts numbers from the input of the user to add to the list

n = n.split()

n = [int(num) for num in n]

# Bring's the number's from l1 to l2

n2 = []

for i in n:
    
    if i not in n2:
        
        n2.append(i)
        
# Display's the number's list

print("The Number's Are: " , end = "")

for i in range(len(n2)):
    
    print(n2[i], end = "")
    