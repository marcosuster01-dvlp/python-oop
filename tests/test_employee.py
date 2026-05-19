from models.employee import Employee

def test_employee_creation():
    emp = Employee("Marcos", 50000, "Engineering")
    assert emp.name == "Marcos"
    assert emp.salary == 50000
    assert emp.department == "Engineering"
    assert emp.is_active == True

def test_give_raise():
    emp = Employee("Marcos", 50000, "Engineering")
    emp.give_raise(5000)
    assert emp.salary == 55000

def test_deactivate():
    emp = Employee("Marcos", 50000, "Engineering")
    emp.deactivate()
    assert emp.is_active == False