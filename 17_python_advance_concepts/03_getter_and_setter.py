class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        l = self.name.split(" ")
        return l[0]

    """
    def set_first_name(self, first_name):
        l = self.name.split(" ")
        self.name = f"{first_name} {l[1]}"
    """

    @first_name.setter
    def first_name(self, first_name):
        l = self.name.split(" ")
        self.name = f"{first_name} {l[1]}"


emp = Employee("Rupayan Dirghangi", 50000)

# Before using getter and setter
# print(emp.first_name())
# emp.set_first_name("John")
# print(emp.name)

# After usinge getter and setter
print(emp.first_name)
emp.first_name = "John"
print(emp.name)
