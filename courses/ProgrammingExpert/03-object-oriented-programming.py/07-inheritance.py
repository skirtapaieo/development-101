# polynorhism

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def __repr__(self):
        return self.name

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"


d = Dog("Fido")
print(d.speak())

