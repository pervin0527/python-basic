from random import choice, randint
from turtle import Turtle, Screen, colormode

def draw_square(turtle):
    ### Draw Square
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_dash_line(turtle):
    ### 10 걸음 선을 그리고, 10걸음 간격을 만든다. 15회 수행.
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw_figures(turtle):
    ### 정삼각형, 정사각형, 정오각형, 정육각형, 정칠각형, 정팔각형, 정구각형, 정십각형 그리기.
    ### 도형 각각은 임의의 색상으로 그려져야 한다. 
    ### 각 변의 길이는 100. 
    ### 모든 도형은 서로 겹쳐지며 순서대로 그려진다.
    colors = ["red", "green", "blue", "cyan", "black", "brown", "DarkGrey", "BlueViolet", "DeepPink"]
    for angle in range(3, 11):
        turtle.pencolor(choice(colors))
        degree = 360 / angle
        for _ in range(angle):
            turtle.forward(100)
            turtle.right(degree)

def random_walk(turtle):
    ### 무작위 행보는 turtle이 동,서,남,북쪽으로 무작위로 움직이는 것
    ### 매번 같은 거리만큼 이동한다.
    ### 모든 지점에서 네 방향 중 다음에 향할 방향을 선택할 수 있다.
    ### 움직일 때마다 다른 색상을 선택한다.
    ### 선의 굵기를 굵게 하고, 이동 속도를 더 빠르게 해보자.
    distance = 30
    turtle.speed(7)
    # turtle.width(10)
    turtle.pensize(15)
    
    for _ in range(200):
        direction = 90 * randint(1, 3)
        turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.forward(distance)
        # turtle.right(direction)
        turtle.setheading(direction)

def draw_spiro_graph(turtle):
    ## 반시계 방향으로 돌면서, 반지름이 100인 여러 개의 원을 그리도록 한다.
    ## 각 원의 색상은 무작위로 한다.
    degree = 0
    turtle.speed("fastest")
    while degree < 360:
        turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.circle(100)
        degree += 5
        turtle.setheading(degree)

screen = Screen()
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
colormode(255)

# draw_square(turtle)
# draw_dash_line(turtle)
# draw_figures(my_turtle)
# random_walk(my_turtle)
draw_spiro_graph(my_turtle)

screen.exitonclick()