import random
from turtle import Turtle, Screen, colormode

colormode(255)
colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

initial_x, initial_y = -230, -100
turtles = [Turtle(shape="turtle") for _ in range(7)]
for idx, tt in enumerate(turtles):
    print(id(tt)) ## loop문으로 instance를 생성해도, 주소값이 전부 다르다.
    tt.penup()
    tt.goto(x=initial_x, y=initial_y)
    tt.color(colors[idx])
    initial_y += 40

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for tt in turtles:
        if tt.xcor() > 230:
            is_race_on = False
            winner_color = tt.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lose. The {winner_color} turtle is the winner.")

        random_distance = random.randint(0, 10)
        tt.forward(random_distance)

my_screen.exitonclick()