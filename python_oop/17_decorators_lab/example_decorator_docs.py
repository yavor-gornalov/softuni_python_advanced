from functools import wraps


def uppercase_decorator(function):
    @wraps(function)
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


# def say_hi():
#     return 'hello there'
#
#
# decorate = uppercase_decorator(say_hi)
# print(decorate())

@uppercase_decorator
def say_hi():
    """
    Saying Hi Documentation is lost
    without using '@wraps(function)'
    """
    return 'hello there'


print(say_hi())
print(say_hi.__name__)
print(say_hi.__doc__)
