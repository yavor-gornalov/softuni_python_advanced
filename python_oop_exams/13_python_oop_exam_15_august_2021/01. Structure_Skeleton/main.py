from project.bakery import Bakery

my_bakery = Bakery("My Bakery")

my_bakery.add_food("Bread", "Corn Bread", 2.30)
my_bakery.add_food("Bread", "Limetz Bread", 3.50)
my_bakery.add_food("Cake", "Space Cake", 5.00)
my_bakery.add_food("Cake", "SugarFree Cake", 4.20)
my_bakery.add_food("Cake", "Chocolate Cake", 6.80)

my_bakery.add_drink("Tea", "Herbal", 250, "Alpine")
my_bakery.add_drink("Water", "Fuzzy water", 500, "Devin")
my_bakery.add_drink("Water", "Mineral water", 500, "Devin")

my_bakery.add_table("InsideTable", 1, 4)
my_bakery.add_table("InsideTable", 50, 6)
my_bakery.add_table("OutsideTable", 51, 8)
my_bakery.add_table("OutsideTable", 100, 10)

print(my_bakery.reserve_table(2))
print("==============================================================")

print(my_bakery.order_food(1, "Corn Bread", "Meet Balls", "Space Cake"))
print("==============================================================")
print(my_bakery.order_drink(1, "Mineral water", "Fuzzy water"))
print("==============================================================")

print(my_bakery.get_free_tables_info())
print("==============================================================")

print(my_bakery.leave_table(1))
print("==============================================================")
print(my_bakery.get_total_income())
