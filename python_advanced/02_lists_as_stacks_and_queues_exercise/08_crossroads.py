# https://judge.softuni.org/Contests/Practice/Index/1831#7

from collections import deque

green_light_time = int(input())
free_window_time = int(input())

cars_waiting = deque()
cars_passed = 0
crash_happened = False
while True:
    command = input()
    if command == "END":
        break
    elif command == "green":

        current_pass_time = green_light_time
        current_free_time = free_window_time
        while cars_waiting:
            if current_pass_time > 0 and cars_waiting:
                car = cars_waiting.popleft()
                car_length = len(car)
                if car_length < current_pass_time:
                    current_pass_time -= car_length
                else:
                    car_length -= current_pass_time
                    current_pass_time = 0
                    current_free_time -= car_length
                    if current_free_time < 0:
                        print(f"A crash happened!\n{car} was hit at {car[current_free_time]}.")
                        crash_happened = True
                        break
            else:
                break
            cars_passed += 1
    else:
        cars_waiting.append(command)

    if crash_happened:
        break

if not crash_happened:
    print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")
