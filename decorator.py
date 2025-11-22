def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызываем функцию: {func.__name__}")
        print(f"Аргументы: {args}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершилась")
        return result
    return wrapper

def add_numbers(x,y):
    return x + y

add_numbers = decorator(add_numbers)

result = add_numbers(5,10)
