import os
from tema1 import Manager

def test0():
    employee1 = Manager("Mariuca", 865, "Beauty")
    employee = Manager("Ioana", 65, "Nuj")
    assert [employee1.salary, employee.salary] == [865, 65]

def test1():
    test1employee = Manager("Ionut", 3456, "IT")
    assert test1employee.salary == 3456
    
def test2():
    employee1 = Manager("Ionut", 3456, "IT")
    employee2 = Manager("Ramona", 3456, "Chef")
    employee3 = Manager("Andreea", 3456, "Software")
    employee4 = Manager("Sorina", 3456, "Marketing")
    employee5 = Manager("Ioana", 3456, "Vase")
    assert Manager.mgr_count==9 ##se ia in calcul si testul din fata
    
def test3():
    department="IT"
    test3employee = Manager("Ionut", 3456, department)
    assert test3employee.department=="F09IT"
    