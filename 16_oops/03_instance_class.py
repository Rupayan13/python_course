class Employee:
    company = "Accenture"

    def __init__(self, name, salary, bond, company):
        self.name = name
        self.salary = salary
        self.bond = bond
        self.company = company

    def get_salary(
        self,
    ):  # self is important here because it refers to the specific instance of the class
        return self.salary

    def get_info(self):
        print(
            f"The name of the employee is {self.name}. The salary is {self.salary} and the bond period is {self.bond} years."
        )


e = Employee("John Doe", 50000, 2, "Deloitte")
print(e.company)  # will always print instance attribute whenever present
print(Employee.company)  # will print class attribute

# Object introspection
print(dir(e))  # prints all attributes and methods of the object e
