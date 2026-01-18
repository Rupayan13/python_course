class Employee:
    def __init__(self, name, salary, bond):
        self.name = name
        self.salary = salary
        self.bond = bond

    def get_salary(
        self,
    ):  # self is important here because it refers to the specific instance of the class
        return self.salary

    def get_info(self):
        print(
            f"The name of the employee is {self.name}. The salary is {self.salary} and the bond period is {self.bond} years."
        )


e = Employee(
    "John Doe", 50000, 2
)  # Creating an object of class Employee with specific attributes

e.get_info()  # Calling the method get_info on the object e
