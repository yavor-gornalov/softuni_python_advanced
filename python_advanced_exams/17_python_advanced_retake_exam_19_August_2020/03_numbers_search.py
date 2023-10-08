def numbers_searching(*args):
    numbers = sorted(args)
    unique_numbers = set(numbers)
    min_number, max_number = numbers[0], numbers[-1]
    missing_numbers = set(range(min_number, max_number)) - unique_numbers
    return [max(missing_numbers), sorted(set(x for x in numbers if numbers.count(x) > 1))]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
