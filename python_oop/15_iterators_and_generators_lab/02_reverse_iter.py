class reverse_iter:
    def __init__(self, array):
        self.array = array
        self.idx = len(self.array) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= 0:
            curr_el = self.array[self.idx]
            self.idx -= 1
            return curr_el
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 3, 5, 7])
for item in reversed_list:
    print(item)
