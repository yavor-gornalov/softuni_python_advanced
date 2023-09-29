def concatenate(*args, **kwargs):
    text = "".join(args)
    for old, new in kwargs.items():
        text = text.replace(old, new)
    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
