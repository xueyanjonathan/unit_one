import turtle
turtle.speed(100)
turtle.pensize(20)
for x in range(3):
    turtle.circle(100)
    turtle.penup()
    turtle.forward(130)
    turtle.pendown()
    turtle.circle(100)
turtle.exitonclick()
