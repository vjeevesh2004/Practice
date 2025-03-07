''' 
Write a Python program that 
executes division and handles an
 ArithmeticError exception if
   there is an arithmetic error.
'''
a = int(input("enter a number1: "))
b = int(input("enter a number12: "))

try:
    c = a/b
    print(c)
except ArithmeticError as e:
    print(" The division is not possible")
    print(f"Error, {e}")