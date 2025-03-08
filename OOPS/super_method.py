class Person:
    country = "india"
    def __init__(self):
        print("Intialising Person...\n")

    def takeBreath(self):
        print("I am breathing..")

class Employee(Person):
    company = "Honda"
    
    def __init__(self):
        super().__init__()
        print("Intialising Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath() 
        print("I am an Employee so I am luckily Breathing")

class Programmer(Employee):
    company = "fiverr"

    def __init__(self):
       # super().__init__()
        print("Intialising Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath() 
        # this runs first its super class k take breath then its parent class take breath will run.
        print("I am a Programmer so I am breathing++..")

# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()

'''
I am breathing..  - Person o/p
here employe will run first parent class, then super class
I am breathing..
I am an Employee so I am luckily Breathing
here progeammer will run first parent class, then super class
I am breathing..
I am an Employee so I am luckily Breathing
I am a Programmer so I am breathing++..
'''