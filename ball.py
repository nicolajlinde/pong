from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move
        self.goto(x, y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.8
        print(self.move_speed)

    def reset_pos(self):
        self.home()
        self.move_speed = 0.1
        self.x_bounce()

