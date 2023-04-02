# https://judge.softuni.org/Contests/Practice/Index/1831#6
from collections import deque
from datetime import datetime, timedelta

# robots = robot_name: {processing_time, idle_time_left} for each robot in input line
robots = {robot.split('-')[0]: [int(robot.split('-')[1]), 0] for robot in input().split(";")}

start_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    start_time += timedelta(0, 1)
    current_product = products.popleft()
    robots = {robot[0]: [robot[1][0], max(0, robot[1][1] - 1)] for robot in robots.items()}
    # search for free robots
    free_robots = list(filter(lambda robot: robot[1][1] == 0, robots.items()))
    if free_robots:
        free_robots[0][1][1] = free_robots[0][1][0]
        print(f"{free_robots[0][0]} - {current_product} [{start_time.strftime('%H:%M:%S')}]")
    else:
        products.append(current_product)
