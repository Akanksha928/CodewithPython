from turtle import Screen, Turtle
from paddle_and_ball import Paddle, Ball
from scoreboard import ScoreBoard
turtle = Turtle()
screen = Screen()
screen.tracer(0)
ball = Ball()
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.bgcolor("black")

l_paddle = Paddle()
l_paddle.position(-350, 0)
r_paddle = Paddle()
r_paddle.position(350, 0)
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True

# Keeping Track of game
while game_is_on:
    screen.update()
    ball.move()

    # Check collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision_y()

    # Check collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.collision_x()

    # Track Score for right paddle
    if ball.xcor() > 390:
        ball.reset_pos()
        score.track_score_r()

    # Track Score for right paddle
    if ball.xcor() < -390:
        ball.reset_pos()
        score.track_score_l()

screen.exitonclick()
