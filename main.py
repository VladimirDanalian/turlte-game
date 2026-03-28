import time
from turtle import Screen
from player1 import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
car.rodes_up()
car.rodes_down()
screen.listen()

screen.onkey(player.go_up,"Up")
screen.onkey(player.go_down,"Down")
game_is_on = True
i=0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cares_faster()
    for i in car.cars:
        if i.distance(player) < 20:
            game_is_on = False
    if player.finsh():
        player.if_finsh()
        car.speed_up()



screen.exitonclick()
