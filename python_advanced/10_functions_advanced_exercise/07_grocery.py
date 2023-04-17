# https://judge.softuni.org/Contests/Practice/Index/1839#6

def grocery_store(**kwargs):
    result = []
    receipt = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for name, quantity in receipt:
        result.append(f"{name}: {quantity}")
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))