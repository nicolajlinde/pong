from turtle import Screen
WIDTH = 800
HEIGHT = 600
TITLE = "Pong"
BG_COLOR = "black"


class Setup:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.title(TITLE)
        self.screen.bgcolor(BG_COLOR)
        self.screen.tracer(0)

    def exit(self):
        self.screen.exitonclick()

