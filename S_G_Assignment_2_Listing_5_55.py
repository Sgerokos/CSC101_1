# Imports turtle module

import turtle  
   
screen = turtle.Screen() 
   
# Create's a turtle object 

pen = turtle.Turtle() 

# The size of the board, along with the screen size, and size of each square can be altered here

BOARD_SIZE = 8

SQUARESIZE = 60

SCREENSIZE = BOARD_SIZE * SQUARESIZE * 2

# Draw's the square

def draw(): 
   
  for a in range(4): 
    
    pen.forward(SQUARESIZE) 
    
    pen.left(90) 
    
   
  pen.forward(SQUARESIZE)
   
if __name__ == "__main__" : 
    
# Set's the screen 
  
    screen.setup (SCREENSIZE, SCREENSIZE) 
       
# The turtle's object speed is controlled from here 
    
    pen.speed(25) 
       
# Loops for the board
    
    for a in range(BOARD_SIZE): 
       
# Prepare's the pen and set's the position
      
      pen.up() 
      
      pen.setpos(-1 * (SCREENSIZE / 2), SQUARESIZE * a) 
       
# The board will be prepared to be drawn
      
      pen.down() 
      
      for b in range(BOARD_SIZE): 
       
# The color's are set and can be altered here 
        
        if (a + b)% 2 == 0: 
          
          col ='black'
       
        else: 
          
          col ='white' 
        
        pen.fillcolor(col) 
       
# Fill's the color
        
        pen.begin_fill() 

        draw() 
        
        pen.end_fill() 
       
# Hide's the turtle 
    
    pen.hideturtle() 

