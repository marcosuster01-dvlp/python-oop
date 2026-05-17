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
    
class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size
        self.reports = []
    
    def add_report(self, employee):
        self.reports.append(employee)
        return f"{employee.name} now reports to {self.name}"
    
    def get_info(self):
        base = super().get_info()
        return f"{base} | Team size: {self.team_size}"

manager = Manager("Sarah", 90000, "Engineering", 5)
emp1 = Employee("Marcos", 50000, "Engineering")
emp2 = Employee("Juan", 75000, "Engineering")

print(manager.get_info())
print(manager.add_report(emp1))
print(manager.add_report(emp2))
print(f"{manager.name} manages: {[e.name for e in manager.reports]}")
print(manager.give_raise(10000))