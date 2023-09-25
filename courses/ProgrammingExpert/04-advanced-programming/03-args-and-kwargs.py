""" def sum_items(*args, **kwargs):
    print(args)
    print(kwargs)

sum_items(1,2,3,k=2,a=2)
sum_items(1,3,4,4,4,5)
sum_items(1)
sum_items()
 """

"""
def sum_items(a,b,c):
    return a+b+c

args = [4,5,7]
x = sum_items(*args)
print(x)
"""

def sum_items(a,b,c):
    return a+b+c

kwargs = {"a":4, "b":5, "c":7}
x = sum_items(**kwargs)
print(x)
