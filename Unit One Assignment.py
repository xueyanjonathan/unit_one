# Jonathan Lin
# 9/13/2018
# Unit One Assignment
# Draw a face using functions and loops in Python

import turtle

turtle.speed(100)
# draw a circle to resemble the face and color in it
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

# move the turtle up to draw the mouth
turtle.left(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()

# draw the mouth and fill in color
turtle.right(150)
turtle.fillcolor("pink")
turtle.begin_fill()
for x in range(3):
    turtle.left(120)
    turtle.forward(80)
turtle.end_fill()

# move the turtle up to draw the nose
turtle.left(150)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.right(90)

# draw the nose
turtle.fillcolor("red")
turtle.begin_fill()
for x in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
turtle.end_fill()

# move the turtle up to draw the eyes
turtle.left(90)
turtle.penup()
turtle.forward(120)

# make a function to draw the eyes
def drawaneye():
    turtle.fillcolor("white")
    turtle.begin_fill()
    for x in range(12):
        turtle.forward(15)
        turtle.left(30)
    turtle.end_fill()
    turtle.pendown()

# draw the left eye
turtle.right(90)
turtle.forward(50)
turtle.pendown()
drawaneye()

# move the turtle to prepare to draw the right eye
turtle.penup()
turtle.left(180)
turtle.forward(115)
turtle.right(180)
turtle.pendown()

# draw the right eye
drawaneye()


turtle.exitonclick()