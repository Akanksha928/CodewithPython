from turtle import Turtle
from turtle import Screen
import turtle
import random
turtle.colormode(255)

tim = Turtle()

tim.shape("turtle")

colorlist = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),(98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83), (245, 205, 7), (35, 88, 88), (103, 24, 56)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed(0)
tim.hideturtle()

for i in range(10):
    for j in range(10):
        colour = random.choice(colorlist)
        tim.pencolor(colour)
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    tim.backward(50*10)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

screen = Screen()
screen.exitonclick()
