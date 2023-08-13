from project.vehicle import Vehicle
from project.car import Car
from project.sports_car import SportsCar

v = Vehicle()
print(v.move())

c = Car()
print(c.move(), c.drive())

s_c = SportsCar()
print(s_c.move(), s_c.drive(), s_c.race())
