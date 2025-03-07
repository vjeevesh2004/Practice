'''
Write a Python program that opens
a file and handles a PermissionError 
exception if there is a permission issue
'''

filename = input("enter the name of the file to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("file content: ")
        print(content)

except PermissionError as e:
    print(f"Error: the file do not have permission to open")
    print(e)