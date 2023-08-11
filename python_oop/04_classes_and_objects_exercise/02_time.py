# https://judge.softuni.org/Contests/Practice/Index/1937#1

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = 23
        self.minutes = 59
        self.seconds = 59




time = Time(9, 30, 59)
print(time.next_second())
