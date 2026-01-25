class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        print(f"Name of the employee is {self.name} and salary is {self.salary}.")

    # Static Method
    @staticmethod
    def add(a, b):
        return a + b

    # Class Methods
    @classmethod
    def print_company(cls):
        print(f"The company name is {cls.company}.")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Rupayan Dirghangi", 50000)
e2 = Employee("John Doe", 60000)
# print(Employee.company)
# print(Employee.name)  # It will give error because name is instance variable

print(e2.add(5, 10))

Employee.print_company()
e2.change_company("Microsoft")  # Class methods can be called by instance also
Employee.print_company()
