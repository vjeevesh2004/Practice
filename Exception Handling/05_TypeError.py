''' 
Write a Python program that
prompts the user to input two numbers
and raises a TypeError exception if 
the inputs are not numerical.
'''
try:
    a = input()
    b  = input()
    if not a.isdigit() or not b.isdigit():
        raise TypeError ('Only numerical values are allowe')

    a = int(a)
    b = int(b)
    print("The numbers are:",a, b)
except TypeError as e:
    # print("The given number is not numerical")
    print(f"Error, {e}")