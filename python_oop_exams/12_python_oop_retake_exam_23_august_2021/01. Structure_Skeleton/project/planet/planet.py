class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    def attach_items(self, items: str):
        self.items = [x for x in items.split(", ")]
