# https://judge.softuni.org/Contests/Practice/Index/1935#1

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health = max(self.health - damage, 0)
        return f"{self.name} was defeated" if not self.health else None

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
