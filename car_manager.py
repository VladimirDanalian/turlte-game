from turtledemo.minimal_hanoi import Tower

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle

class CarManager(Turtle):

    def __init__(self):
       self.cars = []
       self.speed = STARTING_MOVE_DISTANCE

    def rodes_up(self):
        for i in range(1,23):
            row = Turtle("square")
            row.penup()
            row.shapesize(stretch_wid=0.05,stretch_len=0.6)
            row.goto(-300+i*30 ,280)

    def rodes_down(self):
        for i in range(1,23):
            row = Turtle("square")
            row.penup()
            row.shapesize(stretch_wid=0.05,stretch_len=0.6)
            row.goto(-300+i*30 ,-280)


    def create_cars(self):
        random_number = random.randint(1,4)
        if random_number == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y= random.randint(-250,250)
            car.goto(300,random_y)
            self.cars.append(car)

    def move_cares(self):
        for car in self.cars:
            car.backward(self.speed)

    def move_cares_faster(self):
        for car in self.cars:
            car.backward(self.speed)
    def speed_up(self):
        self.speed+=2




