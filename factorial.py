from functools import reduce

num = int(input("Введите число , пожалуйста!\n"))

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(factorial(num))