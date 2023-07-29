""" file = open("04-advanced-programming/file.txt", "r")
print(file.read())
file.close()
 """

""" with open("04-advanced-programming/file.txt", "r") as file:
    line1 = file.readlines()[0] #index first line
    print([line1.strip()]) #strip() removes the whitespace at the beginning and end of the line
 """

"""
    with open("04-advanced-programming/file2.txt", "w") as file:
    file.write("Hello World")
 """

"""
    with open("04-advanced-programming/file2.txt", "r+") as file:
    file.write("\nHello World")
"""

"""
    with open("04-advanced-programming/file3.txt", "r+") as file:
    score = file.read()
    new_score = int(score) + 1
    file.seek(0) #move the cursor to the beginning of the file, 1 = current position, 2 = end of file
    file.write(str(new_score))
 """

#iterate over a file ...

"""
with open("04-advanced-programming/file2.txt", "r+") as file:
    count = 0
    for line in file:
        print(line, end="")
        count += 1
        if count >= 3:
            break

#enumerate instead ...
     for i, line in enumerate(file)
        if i == 2:
            break
"""

