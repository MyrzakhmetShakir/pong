from turtle import Turtle

class Score(Turtle):
    def __init__(self, position, score):
        super().__init__()
        self.hideturtle()
        self.score = score
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", align="center", font=("Arial", 25, "normal", "bold"))



