from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "John"))
print(space_station.add_astronaut("Biologist", "John"))
print(space_station.add_astronaut("Biologist", "Janet"))
print(space_station.add_astronaut("Geodesist", "George"))
print(space_station.add_astronaut("Geodesist", "Peter"))
print(space_station.add_astronaut("Meteorologist", "Maria"))
print(space_station.add_astronaut("Meteorologist", "Sarah"))
print(space_station.add_astronaut("Meteorologist", "Michael"))
print(space_station.retire_astronaut("Michael"))

print(space_station.add_planet("Mars", "stone, copper, iron, diamonds, sand, coal, steel"))
print(space_station.add_planet("Venera", "stone, copper, iron, diamonds, sand, coal, steel"))
print(space_station.add_planet("Neptun", "stone, copper, iron, diamonds, sand, coal, steel"))
print(space_station.add_planet("Saturn", "stone, copper, iron, diamonds, sand, coal, steel"))

print(space_station.send_on_mission("Mars"))
print(space_station.send_on_mission("Venera"))
print(space_station.retire_astronaut("John"))
print(space_station.retire_astronaut("Janet"))
print(space_station.send_on_mission("Neptun"))
space_station.recharge_oxygen()
space_station.recharge_oxygen()
print(space_station.send_on_mission("Saturn"))

print(space_station.report())

