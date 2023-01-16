from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.poss = 290
        self.speed("fastest")


    def line_many(self):
        self.speed("fastest")
        for _ in range(18):
            line = Turtle()
            line.speed("fastest")
            line.penup()
            self.poss -= 30
            line.sety(self.poss)
            line.setx(0)
            line.color("yellow")
            line.shape("square")
            line.shapesize(0.8, 0.1)