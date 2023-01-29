from turtle import Turtle, Screen

def move_forwards():
    my_turtle.forward(10)

my_turtle = Turtle()
my_screen = Screen()

my_screen.listen() ## 이벤트를 듣기 시작한다.

## 특정 키가 입력될 때 동작하는 함수.
## 함수가 다른 함수의 인자로 전달될 때는 괄호가 사용되지 않는다. move_forwards() <--- XX
my_screen.onkey(move_forwards, key="space")

my_screen.exitonclick()