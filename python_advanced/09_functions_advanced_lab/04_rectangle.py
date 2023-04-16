# https://judge.softuni.org/Contests/Practice/Index/1838#3


def rectangle(*args):
    for arg in args:
        if not isinstance(arg, int):
            return "Enter valid values!"
    a, b = args

    def rect_area():
        return a * b

    def rect_perim():
        return 2 * (a + b)

    return f"Rectangle area: {rect_area()}\n" \
           f"Rectangle perimeter: {rect_perim()}"


print(rectangle(2, 10))
print(rectangle('2', 10))

