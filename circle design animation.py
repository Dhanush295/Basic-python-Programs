import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.speed(15)

def ran():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_rgb = (r, g, b)
    return ran_rgb


def draw_spirograph(size_of_gap):
    for i in range(int(360/ size_of_gap)):
        tim.color(ran())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

Screen().exitonclick()

tim = Screen()










