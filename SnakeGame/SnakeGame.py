import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.title('Snake Game')
screen.bgcolor('black')

screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
print(snake.head.position())
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()
    for seg in snake.segment[1:]:
        if snake.head.distance(seg)<10:
            scoreboard.reset()


screen.exitonclick()
