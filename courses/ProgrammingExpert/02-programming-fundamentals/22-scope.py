

# local scope of x
""" def foo():
    x = 0
foo()
print(x) """


# global scope of x
""" x = 1

def foo():
    print(x+1)

foo()
print(x)
 """

#block scope
""" inp = int(input("Enter a number: "))
if inp > 5:
    value = "greater than 5"
else:
    value = "less than 5"

print(value) """

def add_5(x):
    x += 5
    return x

x = 10
print(x)
add_5(x)
print(x)

