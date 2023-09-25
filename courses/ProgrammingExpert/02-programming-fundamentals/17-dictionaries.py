"""
 x = {1: "hello", 2: "world", 3: "python", 4: "programming", 5: 5}

print(x[1]) 

x = dict()

x[1] = "hello"

print(x)

contains = 1 in x 

print(contains)

values = x.values() 
print(values) 

keys = x.keys()
print(keys) 

items = x.items()
print(items)

del x[1]

print(x) """

# x = {2:1, 3:3, 4:5, 5:7, 6:9}

""" #example 
for key in x: 
    value = x[key]
    print(key, value)

# better
for key, value in x.items():
    print(key, value)
 """
""" 
x[12] = x.get(12,0) + 1

print(x)
 """

""" characters = {}
string = {"hello world"}

for char in string: 
    characters[char] = characters.get(char, 0) + 1

print(characters)
 """

""" counts = {}

while True: 
    num = input("Enter number: ")

    if num == "q":
        break
    num = int(num) 
    counts[num] = counts.get(num, 0) + 1

print(counts)
 """

d = {1: "hello", 2: "world", 3: "python", 4: "programming", 5: 5}
l = {1: "hello", 2: "world", 4: "programming", 6: 6, 5: 5}

"d" in d

"d" in l
