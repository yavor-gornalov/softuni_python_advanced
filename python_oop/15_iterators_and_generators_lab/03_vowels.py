class vowels:
    VOWELS_LIST = "AEIOUY"

    def __init__(self, string: str):
        self.string = string
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.string):
            raise StopIteration
        current_element = self.string[self.idx]
        self.idx += 1

        if current_element.upper() in self.VOWELS_LIST:
            return current_element
        return vowels.__next__(self)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
