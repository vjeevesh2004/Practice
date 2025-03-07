''' 
Write a Python program that
executes a list operation and 
handles an AttributeError exception
if the attribute does not exist.
'''

try:
    my_list = [1, 2, 3, 4, 5]
    # Attempting to call a non-existent method on a list
    my_list.non_existent_method()
except AttributeError as e:
    print("Error: The operation could not be completed because the attribute or method does not exist.")
    print(f"Details: {e}")


''' 
An AttributeError is raised when 
you try to access or call an attribute 
or method that does not exist for an object.
'''