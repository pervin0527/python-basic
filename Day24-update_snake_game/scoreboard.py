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

        with open("./data.txt", "r") as f:
            self.high_score = int(f.readline())
            print(self.high_score)
        f.close()

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", "w") as f:
                f.write(str(self.high_score))
            f.close()

        self.score = 0
        self.update_score()