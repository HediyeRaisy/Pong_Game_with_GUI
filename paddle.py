from turtle import Turtle
UP = 90
DOWN = 270

#Class for making paddles and movement of them
class Paddle():

    def __init__(self):

        self.squares = []
        self.x = -380

    def make(self):
        s = 40
        for i in range(0, 4):
            self.squares.append(Turtle(shape="square"))
            self.squares[i].penup()
            self.squares[i].color("white")
            self.squares[i].goto(self.x, s)
            self.squares[i].setheading(90)
            self.squares[i].speed("fastest")

            s += -20

    def move(self):
        for square in range(3, 0, -1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)
        # self.squares[0].forward(20)


    def up(self):
        # if self.squares[0].heading() != DOWN:
        # self.squares[0].forward(20)
        self.move()
        self.squares[0].forward(20)
        self.move()
        self.squares[0].forward(20)

    def down(self):
        # if self.squares[0].heading() != UP:
        # self.squares[0].backward(20)
        self.move()
        self.squares[0].backward(20)
        self.move()
        self.squares[0].backward(20)
