# classs Attirbutes
class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
harry.salary = 300  #instance variable
rajni.salary = 400  #instance variable 

print(harry.company)
print(rajni.company)
Employee.company = "Youtube" # attribute changes
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)
#instance attributes
