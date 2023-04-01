# Imports turtle module

  
import turtle


turtle.showturtle()

# turns the background color to black

turtle.bgcolor("black")

# Designing the letter S

turtle.pensize(5)
turtle.color("blue")

turtle.backward(50)


turtle.right(90)
turtle.forward(50)

turtle.left(90)
turtle.forward(50)

turtle.right(90)
turtle.forward(50)

turtle.right(90)
turtle.forward(50)

# Moving the pen next to the letter S
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()

# Drawing the G
turtle.pensize(10)
turtle.color("red")
turtle.forward(50)
turtle.left(90)

turtle.forward(50)
turtle.left(90)

turtle.forward(50)
turtle.left(90)

turtle.forward(20)
turtle.right(90)
turtle.forward(15)
turtle.left(90)
turtle.left(90)
turtle.forward(30)

# re position pen

turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.left(20)

# Draw Star

turtle.pensize(8)
turtle.color("grey")

turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)