# https://judge.softuni.org/Contests/Practice/Index/3889#2


def shop_from_grocery_list(budget, *args):
    shopping_list, *products = args
    for product, price in products:
        if product not in shopping_list:
            continue
        if price > budget:
            continue
        shopping_list.pop(shopping_list.index(product))
        budget -= price
        if not budget:
            break

    if not shopping_list:
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result = f"You did not buy all the products. Missing products: {', '.join(shopping_list)}."

    return result


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))
#
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
