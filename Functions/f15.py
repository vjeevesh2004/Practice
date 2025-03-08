'''Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336 '''

def multiply_num(l):
    total = 1
    for a in l:
        total *= a
    return total

print(multiply_num([1,3,4]))