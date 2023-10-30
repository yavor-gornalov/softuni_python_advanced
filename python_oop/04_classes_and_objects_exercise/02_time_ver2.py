from datetime import datetime, timedelta


class Time:
    max_hours: int = 23
    max_minutes: int = 59
    max_seconds: int = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        if hours <= self.max_hours and minutes < self.max_minutes and seconds < self.max_seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def next_second(self):
        current_time = datetime(2023, 1, 1, self.hours, self.minutes, self.seconds)
        next_time = current_time + timedelta(seconds=1)
        self.hours = next_time.hour
        self.minutes = next_time.minute
        self.seconds = next_time.second
        return self.get_time()

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
