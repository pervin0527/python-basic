from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        self.segments = []
        self.create_snake() ### (놓친 부분)객체를 만들 때, snake를 만들게 해준다.
        self.head = self.segments[0]

    def __len__(self):
        return len(self.segments)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self): ### 생성한 객체를 main.py에서 움직이려고 하니 "object is not subscriptable" 에러가 발생했다. 객체 내의 메서드로 움직이게 해야한다.
        for idx in range(len(self.segments)-1, 0, -1):
            x, y = self.segments[idx-1].xcor(), self.segments[idx-1].ycor()
            self.segments[idx].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

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

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]