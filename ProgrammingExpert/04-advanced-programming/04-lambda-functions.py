

""" func = lambda x,y,z=0: x+y+z # lambda function with 3 parameters, assigned to variable func
print(func(1,2)) # 3
print(func(1,2,3)) # 6
 """

"""
def sort_func(x):
    return x[1]

lst = [(4,8,6), (1,4,3), (7,12,9)]
lst.sort(key=sort_func)
print(lst)
"""

""" lst = [(4,8,6), (1,4,3), (7,12,9)]
lst.sort(key=lambda x: x[1])
print(lst)
 """

mul = lambda x: lambda y: x * y

result = mul(2)

print(result(4))
