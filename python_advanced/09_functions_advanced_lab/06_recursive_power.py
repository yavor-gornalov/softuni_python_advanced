# https://judge.softuni.org/Contests/Practice/Index/1838#5

def recursive_power(num, pwr):
    if pwr == 0:
        return 1
    return num * recursive_power(num, pwr - 1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
