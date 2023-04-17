# https://judge.softuni.org/Contests/Practice/Index/1839#7

def age_assignment(*args, **kwargs):
    names_ages = {name: kwargs.get(name[0]) for name in args}
    result = [f"{name} is {names_ages[name]} years old." for name in sorted(names_ages)]
    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
