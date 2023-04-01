# Functions call for main

if __name__ == "__main__":
    
    # Create's an empty list
    
    mylist = []
    
# Ask's the user for there input
    
    user_input = input("\nMenu: A)dd,  R)emove,  F)ind,  P)rint,  Q)uite: ")
    
# Sentinal controlled loop
    
    while(user_input != "Q"):
        
# Add's item to the list
        
        if(user_input == "A"):
            
            item = input("Please Enter The Item To Add To The List: ")
            
            mylist.append(item)
            
# Remove's item from the list
        
        elif(user_input == "R"):
            
            item = input("Please Enter The Item To Remove From The List: ")
            
            mylist.remove(item)
            
# Find's items on the list for the user
        
        elif(user_input == "F"):
            
            item = input("What Item Would You Like To Find In The List: ")
            
            count = mylist.count(item)
            
            if(count==0):
                
                print("" + item + " Is Not On The List.")
                
            else:
                
                print(item, "Found On The List At","Index" , mylist.index(item))
                
# Print's the list's element's
        
        elif(user_input == "P"):
            
            print("List Of The Items")
            
            for i in range(len(mylist)):
                
                print(str(i+1)+". "+mylist[i])
                
# If the user type's an invalid input they will get a message invalid input
        
        else:
            
            print("Invalid Input Please Try Again")
        
# Continues to take the user's input and continue's the loop
        
        user_input = input("\nMenu: A)dd,  R)emove,  F)ind,  P)rint,  Q)uite: ")
    
# Print's a thank you message and exit's
    
print("Thank You Come Again!!!")
