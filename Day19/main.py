from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput("Welcome to the Turtle Race", "Place your bets on the turtle: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
turtles = ["mini", "moni", "tim", "cook", "tom", "zack"]
race_is_on = False
# Creating a list of turtle objects in the turtles list
for i in range(len(turtles)):
    turtles[i] = Turtle()
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])

positions = [-70, -40, -10, 20, 50, 80]
# Positioning the turtles
for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].goto(x=-230, y=positions[i])

if user_bet:
    race_is_on = True

while race_is_on:
    for i in turtles:
        if i.xcor() > 230:
            winner = i.color()
            if user_bet.lower() == i.pencolor():
                print(f"You won! The winning color is {i.pencolor()}.")
                race_is_on = False
            else:
                print(f"You lost! The winning color was {i.pencolor()}.")
                race_is_on = False

        i.forward(random.randint(0, 10))

screen.exitonclick()

