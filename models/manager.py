from models.employee import Employee

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
