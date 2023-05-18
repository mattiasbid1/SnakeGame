from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = "center"
SCORE_TEXT = "Score: "


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.clear()
        self.write(SCORE_TEXT + str(self.score), font=FONT, align=ALIGNMENT)
