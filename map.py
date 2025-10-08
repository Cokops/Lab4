numbers = [2,4,6,8,10]

print("Исходный список: ")
for i in numbers:
    print(i,end=" ", )

print()

def square(x):
    return x * x
def duo(x):
    return x * 2
def delenie(x):
    return x / 2

print("Умножение на 2: ")
result = map(duo, numbers)
print(list(result))

print("Деление на 2: ")
result = map(delenie, numbers)
print(list(result))


print("Возведение в квадрат: ")
result = map(square, numbers)
print(list(result))