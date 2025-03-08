class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    # company = "Youtube"
    def getName(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("This is a programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails() # this will give updated value
print(p.company)