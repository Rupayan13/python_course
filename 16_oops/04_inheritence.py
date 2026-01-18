class Animal:  # Parent class (superclass)
    location = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Spaking now...")


class Dog(Animal):  # Child class (subclass) inheriting from Animal
    def speak(self):  # Overriding the speak method
        super().speak()  # using super method in the parent class
        print("Woof! Woof!")


d = Dog("Bruno")
d.speak()
print(d.location)
