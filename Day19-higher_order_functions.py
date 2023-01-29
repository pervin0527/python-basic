## 고차함수(higher order functions)
## 다른 함수를 인수로 받아들이는 함수. ex) map(), filter(), reduce()

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2 ## python에서 나눗셈의 결과 값은 무조건 실수

def calculator(n1, n2, func): ## higher order function
    return func(n1, n2)

print(calculator(2, 3, multiply))
print(calculator(1, 1, add))