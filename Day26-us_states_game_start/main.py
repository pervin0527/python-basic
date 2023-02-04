import turtle
import pandas as pd

image = "./blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)

total_states = pd.read_csv("50_states.csv")
states_names = total_states["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)} / 50 States correct.", prompt="What's another state's name??").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_names:
            if state not in guessed_states:
                missing_states.append(state)
        df = pd.DataFrame(missing_states)
        df.to_csv("./states_to_learn.csv")
        break

    if answer_state in states_names:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = total_states[total_states.state == answer_state]
        t.goto(int(data.x), int(data.y))
        t.write(answer_state)
