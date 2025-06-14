import time
from turtle import Screen


from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
game_car = CarManager()
player = Player()
score = Scoreboard()
score.show_score()

screen.listen()
screen.onkey(player.move_forward, "Up")
game_is_on = True
cars = []
loop = 1
while game_is_on:

    if loop % 8==0:
        game_car.create_car()
    for car in game_car.all_cars:
        if car.distance(player) < 30:
            score.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.reset_player()
        game_car.speed_increment()
        score.show_score()
    game_car.move()
    time.sleep(0.1)
    screen.update()
    loop += 1
screen.exitonclick()