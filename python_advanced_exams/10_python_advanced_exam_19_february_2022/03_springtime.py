def start_spring(**kwargs):
    spring_objects = {}
    for obj, typ in kwargs.items():
        if typ not in spring_objects:
            spring_objects[typ] = []
        spring_objects[typ].append(obj)

    result = []
    for typ, obj in sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{typ}:")
        [result.append(f"-{o}") for o in sorted(obj)]

    return "\n".join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }

print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
