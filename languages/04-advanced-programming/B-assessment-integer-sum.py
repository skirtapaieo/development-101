from functools import wraps

def flatten_lists(func):
    @wraps(func)
    def inner(*args):
        flat_args = []
        for arg in args:
            if isinstance(arg, list):
                flat_args.extend(arg)
            else:
                flat_args.append(arg)
        return func(*flat_args)
    return inner

def convert_strings_to_ints(func):
    @wraps(func)
    def inner(*args):
        converted_args = []
        for arg in args:
            if isinstance(arg, str) and arg.isdigit():
                converted_args.append(int(arg))
            elif not isinstance(arg, str):
                converted_args.append(arg)
        return func(*converted_args)
    return inner

def filter_integers(func):
    @wraps(func)
    def inner(*args):
        int_args = [arg for arg in args if isinstance(arg, int)]
        return func(*int_args)
    return inner

@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)

# Testing the function
print(integer_sum("1", "2", -0.9, 4, [5, "hi", "3"]))
