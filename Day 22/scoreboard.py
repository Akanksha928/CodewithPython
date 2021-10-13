from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.setposition(0, 250)
        self.write(f"{self.score_l}:{self.score_r}", align='center', font=("Arial", 20, "normal"))

    def track_score_r(self):
        self.score_l += 1
        self.clear()
        self.write(f"{self.score_l}:{self.score_r}", align='center', font=("Arial", 20, "normal"))

    def track_score_l(self):
        self.score_r += 1
        self.clear()
        self.write(f"{self.score_l}:{self.score_r}", align='center', font=("Arial", 20, "normal"))



