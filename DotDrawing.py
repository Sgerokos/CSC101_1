# Imports turtle library

import turtle

# Import's random library

import random

# defines the distance

def distance (xa, ya, xb, yb):

    distance = ((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)) ** 0.5
	
    return distance 

# Draws the dot's

def drawDot (x, y):

    turtle.penup ()
	
    turtle.goto (x, y)
	
    turtle.pendown ()
	
    turtle.begin_fill ()
	
    turtle.circle (3)
	
    turtle.end_fill ()
 
# Draw's the circle

def drawCircle (x = 0, y = 0, radius = 10):

    turtle.penup ()
	
    turtle.goto (x, y - radius)
	
    turtle.pendown ()
	
    turtle.circle (radius)
    
# Draw's the square   

def drawRectangle (x = 0, y = 0, width = 10, height = 10):

    turtle.penup ()
	
    turtle.goto  (x + width / 2, y + height / 2)
	
    turtle.pendown ()
	
    turtle.right (90)
	
    turtle.forward (height)
	
    turtle.right (90)
	
    turtle.forward (width)
	
    turtle.right (90)
	
    turtle.forward (height)
	
    turtle.right (90)
	
    turtle.forward (width)
    
# Draw's the dot's in the circle

def drawDotsInCircle ():

    i = 0
	
    while i < 10:
	
        x = random.randint (0, 100)
		
        y = random.randint (-50, 50)
		
        if distance (x, y, 50, 0) <= 50:
		
            drawDot (x, y)
			
            i += 1

# Draw's dot's in the square

def drawDotsInSquare ():

    for i in range (10):
	
        x = random.randint (-125, -25)
		
        y = random.randint (-50, 50)
		
        drawDot (x, y)
    
def main ():

    drawRectangle (-75, 0, 100, 100)
	
    drawCircle (50, 0, 50)
	
    drawDotsInCircle ()
	
    drawDotsInSquare ()
	
main()