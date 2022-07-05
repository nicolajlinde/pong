from turtle import Screen
from setup import Setup
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

setup = Setup()
screen = Screen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# Player 1 (R)
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
# Player 2 (L)
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision on upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision on right and left paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect collision if ball outside the x-axis (player score point)
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

setup.exit()




