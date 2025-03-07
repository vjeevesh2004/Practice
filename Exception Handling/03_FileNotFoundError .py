''' 
Write a Python program that opens 
a file and handles a FileNotFoundError 
exception if the file does not exist.
'''

filename = input("enter the name of the file to open: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("file content: ")
        print(content)

except FileNotFoundError as e:
    print(f"Error: the file {filename} does not exist")
    