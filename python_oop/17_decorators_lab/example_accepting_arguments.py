from time import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(end - start)
        return result

    return wrapper


@measure_time
def range_to_number(number):
    return [x for x in range(number)]


range_to_number(1_000_000)
