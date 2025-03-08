#  Write a Python function to find the maximum of three numbers.

def max_of_three(a,b,c):
    if a > b and a > c:
        return "a is largest"
    elif b > a and b >c:
        return "b is largest"
    else:
        return "c is largest"
    
print(max_of_three(90,8,134))