from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # self.shapesize(, 0.8)
        self.color("yellow")
        self.speed("fastest")
        self.head = random.randint(135,225)
        self.setheading(self.head)

    def move(self):
        self.forward(20)



