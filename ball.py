from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.sety(0)
        self.setx(0)
        self.shape("circle")
        self.color("red")
        self.shapesize(1)
        self.x_move = 4
        self.y_move = 4

    def first_move(self):
        self.penup()
        self.speed("slowest")
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_wall(self):
        self.y_move *= -1

    def collision_paddle_comp(self):
        if self.x_move > 0:
            self.x_move += 0.5
        elif self.x_move < 0:
            self.x_move -= 0.5
        self.x_move *= -1
        print(self.x_move)

    def res(self):
        self.sety(0)
        self.setx(0)
        if self.x_move > 0:
            self.x_move = 4
        else:
            self.x_move = -4
        if self.y_move > 0:
            self.y_move = 4
        else:
            self.y_move = -4
        self.x_move *= -1
        self.y_move *= -1