from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

#
# green_plant = Plant()
# rock = Ornament()
# plastic_ship = Ornament()
#
# print(green_plant.__dict__, green_plant.decoration_type)
# print(rock.__dict__, rock.decoration_type)
#
# decoration_repository = DecorationRepository()
#
# decoration_repository.add(green_plant)
# decoration_repository.add(rock)
# print(decoration_repository.remove(plastic_ship))
# print(decoration_repository.remove(rock))
# found = decoration_repository.find_by_type("Plant")
# print(found.decoration_type)
# print(decoration_repository.find_by_type("Fish"))
#
# salt_fish = SaltwaterFish("Mini-shark", "Shark", 100)
# salt_fish2 = SaltwaterFish("Hummer-shark", "Shark", 100)
# fresh_fish = FreshwaterFish("Beta", "Beta-fish", 15)
# fresh_fish2 = FreshwaterFish("Queen", "Queen-fish", 15)
#
# print(salt_fish.__dict__)
# print(fresh_fish.__dict__)
# fresh_fish.eat()
# print(fresh_fish.__dict__)
#
# fresh_aquarium = FreshwaterAquarium("Fresh")
# print(fresh_aquarium.capacity)
# salt_aquarium = SaltwaterAquarium("Salt")
# print(salt_aquarium.capacity)
#
# fresh_aquarium.decorations = decoration_repository.decorations
# print(fresh_aquarium)
# print(fresh_aquarium.add_fish(salt_fish))
# print(fresh_aquarium.add_fish(fresh_fish))
# print(fresh_aquarium)

controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Fresh Aqua"))
print(controller.add_aquarium("SaltwaterAquarium", "Salt Aqua"))
print(controller.add_aquarium("WaterAquarium", "Aqua"))

print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Unknown"))
print(controller.add_decoration("Plant"))

print([x.decoration_type for x in controller.decorations_repository.decorations])

print(controller.insert_decoration("Fresh Aqua", "Plant"))
print(controller.insert_decoration("Fresh Aqua", "Ornament"))
print(controller.insert_decoration("Fresh Aqua", "Plant"))
print(controller.insert_decoration("Fresh Aqua", "Plant"))

print(controller.add_fish("Fresh Aqua", "SaltwaterFish", "Shark", "Shark", 100))
print(controller.add_fish("Fresh Aqua", "FreshwaterFish", "Beta", "Beta-Fish", 15))
print(controller.add_fish("Fresh Aqua", "FreshwaterFish", "Queen", "Queen-Fish", 10))
controller.aquariums[0].capacity = 2
print(controller.add_fish("Fresh Aqua", "FreshwaterFish", "Nemo", "Nemo-Fish", 10))

print([f.size for f in controller.aquariums[0].fish])
print(controller.feed_fish("Fresh Aqua"))
print([f.size for f in controller.aquariums[0].fish])

print(controller.calculate_value("Fresh Aqua"))

print(controller.report())
