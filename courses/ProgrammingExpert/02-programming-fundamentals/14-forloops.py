
""" 
for i in range(20):
    print(i+1)
 """    

""" for i in range (0, 20, 5):
    print(i+1)
 """

""" for i in range(10, -5, -5):
    print(i)
 """

""" lst = [1,2,3,4,5,True]

for i in lst:
    print(i)    
 """
""" 
lst = [1,2,3,4,5,True]

for i, element in enumerate(lst):
    print(i, element)
     """
""" 
tup = (2,3,4,"Hello", True)

for in range (len(tup)):
    print(tup[i]
     """      

""" 
lst = [1,2,3,4,5,True]

for num in lst: 
    if num == 3:
        continue
    print(num)
print("Done")
 """

""" 
for i in range(10):
    for j in range(10):
        for w in range(10):
            print(w)    
        print("Done with innermost loop")
    print("Done with inner loop")
print("Done with outer loop")
 """

# lst = [1,2,3,4,5,True]

# by index
""" for i in range(len(lst)):
    print(lst[i])
    if lst[i] == 3:
        break
 """

""" # by item 
for element in lst: 
 print(element)
 """

""" # enumerate keyword - by id and item 
for i, element in enumerate(lst):
    print(i, element)
 """

""" tup = (2,3,4,"Hello", True)

for i in range(len(tup)):
    print(tup[i])
 """

""" s = "my string"

for i in range(len(s)):
    print(s[i])
 """          

""" lst = [1,2,3,4,5,True]

for num in lst: 
    if num == 4: 
        continue
    print(num)

 """

""" for i in range(10):
    for j in range(10):
        for w in range(10):
            print(w)
        print("Done with innermost loop")
    print("Done with inner loop")
 """

""" str = "hello worlds"

for i, chr in enumerate(str):
    if chr == "w":
        print(i)
 """        

""" numbers = []

for i in range(3): 
    num = input("Enter a number: ")
    numbers.append(int(num))

print(numbers)
 """

words = ("hello", "world", "python", "programming")
target = "python"

for word in words:
    if word == target:
        print("Found!")
        break
else: 
    print("Not found!")

