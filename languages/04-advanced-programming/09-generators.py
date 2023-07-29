# generators are iterators

""" def gen():
    yield 1
    yield 2
    yield 3

itr = gen()

print(next(itr))

 """

def fib(n):
    pass

fib_numbers = [1,1]

for i in range(2, 10):
    fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])

print(fib_numbers)
