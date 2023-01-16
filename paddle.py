import random
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setx(-480)
        self.sety(0)
        self.speed("fastest")
        self.hideturtle()
        self.shape("square")
        self.shapesize(0.5, 4)
        self.setheading(90)
        self.color("white")

        self.showturtle()


    def up(self):
        self.forward(60)

    def down(self):
        self.backward(60)