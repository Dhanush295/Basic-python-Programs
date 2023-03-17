from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.total_cars = []

    def create_car(self):
        random_cars = random.randint(1, 6)
        if random_cars == 1:
            cars = Turtle("square")
            cars.color(random.choice(COLORS))
            cars.penup()
            cars.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            cars.goto(280, random_y)
            self.total_cars.append(cars)

    def move_cars(self):
        for cars in self.total_cars:
            cars.backward(MOVE_INCREMENT)


