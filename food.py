import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.goto(400, 400)
        self.respawn()

    def respawn(self):
        x_rand = random.randint(-14, 14) * 20
        y_rand = random.randint(-14, 14) * 20
        self.goto(x_rand, y_rand)
