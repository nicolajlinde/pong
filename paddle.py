from turtle import Turtle
WIDTH = 5
HEIGHT = 1
SPEED = 20
COLOR = "white"
UP = 180
DOWN = 0


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.paddle = Turtle("square")
        self.add_players(x, y)
        self.speed = SPEED

    def add_players(self, x, y):
        self.shape("square")
        self.color(COLOR)
        self.penup()
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.goto((x, y))

    def up(self):
        paddle_y = self.ycor()
        self.goto(self.xcor(), paddle_y + self.speed)

    def down(self):
        paddle_y = self.ycor()
        self.goto(self.xcor(), paddle_y - self.speed)
