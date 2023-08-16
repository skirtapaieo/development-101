
""" def print_value(value):
    print(value) """

""" def print_value(value):
    print(value)

print_value("hello")
print_value(5)
 """
""" 
def add_5(x,y,z):
    result = x + y + z +5 
    print(result)

 """
""" 
def add_5(x,y,z):
    result = x + y + z + 5 
    return result

r = add_5(1,2,3)    
print(r)
 """

""" def new_range(start=0, stop=10): 
    x = start

    while x < stop: 
        print(x) 
        x += 1

new_range(start=-4, stop=5)
 """

""" def return_values(x,y,z):
    return x,y,z

result = return_values(2,3,4)
print(result)
 """

""" def remove_chars(base, chars):
    result = base.replace(chars, "")
    return result

result = remove_chars("hello harald", "h")
print(result) """


def sum_lists(list1, list2):
    list1_sum = sum_list(list1) 
    list2_sum = sum_list(list2)
    return list1_sum, list2_sum

def sum_list(lst): 
    total = 0
    for num in lst: 
        total += num

    return total

sum1, sum2 = sum_lists([1,2,3], [4,5,6])
print(sum1, sum2)



