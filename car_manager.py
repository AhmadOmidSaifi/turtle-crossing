from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]



class CarManager():

    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
    def speed_increment(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(300, random.randint(-280, 280))
        self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.forward(self.STARTING_MOVE_DISTANCE)


