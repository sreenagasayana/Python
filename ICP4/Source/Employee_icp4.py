class Employee:
    empcnt = 0
    salsum = 0
    def __init__(self,ename,sal,dpt,family):
        self.ename = ename
        self.sal = sal
        self.dpt = dpt
        self.family = family
        Employee.empcnt += 1
        Employee.salsum+= sal
    def display(self):
        print("Name:", self.ename, "Salary:", self.sal, "Department:", self.dpt, "Family:", self.family)

class EmployeeFullTime(Employee): # define child class
   def __init__(self,ename,sal,dpt,family):
       self.ename = ename
       self.sal = sal
       self.dpt = dpt
       self.family = family


EF1  = EmployeeFullTime("Sree Naga", 2000, "CS", "Harish Jayanti")
EF1.display()
emp1 = Employee("Sree", 1000, "CS", "Harish Jayanti")
emp2 = Employee("Hari", 1500, "CS", "Mom")
emp3 = Employee("Ram", 2000, "EE", "Dad")
emp4 = Employee("Jack", 4000, "EE", "Dad")
emp1.display()
emp2.display()
emp3.display()
emp4.display()
print("Total employees", Employee.empcnt)
print(Employee.salsum/Employee.empcnt)
