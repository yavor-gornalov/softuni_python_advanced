# https://judge.softuni.org/Contests/Practice/Index/1839#4

def concatenate(*args, **kwargs):
    result = "".join(args)
    for key, el in kwargs.items():
        result = result.replace(key, el)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
