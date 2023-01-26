## attributes : 클래스가 가지고 있는 변수
## methods : 클래스가 가지고 있는 함수
## class : 객체를 만들기 위한 청사진. 설계.
## object : 클래스를 기반으로 제작한 것.

# import turtle

# turtle1 = turtle.Turtle() ## 객체 생성
# print(turtle1)
# turtle1.shape("turtle")
# turtle1.color("coral")
# turtle1.forward(100)

# my_screen = turtle.Screen() ## 객체 생성
# print(my_screen.canvheight) ## 객체가 가진 attribute에 접근한다.
# my_screen.exitonclick() ## 객체가 가진 method에 접근.

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)