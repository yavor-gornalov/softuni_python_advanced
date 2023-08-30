class store_results:
    _logfile = 'results.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        func_name = self.func.__name__
        func_res = self.func(*args)
        line_to_append = f"{func_name} was called. Result: {func_res}"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(line_to_append + '\n')


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
