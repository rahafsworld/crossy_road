from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("slategrey")

turtle = Turtle()
turtle.shape('square')
turtle.shapesize(stretch_wid=0.1, stretch_len=0.1)
turtle.penup()
turtle.color("lightsteelblue")
turtle.goto(-300, 300)
turtle.pendown()


def horizontal():
    turtle.forward(600)
    turtle.right(90)


def vertical():
    turtle.forward(600)
    turtle.right(90)