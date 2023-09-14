# https://judge.softuni.org/Contests/Practice/Index/3534#0

from collections import deque

seats = input().split(", ")

first_seq = deque([int(x) for x in input().split(", ")])
second_seq = deque([int(x) for x in input().split(", ")])

rotations = 0
taken_seats = []
while rotations < 10 and len(taken_seats) < 3:
    rotations += 1
    nums = [first_seq.popleft(), second_seq.pop()]
    letter = chr(sum(nums))

    match = False
    for num in nums:
        current_seat = str(num) + letter
        if current_seat in seats:
            if current_seat not in taken_seats:
                taken_seats.append(current_seat)
                match = True

    if not match:
        first_seq.append(nums[0])
        second_seq.appendleft(nums[1])

print(f"Seat matches: {', '.join(taken_seats)}\nRotations count: {rotations}")
