import time
from turtle import Screen
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.rate)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() <- 320:
        ball.bounce_x()
    if ball.xcor()>380 :
        ball.reset_position()
        scoreboard.l_point()
    if  ball.xcor()<-380 :
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
