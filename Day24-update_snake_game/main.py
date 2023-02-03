import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) ### screen의 애니메이션을 끈다.

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up") ### higher order function의 인수로 받는 함수는 괄호를 쓰지 않는다.(실수함)
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

food = Food()
score = Score()

### 움직이게 만들기
is_game_on = True
while is_game_on:
    screen.update() ### screen.tracer()가 꺼져 있으면, update()를 통해 애니메이션을 갱신해줘야 한다.
    time.sleep(0.1) ### 화면 갱신에 delay를 줘서 갱신 횟수를 조정.
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
    
screen.exitonclick()