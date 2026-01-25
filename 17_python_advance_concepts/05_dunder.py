class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The employee name is {self.name} and salary is {self.salary}."

    def __repr__(self):
        return f"Name: {self.name}\nSalary: {self.salary}"

    def __len__(self):
        return len(self.name)


e1 = Employee("Rupayan Dirghangi", 50000)

print(str(e1))
print(repr(e1))
print(len(e1))
