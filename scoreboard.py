from turtle import Turtle
ALIGHNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=220)
        self.write(self.l_score, align=ALIGHNMENT,
                   font=FONT)
        self.goto(x=100, y=220)
        self.write(self.r_score, align=ALIGHNMENT,
                   font=FONT)

    def increase_right_score(self):
        self.r_score += 1
        self.update_score()

    def increase_left_score(self):
        self.l_score += 1
        self.update_score()
