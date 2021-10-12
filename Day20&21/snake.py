from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]
move = 20


class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for item in positions:
            self.add_part(item)

    def add_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.parts.append(new_part)

    def extend(self):
        self.add_part(self.parts[-1].position())

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.parts[0].forward(move)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
