from turtle import Turtle

class Score(Turtle):

    def __init__(self , x):
        super().__init__()
        self.mark = 0
        self.color("white")
        self.penup()
        self.goto(x, 270)

    def show(self):
        self.clear()
        self.hideturtle()
        self.write(f"{self.mark}", move=False, align="center", font=("Courier",24, "normal"))

    def refresh(self):
        self.mark += 1
        self.show()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("GAME OVER", move=False, align="center", font=("Arial", 24, "normal"))
