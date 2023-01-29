from turtle import Turtle, Screen

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def turn_ccw():
    # my_turtle.left(10)
    new_heading = my_turtle.heading() + 10
    my_turtle.setheading(new_heading)

def turn_cw():
    # my_turtle.right(10)
    new_heading = my_turtle.heading() - 10
    my_turtle.setheading(new_heading)

def clear():
    # my_turtle.reset()
    my_turtle.clear()
    my_turtle.home()

my_turtle = Turtle()
my_screen = Screen()

my_screen.listen()
my_screen.onkey(move_forward, "w")
my_screen.onkey(move_backward, "s")
my_screen.onkey(turn_cw, "d")
my_screen.onkey(turn_ccw, "a")
my_screen.onkey(clear, "c")

my_screen.exitonclick()