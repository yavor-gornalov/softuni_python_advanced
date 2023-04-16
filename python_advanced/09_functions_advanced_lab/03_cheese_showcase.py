# https://judge.softuni.org/Contests/Practice/Index/1838#2

def sorting_cheeses(**kwargs):
    result = ""
    cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, quantities in cheeses:
        result += cheese + "\n"
        result += "\n".join([str(q) for q in sorted(quantities, reverse=True)]) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
