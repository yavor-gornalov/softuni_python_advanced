from project.animal import Animal
from project.dog import Dog
from project.cat import Cat

a = Animal()
print(a.eat())

d = Dog()
print(d.eat(), d.bark())

c = Cat()
print(c.eat(), c.meow())
