from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration not in self.decorations:
            return False

        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        return next((x for x in self.decorations if x.decoration_type == decoration_type), "None")

    @property
    def comfort(self):
        return sum([d.comfort for d in self.decorations])

    @property
    def count(self):
        return len(self.decorations)
