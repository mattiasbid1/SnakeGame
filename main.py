from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes of doom")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
snooze = 0.1

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while True:
    time.sleep(snooze)
    screen.update()
    snake.move_snake()

    if snake.head.distance(food) < 15:
        snake.grow_snake(1)
        food.respawn()
        score.add_score()
        snooze *= 0.95

    if not snake.is_alive():
        score.restart()
        snake.restart()
        snooze = 0.1
        food.respawn()

screen.exitonclick()
