###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from random import choice
from turtle import Turtle, Screen, colormode

def extract_color_list():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(new_color)

    return rgb_colors


def draw_spot_painting(turtle, color_list):
    turtle.setheading(225)
    turtle.penup()
    turtle.forward(300)
    turtle.setheading(0)

    start_x, start_y = turtle.position()
    for i in range(10):
        turtle.penup()
        turtle.setposition(start_x, start_y + (50 * i))
        for _ in range(10):
            turtle.dot(20, choice(color_list))
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()


colors = extract_color_list()
colors = colors[3:]
colormode(255)

my_turtle = Turtle()
my_screen = Screen()
my_turtle.speed("fastest")

draw_spot_painting(my_turtle, colors)   
my_screen.exitonclick()