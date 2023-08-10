# https://judge.softuni.org/Contests/Practice/Index/1935#3

class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, new_quantity):
        free_space = self.status()
        if free_space >= new_quantity:
            self.quantity += new_quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
