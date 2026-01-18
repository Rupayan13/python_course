# Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

# Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.


class Employee:
    company = "Accenture"

    def get_salary(
        self,
    ):  # self is important here because it refers to the specific instance of the class
        return 34000


e1 = Employee()  # An object of class Employee is created here
print(e1.get_salary())  # Calling the method get_salary on the object e1

e2 = Employee()  # Another object of class Employee is created here
print(e2.get_salary())  # Calling the method get_salary on the object e2
print(e2.company)  # Accessing the class variable 'company' through object e2
