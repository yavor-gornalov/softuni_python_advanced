# https://judge.softuni.org/Contests/Practice/Index/1935#0

class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
