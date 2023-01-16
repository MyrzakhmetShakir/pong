from turtle import Turtle

class PaddleComp(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.setx(480)
        self.sety(0)
        self.shape("square")
        self.shapesize(0.5, 4)
        self.setheading(90)
        self.color("white")


    def move(self):
        self.clear()
        self.speed(2)
        self.goto(480, 250)
        self.goto(480, -250)
        self.goto(480, 250)

    def up(self):
        self.forward(60)

    def down(self):
        self.backward(60)