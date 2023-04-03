# https://judge.softuni.org/Contests/Practice/Index/1832#3

COMMAND_IN, COMMAND_OUT = "IN", "OUT"

cars = set()
for _ in range(int(input())):
    command, plate_number = input().split(", ")
    if command == COMMAND_IN:
        cars.add(plate_number)
    elif command == COMMAND_OUT:
        cars.remove(plate_number)
if cars:
    [print(car) for car in cars]
else:
    print("Parking Lot is Empty")
