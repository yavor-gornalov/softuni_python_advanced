# https://judge.softuni.org/Contests/Practice/Index/1831#6

from collections import deque
from datetime import datetime, timedelta


def get_robots():
    robots = {}
    for robot_str in input().split(";"):
        robot_name, processing_time = robot_str.split("-")
        robots[robot_name] = [int(processing_time), 0]
    return robots


def get_details():
    details = deque()
    while True:
        detail = input()
        if detail == "End":
            return details
        details.append(detail)


def check_free_robots(robots):
    for robot, (processing_time, remaining_time) in robots.items():
        if remaining_time == 0:
            return robot
    return


def decrease_robots_remaining_time(robots):
    for robot in robots:
        robots[robot][1] = max(0, robots[robot][1] - 1)
    return robots


robots = get_robots()
current_time = datetime.strptime(input(), "%H:%M:%S")
details = get_details()

while details:
    current_time += timedelta(0, 1)
    robots = decrease_robots_remaining_time(robots)

    current_detail = details.popleft()

    current_robot = check_free_robots(robots)
    if not current_robot:
        details.append(current_detail)
    else:
        robots[current_robot][1] = robots[current_robot][0]
        print(f"{current_robot} - {current_detail} [{current_time.strftime('%H:%M:%S')}]")
