from turtle import Turtle, Screen
from paddle import Paddle
from line import draw_line
import time
from ball import Ball
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
user_paddle = Paddle()
user_paddle.make()


paddle = Paddle()
paddle.x = 370
paddle.make()
draw_line()
ball = Ball()

mark1 = Score(-30)
mark2 = Score(30)

game_is_on = True
paddle.up()
c = 1
screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")
#code for playing with another user
screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")

while game_is_on:
    # ball.pendown()
    mark1.show()
    mark2.show()
    ball.move()
    screen.update()
    time.sleep(0.06)
    #code for playing with computer
    # if paddle.squares[0].ycor() > 270:
    #     paddle.down()
    #     c = 0
    # elif paddle.squares[0].ycor() < -270:
    #     paddle.up()
    #     c = 1
    # else:
    #     paddle.move()
    #     if c == 1:
    #         paddle.squares[0].forward(20)
    #     else:
    #         paddle.squares[0].backward(20)

    for i in range(0, 3):
        if user_paddle.squares[i].distance(ball) < 20:

            ball.setheading(ball.heading() * -1 - 180)
            ball.move()
            break

    for i in range(0, 3):
        if paddle.squares[i].distance(ball) < 20:
            # head1 = ball.heading() +90
            ball.setheading(ball.heading() * -1 - 180)
            ball.move()
            break
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(ball.heading() * -1 )
    if ball.xcor()  > 380 :
        mark1.refresh()
        ball.hideturtle()
        ball = Ball()
    elif ball.xcor() < -380:
        mark2.refresh()
        ball.hideturtle()
        ball = Ball()

screen.exitonclick()
