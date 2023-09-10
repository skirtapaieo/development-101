

# built-in sorting

""" lst = sorted([5, 2, 3, 1, 4]) # [1, 2, 3, 4, 5]
print(lst)
 """

""" lst = sorted([5, 2, 3, 1, 4], reverse=True) # [5, 4, 3, 2, 1]
print(sorted(lst, reverse=True))
print(lst)
 """

""" lst = (1, 2, 3, 4, 5)
sorted(lst)
print(lst)
 """

def sort_second_index(item):
    return item[1]

lst = [[1, 2], [3, 4], [4, 3], [2, 1]]
lst.sort(reverse=True, key=sort_second_index)
print(lst)
