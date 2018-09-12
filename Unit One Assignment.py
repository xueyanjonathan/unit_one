import turtle

turtle.speed(100)
#draw a circle to resemble the face and color in it
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

#move the turtle up to draw the mouth
turtle.left(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()

#draw the mouth and fill in color
turtle.right(150)
turtle.fillcolor("pink")
turtle.begin_fill()
for x in range(3):
    turtle.left(120)
    turtle.forward(80)
turtle.end_fill()

#move the turtle up to draw the nose
turtle.left(150)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.right(90)

#draw the nose
turtle.fillcolor("red")
turtle.begin_fill()
for x in range(2):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
turtle.end_fill()

#move the turtle up to draw the eyes
turtle.left(90)
turtle.penup()
turtle.forward(150)

#make a function to draw the eyes
def drawaneye():
    turtle.fillcolor("white")
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(30)
        turtle.left(45)
    turtle.end_fill()

#draw the left eye
turtle.right(90)
turtle.forward(50)
turtle.pendown()
drawaneye()



turtle.exitonclick()