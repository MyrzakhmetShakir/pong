from turtle import Turtle, Screen
from paddle import Paddle
from paddle_comp import PaddleComp
from line import Line
from ball import Ball
import time
from score import Score





screen = Screen()

screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Ping Pong Myrzakhmet Copyright")
screen.tracer(0)

num = int(screen.textinput("Max value", "What is maximum score to play? "))
print(type(num))

line = Line()
line.line_many()


paddle_mine = Paddle()
paddle_comp = PaddleComp()
ball = Ball()
score_sc1 = 0
score_sc2 = 0
score_1 = Score((-80, 240), score_sc1)
score_2 = Score((80, 240), score_sc2)



screen.title("Ping Pong Myrzakhmet Copyright")
screen.listen()
screen.onkey(paddle_mine.up, "Up")
screen.onkey(paddle_mine.down, "Down")
screen.onkeypress(paddle_comp.up, "w")
screen.onkeypress(paddle_comp.down, "s")


is_game_on = True

while is_game_on:
    time.sleep(0.01)
    screen.update()
    ball.first_move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.collision_wall()
    if ball.distance(paddle_comp) < 50 and ball.xcor() > 460:
        ball.collision_paddle_comp()
    elif ball.distance(paddle_mine) < 50 and ball.xcor() < -460:
        ball.collision_paddle_comp()
    elif ball.xcor() >= 500:
        score_sc1 += 1
        score_1.clear()
        score_1 = Score((-80, 240), score_sc1)
        ball.res()
    elif ball.xcor() <= -500:
        score_sc2 += 1
        score_2.clear()
        score_2 = Score((80, 240), score_sc2)
        ball.res()
    if score_sc1 == num:
        score_3 = Score((0, 0), "Left is winner")
        is_game_on = False
    elif score_2 == num:
        score_4 = Score((0, 0), "Right is winner")
        is_game_on = False







screen.exitonclick()