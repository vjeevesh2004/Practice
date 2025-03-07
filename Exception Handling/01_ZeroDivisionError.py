'''Write a Python program to handle 
a ZeroDivisionError exception when 
dividing a number by zero. '''

a = int(input("Enter a number: "))

try: 
    result = a/0
    print(result)
except ZeroDivisionError as e:
    print(e)