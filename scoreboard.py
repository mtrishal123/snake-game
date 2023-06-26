from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.ht()
        self.score = 0
        self.score_message()

    def update_score(self):
        self.score += 1
        self.clear()
        self.score_message()

    def score_message(self):
        self.write(align=ALIGNMENT, arg=f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(align=ALIGNMENT, arg="Game Over.", font=FONT)