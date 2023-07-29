""" def decorator(func): # decorator function
    def wrapper(*args, **kwargs):
        print('Before function call')
        result = func(*args, **kwargs)
        print('After function call')
        return result
    return wrapper

def foo():
    print("foo")

foo = decorator(foo)
foo()

 """

def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("time taken to execute:", end - start)
        return result
    return wrapper

@timer
def loop():
    for _ in range(1000000):
        pass

loop()


