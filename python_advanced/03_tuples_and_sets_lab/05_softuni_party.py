# https://judge.softuni.org/Contests/Practice/Index/1832#4

n = int(input())
guests = {input() for _ in range(n)}

while True:
    command = input()
    if command == "END":
        break
    guests.remove(command)

print(len(guests))
for guest in sorted(guests):
    print(guest)
