# https://judge.softuni.org/Contests/Practice/Index/3515#2

def shopping_cart(*args):
    meals = {
        "Soup": {"count": 3, "products": []},
        "Pizza": {"count": 4, "products": []},
        "Dessert": {"count": 2, "products": []},
    }
    for arg in args:
        if arg == "Stop":
            break

        meal, product = arg
        if meal not in meals:
            continue
        if meals[meal]["count"] <= len(meals[meal]["products"]):
            continue
        if product in meals[meal]["products"]:
            continue

        meals[meal]["products"].append(product)

    if all(x["products"] == [] for x in meals.values()):
        return "No products in the cart!"

    result = ""
    for meal, data in sorted(meals.items(), key=lambda x: (-len(x[1]["products"]), x[0])):
        result += f"{meal}:\n"
        for product in sorted(data["products"]):
            result += f" - {product}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
