import time
from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
score = ScoreBoard()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 30:
        food.refresh()
        snake.extend()
        score.add_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
    for parts in snake.parts[1:]:
        if snake.head.distance(parts) < 10:
            game_on = False
            score.game_over()
screen.exitonclick()
