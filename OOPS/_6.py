# self parameter
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary fot this employee working in {self.salary} is {self.company}")

harry = Employee()
harry.salary = 10000
harry.getSalary() # = Employee.getSalary(harry)
'''
self is a parmater which gets pass automatically 
whenever u call any object it gets pass.
here we can use instance attributes and class 
attributes this object
'''