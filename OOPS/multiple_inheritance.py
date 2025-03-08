class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "fiver"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upgradelevel()
print(p.level)
print(p.eCode)
print(p.company) # visa is printed coz employee is inherited first. 
