''' create a class Programmer for storing information of few
programmers working at Microsoft'''

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getinfo(self):
        print(f"THe name of the company {self.company} programmer is {self.name} and the product is {self.product}")
        
harry = Programmer("Harry", "Skype")
Alka = Programmer("Alka", "Github")
harry.getinfo()
Alka.getinfo()