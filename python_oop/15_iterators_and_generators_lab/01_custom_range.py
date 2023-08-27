class custom_range:
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            temp = self.current
            self.current += 1
            return temp
        else:
            raise StopIteration


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
