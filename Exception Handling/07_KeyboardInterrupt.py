''' 
Write a Python program that 
prompts the user to input a number 
and handles a KeyboardInterrupt exception
if the user cancels the input.
'''
try:
    number = input("Enter a number: ")
    print(f"You entered: {number}")
except KeyboardInterrupt:
    print("\nInput was canceled by the user. Program terminated.")

''' 
a KeyboardInterrupt exception when the
 user cancels the input 
 (e.g., by pressing Ctrl+C):
'''