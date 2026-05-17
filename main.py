from models.employee import Employee
from models.manager import Manager

manager = Manager("Sarah", 90000, "Engineering", 5)
emp1 = Employee("Marcos", 50000, "Engineering")
emp2 = Employee("Juan", 75000, "Engineering")

print(manager.get_info())
print(manager.add_report(emp1))
print(manager.add_report(emp2))
print(f"{manager.name} manages: {[e.name for e in manager.reports]}")
print(manager.give_raise(10000))