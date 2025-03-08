# classs Attirbutes
class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# creating instance attributes for both the objects(harry & rajni)
#harry.salary = 300 
#rajni.salary = 400  

harry.salary = 45 
print(harry.salary)
print(rajni.salary)
''' below line will throws an error as address is not
present in the instance/class
print(rajni.address)
''' 

