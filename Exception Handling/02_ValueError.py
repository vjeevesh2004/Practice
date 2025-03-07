''' 
Write a Python program that prompts
the user to input an integer and 
raises a ValueError exception if the 
input is not a valid integer.
'''

try:
    a = int(input("enter a number"))
    print(a)
except ValueError as e:
    print("the given input is not an integer",e)