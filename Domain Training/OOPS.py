'''
the program demonstrates creating a classs, defining attributes and methods, and using objects. 
object is an example of class. That shares common behaviours and habbits. 
self keyword is used to represent instance of the class
it should be declared explictly 
it should be the first parameter while declaring
instance methods are only excessed with parameter
'''

class car:
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car: {self.brand} {self.model} {(self.year)}")

car1 = car("Toyota", "Corocila", 2020)
car2 = car("Honda", "Civic", 2022)

car1.display_details()
car2.display_details()

'''
what happen if u dont use self keyword 
then error will be encountered, the object don't know what to do 
class person:
'''

'''
inheritance
we use : in c++ to implment inheritance
'''
class animal: #derived class
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("This animal makes a sound.")
    

class Dog(animal):
    def sound(self):
        print(f"(self.name) says: Meow")





    
    
