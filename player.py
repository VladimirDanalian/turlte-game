STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_up(self):
        self.fd(15)

    def go_down(self):
        self.backward(15)
    def if_finsh(self):
        self.goto(0, -280)

    def finsh(self):
        if self.ycor() > FINISH_LINE_Y:
            return Turtle
        return False







