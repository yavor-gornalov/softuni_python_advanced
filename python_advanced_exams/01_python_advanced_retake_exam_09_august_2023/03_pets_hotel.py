# https://judge.softuni.org/Contests/Practice/Index/4089#2


def accommodate_new_pets(available_capacity: int, weight_limit: float, *args: [str, float]):
    result = []
    pets = {}
    for pet_type, pet_weight in args:
        if not available_capacity:
            result.append("You did not manage to accommodate all pets!")
            break
        if pet_weight > weight_limit:
            continue
        if pet_type not in pets:
            pets[pet_type] = 0
        pets[pet_type] += 1
        available_capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")
    result.append("Accommodated pets:")
    [result.append(f"{pet_type}: {number}") for pet_type, number in sorted(pets.items(), key=lambda x: x[0])]
    return "\n".join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
