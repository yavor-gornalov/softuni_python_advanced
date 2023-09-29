def even_odd_filter(**kwargs):
    result = {}
    for key, nums in kwargs.items():
        if key not in result:
            result[key] = []
        if key == "even":
            result[key].extend([x for x in nums if x % 2 == 0])
        else:
            result[key].extend([x for x in nums if x % 2 != 0])

    return dict(sorted(result.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
