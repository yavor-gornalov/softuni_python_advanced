# https://judge.softuni.org/Contests/Compete/Index/1937#0

from typing import List


class Vet:
    animals: List[str] = []
    space: int = 5

    def __init__(self, name: str) -> None:
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name):
        if self._space_available > 0:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name):
        for animal in self.animals:
            if animal == animal_name:
                self.animals.remove(animal)
                Vet.animals.remove(animal)
                return f"{animal} unregistered successfully"
        return f"{animal_name} not in the clinic"

    @property
    def _space_available(self):
        return Vet.space - len(Vet.animals)

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {self._space_available} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
