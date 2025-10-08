print("Данные: ")
def read_data():
    return ["  Андрей  ", "  ТЁМА ", "Алекс", "Сангвиний", "Попка Дурак", "аАФаыфайейцфыам"]
print(read_data())
def clean_names(names):
    return [name.strip() for name in names]

def capitalize_names(names):
    return [name.title() for name in names]

def filter_long_names(names, max_length=10):
    return [name for name in names if len(name) <= max_length]

def process_data():
    data = read_data()
    data = clean_names(data)
    data = capitalize_names(data)
    data = filter_long_names(data)
    return data

print("Обработанные данные:" )
result = process_data()
print(result)