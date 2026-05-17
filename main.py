class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        self.is_active = True
    
    def get_info(self):
        return f"{self.name} | {self.department} | ${self.salary}"
    
    def give_raise(self, amount):
        self.salary += amount
        return f"New Salary: ${self.salary}"
    
    def deactivate(self):
        self.is_active = False
        return f"{self.name} has been deactivated"
    

emp1 = Employee("Marcos", 50000, "Engineering")
emp2 = Employee("Sarah", 75000, "Management")

print(emp1.get_info())
print(emp2.get_info())
print(emp1.give_raise(5000))
print(emp1.get_info())
print(emp2.deactivate())