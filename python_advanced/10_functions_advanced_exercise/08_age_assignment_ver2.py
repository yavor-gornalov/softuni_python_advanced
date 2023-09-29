def age_assignment(*args, **kwargs):
    names_ages = {n: kwargs.get(n[0]) for n in args}
    # names_ages = dict.fromkeys(args, None)
    # for key, age in kwargs.items():
    #     for name in names_ages:
    #         if name.startswith(key):
    #             names_ages[name] = age
    return "\n".join(sorted(f"{n} is {a} years old." for (n, a) in names_ages.items()))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
