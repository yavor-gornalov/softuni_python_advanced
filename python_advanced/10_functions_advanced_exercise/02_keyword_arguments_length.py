# https://judge.softuni.org/Contests/Practice/Index/1839#1

def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
