def goida_repeat(times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
                print(f"Номер гойды {i+1}! {result}")
            return result
        return wrapper
    return decorator

@goida_repeat(times=3)
def goida_funct(goida):
    return f"{goida}!"

goida_funct("Гойда!!")