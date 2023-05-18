from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.grow_snake(3, "yes")
        self.head = self.snake_parts[0]

    def grow_snake(self, amount, fresh="no"):
        for part in range(amount):
            dist = part
            part = Turtle("square")
            part.color("white")
            part.penup()
            if fresh == "no":
                part.goto(500, 500)
            else:
                part.goto(part.xcor() - (20 * dist), part.ycor())
            self.snake_parts.append(part)

    def move_snake(self):
        for seg in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[seg - 1].xcor()
            new_y = self.snake_parts[seg - 1].ycor()
            self.snake_parts[seg].goto(new_x, new_y)
        self.snake_parts[0].forward(20)

    def is_alive(self):
        for part in self.snake_parts[1:]:
            if self.head.distance(part) < 10:
                return False

        x_cur = self.head.xcor()
        y_cur = self.head.ycor()

        if 285 > x_cur > -285 and 285 > y_cur > -285:
            return True
        else:
            return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
