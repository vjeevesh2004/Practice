''' procedural programming
a = 12
b = 34
print("the sum of a and b is", a+b)
''' 
# object oriented programming

class Number:
    def sum(self):
        return self.a + self.b

num = Number() #Object instantiation
num.a = 12
num.b = 34
s = num.sum()
print(s)