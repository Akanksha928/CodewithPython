from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-260, 250)
        self.num = 0
        self.write(f"Score: {self.num}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 12, "normal"))

    def increment_score(self):
        self.num += 1
        self.clear()
        self.write(f"Score: {self.num}", font=FONT)
