from employee import Employee
import io
import contextlib
import pandas as pd

class Manager(Employee):
    """Class for managers"""

    mgr_count = 0 ##It counts the number of objects created

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department="F09"+department
        Manager.mgr_count += 1

    def display_employee(self):  ##X%3 is 4%3==1 so this method displays only the salary
        """Display the salary as Salary: [salary]"""
        print("Salary: ", self.salary)

##Y/3 is 5/3==1 => 1 object created
    
nume = pd.read_excel('salariati.xlsx', usecols=['Nume'], nrows=1)+' '+pd.read_excel('salariati.xlsx', usecols=['Prenume'], nrows=1)
salary = pd.read_excel('salariati.xlsx', nrows=1, usecols=['Salariu'])

employee = Manager(nume, salary, 'IT')

employee.display_employee()

print('Manager count: ', Manager.mgr_count)
print('Employee count: ', Employee.empCount)




