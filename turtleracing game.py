import turtle
from turtle import Turtle, Screen
import random
clr_list = ["yellow", "green", "black", "pink", "blue", "red"]
y_position = [-80, -50, -20, 10, 40, 70]

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make a bet", prompt="which turtle will win the race, Make a Guess?: ")
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(clr_list[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(new_turtle)

race_start = False

if user_input:
    race_start = True


while race_start:
    for turtle in turtle_list:

        if turtle.xcor() > 230:
            race_start = False
            winner = turtle.pencolor()
            if user_input == winner:
                print(f"You won!. the winner color is {winner}")
            else:
                print(f"You loose!. the winner color is {winner}")


        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()