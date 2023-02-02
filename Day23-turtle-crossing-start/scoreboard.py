from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-220, 250)
        self.show_level()
        
    def show_level(self):
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)