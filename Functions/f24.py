''' Write a Python program to access a function inside a function.
'''

def access_function_under_function():
    def inner_function():
        return "Hellow"
    result  = inner_function()
    return result

print(access_function_under_function()) 

def maths(a,b):
    def add():
        return a + b
    def multiply():
        return a * b
    return add(), multiply()

result = list(maths(2,3))
print(result)