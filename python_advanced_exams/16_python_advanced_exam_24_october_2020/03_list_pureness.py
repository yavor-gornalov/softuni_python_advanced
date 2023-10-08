from collections import deque


def best_list_pureness(numbers, rotations):
    queue = deque(numbers)
    count_rotations = 0
    best_result = sum([x * i for x, i in enumerate(queue)])
    for i in range(1, rotations + 1):
        queue.rotate()
        current_result = sum([x * i for x, i in enumerate(queue)])
        if current_result > best_result:
            best_result = current_result
            count_rotations = i
    return f"Best pureness {best_result} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
