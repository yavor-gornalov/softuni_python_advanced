def naughty_or_nice_list(kids, *args, **kwargs):
    kids_by_type = {}
    for arg in args:
        number, key = int(arg.split("-")[0]), arg.split("-")[1]
        collection = [k for k in kids if k[0] == number]
        if len(collection) != 1:
            continue
        kid = collection[0]
        kids.remove(kid)
        if key not in kids_by_type:
            kids_by_type[key] = []
        kids_by_type[key].append(kid[1])

    for name, key in kwargs.items():
        collection = [k for k in kids if k[1] == name]
        if len(collection) != 1:
            continue
        kid = collection[0]
        kids.remove(kid)
        if key not in kids_by_type:
            kids_by_type[key] = []
        kids_by_type[key].append(name)

    if kids:
        kids_by_type["Not found"] = [k[1] for k in kids]

    result = []
    for key in ["Nice", "Naughty", "Not found"]:
        result.append(f"{key}: {', '.join([kid for kid in kids_by_type[key]])}") if key in kids_by_type else None

    return "\n".join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
