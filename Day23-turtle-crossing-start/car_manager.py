import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

BOUNDARY_X = (100, 300)
BOUNDARY_Y = (-200, 200)


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[random.randint(0, len(COLORS)-1)])
            car.penup()
            car.goto(300, random.randrange(BOUNDARY_Y[0], BOUNDARY_Y[1], 10))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.current_speed)

    def speed_up(self):
        self.current_speed += MOVE_INCREMENT