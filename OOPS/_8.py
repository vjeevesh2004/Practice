# Constructors
class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit): # constructor
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!  ")

    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the name of the employee is {self.salary}")
        print(f"the name of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary fot this employee working in {self.salary} is {self.company}\n{signature}")
    
    @staticmethod
    def greet(): 
        print("Good Morning Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")
    
harry = Employee("Harry", 100, "Youtube")
# harry = Employee() this throws an error 
harry.getDetails()


