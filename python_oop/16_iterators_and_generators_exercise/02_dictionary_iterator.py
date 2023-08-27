class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = obj
        self.curr_idx = -1
        self.end_idx = len(obj) - 1
        self.items = list(obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_idx >= self.end_idx:
            raise StopIteration

        self.curr_idx += 1

        return self.items[self.curr_idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
