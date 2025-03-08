'''Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20 '''

def sum_num(l):
    total = 0
    for num in l:
        total += num
    return total

l = (8, 2, 3, 0, 7)
print(sum_num(l)) 