from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.write(f"Score = {self.num}", False, 'center', font=("Courier", 20, "normal"))
        self.hideturtle()

    def add_score(self):
        self.num += 1
        self.clear()
        self.write(f"Score = {self.num}", False, 'center', font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, 'center', font=("Arial", 15, "normal"))
