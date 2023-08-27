def fibonacci():
    n1, n2 = 0, 1
    while True:
        n1, n2 = n2, n1 + n2
        yield n1


def fibonacci_old():
    fibonacci_seq = [0, 1]
    idx = 2
    while True:
        fibonacci_seq.extend([fibonacci_seq[idx - 1] + fibonacci_seq[idx - 2]])
        yield fibonacci_seq[idx - 2]
        idx += 1


generator = fibonacci()
for i in range(5):
    print(next(generator))
