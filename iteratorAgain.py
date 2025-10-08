x = int(input("Введите число для перебора: \n"))


class classIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration
        

print("Результат перебора: ")
for num in classIterator(x):
    print(num,end=" ")