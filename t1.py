import pandas as pd
class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):

    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department ="F09" + department
        Manager.mgr_count += 1
## 7%3==1
    def display_employee(self):
        print(self.salary)

## 14/3=4 manageri
nume=pd.read_excel('salariati.xlsx', usecols=['Nume','Prenume'], nrows=4)
salariu=pd.read_excel('salariati.xlsx', usecols=['Salariu'], nrows=4)
manager0=Manager(nume.loc[0],salariu.loc[0],'dep')
manager1=Manager(nume.loc[1],salariu.loc[1],'dep')
manager2=Manager(nume.loc[2],salariu.loc[2],'dep')
manager3=Manager(nume.loc[3],salariu.loc[3],'dep')
manager0.display_employee()
manager1.display_employee()
manager2.display_employee()
manager3.display_employee()

employee=Employee(nume, salariu)
print(employee.empCount)
print(manager0.empCount)





