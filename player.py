from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.move_forward()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_forward()
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    def reset_player(self):
        self.goto(STARTING_POSITION)

