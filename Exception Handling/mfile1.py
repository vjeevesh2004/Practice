def greet(name):
    print(f"Good Morning, {name}")

# print(__name__)
if __name__ == "__main__":
    n = input("Enter a name\n")
    greet(n)

'''
this name funciton is mainly used
to print the file on another function. 

is used to check whether the
module is run directly or imported
to another file. 
'''
