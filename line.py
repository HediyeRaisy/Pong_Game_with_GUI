from turtle import Turtle

# Function for drawing the line in the middle
def draw_line():
    line = Turtle()
    line.color("white")
    line.penup()
    line.right(90)
    line.penup()
    line.goto(0, 290)
    line.hideturtle()
    c = 1
    while True:
        if c % 2 == 1:
            line.pendown()
            line.forward(20)
            line.penup()
        else:
            line.forward(20)

        if line.ycor() < -270:
            break
        c += 1