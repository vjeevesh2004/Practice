# static method
class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary fot this employee working in {self.salary} is {self.company}\n{signature}")
    
    @staticmethod
    def greet(): 
        print("Good Morning Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee()
harry.salary = 10000
harry.getSalary("Thanks") # = Employee.getSalary(harry)
harry.greet() # employee.greet()
harry.time()