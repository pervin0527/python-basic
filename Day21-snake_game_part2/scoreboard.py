from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.show_score()

    def show_score(self):
        self.write(f"Score : {self.score}", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)