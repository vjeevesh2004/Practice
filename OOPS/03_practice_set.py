''' create a class with a class attribute a: 
create an object from it and set a directly using 
object.a = a. Does this change the class attribute'''

class Sample: 
    a = "Harry"

obj = Sample()
obj.a = "Vicky"

Sample.a = "Vicky" # this will change the class attribute

print(Sample.a)
print(obj.a)

# no change


    
