# https://judge.softuni.org/Contests/Practice/Index/3893#0

from collections import deque

ducky_dict = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

programmer_times = deque([int(x) for x in input().split()])
tasks_sequence = deque([int(x) for x in input().split()])

while programmer_times and tasks_sequence:
    task_time = programmer_times.popleft()
    number_of_tasks = tasks_sequence.pop()

    calculated_time = task_time * number_of_tasks
    if calculated_time <= 60:
        ducky_dict["Darth Vader Ducky"] += 1
    elif calculated_time <= 120:
        ducky_dict["Thor Ducky"] += 1
    elif calculated_time <= 180:
        ducky_dict["Big Blue Rubber Ducky"] += 1
    elif calculated_time <= 240:
        ducky_dict["Small Yellow Rubber Ducky"] += 1
    else:
        programmer_times.append(task_time)
        tasks_sequence.append(number_of_tasks - 2)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{key}: {value}") for key, value in ducky_dict.items()]
