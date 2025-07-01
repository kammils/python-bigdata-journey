# Example using super()
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)  # Call parent constructor
        self.bonus = bonus

    def get_salary(self):
        return self.base_salary + self.bonus  # Override method

# Test
e1 = Employee("Nikhila", 50000)
m1 = Manager("Dharani", 60000, 15000)

print(f"{e1.name}'s Salary: ₹{e1.get_salary()}")
print(f"{m1.name}'s Salary: ₹{m1.get_salary()}")
