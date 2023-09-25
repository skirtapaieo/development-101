""" lst = [1,2,3,4,5,6,7,8,9,10]
new_lst = map(lambda x: x**2, lst)
print(list(new_lst))
 """

import math

lst = [1,2,3,4,5,6,7,8,9,10]


""" new_lst = map(lambda x: round(math.sqrt(x), 2), lst)
print(list(new_lst))
 """

""" new_lst = list(filter(lambda x: True, lst))
print(list(new_lst))
 """

new_lst = filter(lambda y: y % 2 == 0, map(lambda x: x, lst))
print(list(new_lst))
