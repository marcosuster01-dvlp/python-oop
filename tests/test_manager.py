from models.manager import Manager
from models.employee import Employee

def test_manager_creation():
    man = Manager("Sarah", 90000, "Engineering", 5)
    assert man.name == "Sarah"
    assert man.salary == 90000
    assert man.department == "Engineering"
    assert man.team_size == 5

def test_add_report():
    man = Manager("Sarah", 90000, "Engineering", 5)
    emp = Employee("Marcos", 50000, "Engineering")
    man.add_report(emp)
    assert len(man.reports) == 1
    assert man.reports[0].name == "Marcos"

def test_get_info_shows_team_size():
    man = Manager("Sarah", 90000, "Engineering", 5)
    info = man.get_info()
    assert "Team size: 5" in info

def test_give_raise_inherited():
    man = Manager("Sarah", 90000, "Engineering", 5)
    man.give_raise(10000)
    assert man.salary == 100000