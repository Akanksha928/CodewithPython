import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.title("Turtle Crossing Road Game")

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.check():
        score.increment_score()
        car_manager.speed_up()
    car_manager.generate_cars()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()

