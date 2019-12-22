class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.salary = salary
        self.last = last
    @classmethod
    def emp_str(cls, empl_str):
        first, last, salary=empl_str.split("-")
        return cls(first,last, salary)
print(Employee.emp_str("suhas-gaikwad-12000").__dict__)

'''1. THESE ARE USED AS ALTERNATE CONSTRUCTORS'''



