with open('students.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')
data = [line.strip().split(',') for line in lines[1:]]

print("Исходные данные:")
for row in data:
    print(row)

moscow_students = list(filter(lambda row: row[3] == 'Moscow', data))

print("\nСтуденты из Москвы:")
for student in moscow_students:
    print(student)

def add_status(row):
    grade = int(row[2])
    if grade >= 90:
        status = "Отличник"
    elif grade >= 80:
        status = "Хорошист"
    else:
        status = "Удовлетворительно"
    return row + [status]

students_with_status = list(map(add_status, data))

print("\nСтуденты со статусом:")
for student in students_with_status:
    print(student)