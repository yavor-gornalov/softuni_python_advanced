from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.get_animal_type()} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.get_worker_type()} hired successfully"

    def fire_worker(self, worker_name):
        worker = self.__get_item_by_attr("name", worker_name, self.workers)
        if not worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_salaries = sum([x.salary for x in self.workers])
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tending_cost = sum([x.money_for_care for x in self.animals])
        if self.__budget < tending_cost:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tending_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        if amount > 0:
            self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        for animal_type in ["Lion", "Tiger", "Cheetah"]:
            collection = [x for x in self.animals if x.get_animal_type() == animal_type]
            if not collection:
                continue
            result.append(f"----- {len(collection)} {animal_type}s:")
            [result.append(str(x)) for x in collection]
        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        for worker_type in ["Keeper", "Caretaker", "Vet"]:
            collection = [x for x in self.workers if x.get_worker_type() == worker_type]
            if not collection:
                continue
            result.append(f"----- {len(collection)} {worker_type}s:")
            [result.append(str(x)) for x in collection]
        return "\n".join(result)

    # HELPERS
    @staticmethod
    def __get_item_by_attr(attr, value, collection):
        for item in collection:
            if getattr(item, attr, None) == value:
                return item
