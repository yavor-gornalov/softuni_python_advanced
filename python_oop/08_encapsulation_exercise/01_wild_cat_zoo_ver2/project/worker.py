from abc import ABC


class Worker(ABC):
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def get_worker_type(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
