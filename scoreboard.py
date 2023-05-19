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
        self.high_score = self.handle_score()
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.handle_score(mode="w")
        self.write(SCORE_TEXT + str(self.score) + " High score: " + str(self.high_score), font=FONT, align=ALIGNMENT)

    def handle_score(self, mode="r"):
        with open("high_score.txt", mode=mode) as file:
            if mode == "r":
                return int(file.read())
            elif mode == "w":
                file.write(str(self.high_score))
            else:
                pass
