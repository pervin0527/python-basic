from turtle import Turtle

INIT_X_COORDS = [0, -20, -40] ### 상수
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        self.snake = []
        self.create_snake() ### (놓친 부분)객체를 만들 때, snake를 만들게 해준다.
        self.head = self.snake[0]

    def __len__(self):
        return len(self.snake)

    def create_snake(self):
        for x_coord in INIT_X_COORDS:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=x_coord, y=0)
            self.snake.append(turtle)

    def move(self): ### 생성한 객체를 main.py에서 움직이려고 하니 "object is not subscriptable" 에러가 발생했다. 객체 내의 메서드로 움직이게 해야한다.
        for idx in range(len(self.snake)-1, 0, -1):
            x, y = self.snake[idx-1].xcor(), self.snake[idx-1].ycor()
            self.snake[idx].goto(x, y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)