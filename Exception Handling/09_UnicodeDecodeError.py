''' 
Write a Python program that
 opens a file and handles a
   UnicodeDecodeError exception 
   if there is an encoding issue.
'''

filename = input("Enter the name of the file to open: ")

try:
    # Open the file with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as file:          
        content = file.read()
        print("File content:")
        print(content)
        
except UnicodeDecodeError as e:
    print("Error: The file could not be decoded with UTF-8 encoding.")
    print(f"Details: {e}")
except FileNotFoundError:
    print("Error: The file does not exist.")
