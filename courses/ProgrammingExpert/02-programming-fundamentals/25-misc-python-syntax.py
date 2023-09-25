

# list
lst = [i for i in range(1,11) if i%2==0]
print(lst)

#dictionary
s = {i: i**2 for i in range(1,11) if i%2==0}
print(s)

#multiple assignment
x = y = 1
print(x,y)

a, b = 1, 2
print(a,b)

#docstring

def foo():
    """
    This is a docstring
    this is the foo function
    """
    pass

help(foo)

