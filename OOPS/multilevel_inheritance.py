class Person:
    country = "india"

    def takeBreath(self):
        print("I am breathing..")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee so I am luckily Breathing")

class Programmer(Employee):
    company = "fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

p = Person()
p.takeBreath()
# print(p.company) # throws an error coz no company exist

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)