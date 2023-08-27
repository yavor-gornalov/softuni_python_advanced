from math import sqrt


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(numbers):
    idx = 0
    while idx < len(numbers):
        current_number = numbers[idx]
        if is_prime(current_number):
            yield current_number
        idx += 1


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
