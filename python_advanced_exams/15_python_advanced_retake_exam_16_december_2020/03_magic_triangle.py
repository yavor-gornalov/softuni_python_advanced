def get_magic_triangle(n):
    result = [[1], [1, 1]]
    if n <= 2:
        return result[:n]
    for row in range(2, n):
        result.append([1])
        for idx in range(1, len(result[row - 1])):
            result[row].append(result[row - 1][idx - 1] + result[row - 1][idx])
        result[row].append(1)

    return result


print(get_magic_triangle(5))
