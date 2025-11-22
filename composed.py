def compose(f, g):
    return lambda x: f(g(x))

def add_num(x):
    return x + 5

def double(x):
    return x * 2

composed = compose(double, add_num)

print(composed(50))