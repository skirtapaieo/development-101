
# methods are functions that are associated with a particular object
"""
class Person:
    def __init__(self, name, age): #initialization method
        self.name = name
        self.age = None

    def say_hello(self):
        print("Hello my name is " + self.name)

    def set_age(self,age):
        self.age = age

    def get_age(self):
        return self.age


p1 = Person("John",36)
p2 = Person("Jane", 25)

p1.say_hello()

p1.set_age(40)
print(p1.get_age())

p2.say_hello()


p1.set_age(42)
print(p1.get_age())
 """

""" class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def tooggle_lock(self):
        self.locked = not self.locked

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

    def get(self):
        return self.count

    def print_count(self):
        print(f"The current count i {self.count}")

counter = Counter()
counter.increment()
counter.print_count()
counter.decrement()
counter.print_count()
counter.increment()
counter.print_count()

 """

"""
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def change_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def get_area(self):
        return self.width * self.height


class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

# The above code is copyrighted by Algoexpert - the below code is improved and is not:
"""

class Rectangle:
    # A class to represent a rectangle."""

    def __init__(self, x, y, width, height):
        """Initialize rectangle with x, y, width, height."""
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def change_position(self, x, y):
        """Change the position of the rectangle."""
        self.x = x
        self.y = y

    def get_position(self):
        """Return the position of the rectangle."""
        return self.x, self.y

    def get_area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height


class Group:
    """A class to represent a group of names."""

    def __init__(self, name, members=None):
        """Initialize group with name and members."""
        if members is None:
            members = []
        self.name = name
        self.members = members

    def add(self, name):
        """Add a name to the group."""
        self.members.append(name)

    def delete(self, name):
        """Remove a name from the group."""
        if name in self.members:
            self.members.remove(name)
        else:
            raise ValueError("Member not in group.")

    def get_members(self):
        """Return a sorted list of group members."""
        return sorted(self.members)

