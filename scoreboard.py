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
        self.high_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.score_message()

    def score_message(self):
        self.write(align=ALIGNMENT, arg=f"Score: {self.score} High Score: {self.high_score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(align=ALIGNMENT, arg="Game Over.", font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
