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