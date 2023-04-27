def create_fibonacci(size):
    sequence = [0, 1]
    if size < 3:
        return sequence[0:size]

    for index in range(2, size):
        number_to_append = sum(sequence[index - 2:index])
        sequence.append(number_to_append)
    return sequence


def get_fibonacci_index(searched):
    result = None
    sequence = [0, 1]
    if 0 <= searched < 2:
        result = sequence.index(searched)
    else:
        index = 2
        while True:
            number_to_append = sum(sequence[index - 2:index])
            if number_to_append == searched:
                result = index
            elif number_to_append > searched:
                break
            sequence.append(number_to_append)
            index += 1
    return result
