from turtle import Turtle
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-235, 260)
        self.point = 0
        self.color("black")

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.point}", align="center", font=FONT)
        self.point +=1
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center",font=FONT)
