a = 54 # global variable
def func1():
    global a
    print(f" Print Statment 1: {a}")
    a = 8 # local variable if global variable is not used
    print(f" Print Statment 2: {a}")


func1()
print(f" Print Statment 3: {a}")
