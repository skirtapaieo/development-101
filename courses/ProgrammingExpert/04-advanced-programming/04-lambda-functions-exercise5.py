
# A lambda function that takes three integer or float parameters and returns their sum
add_values = lambda x, y, z: x + y + z

# A lambda function that takes two string parameters and returns the maximum of their lengths
max_length = lambda str1, str2: max(len(str1), len(str2))

# A lambda function that takes two list parameters and returns a set containing the elements from both lists
create_set = lambda list1, list2: set(list1 + list2)

print(add_values(3, 4, 5))   # output: 12
print(max_length("hello", "tim"))  # output: 5
print(create_set([1, 2, 3, 4], [2, 3, 5]))  # output: {1, 2, 3, 4, 5}
