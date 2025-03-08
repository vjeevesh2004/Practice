'''
Write a Python function to calculate the factorial of a number (a non-negative integer). 
The function accepts the number as an argument.
'''

a = int(input("Enter number"))
def fact(a):
    if a==0:
        return 0
    else:
        return a*fact(a-1)
print(fact) 