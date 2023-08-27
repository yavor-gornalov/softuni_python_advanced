class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number - 1:
            raise StopIteration

        self.idx += 1

        return self.sequence[self.idx % len(self.sequence)]


class sequence_repeat_old:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_count = 0
        self.current_idx = -1
        self.end_idx = len(self.sequence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count >= self.number:
            raise StopIteration
        if self.current_idx >= self.end_idx:
            self.current_idx = -1

        self.current_count += 1
        self.current_idx += 1

        return self.sequence[self.current_idx]


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
