# Create a function to find the largest number in a list.
def find_largest_num(l):
    #l=[1,2,89,45]
    return max(l)

l=[1,2,89,45]
print(find_largest_num(l))

def find_largest_num_loop(l):
    largest = l[0]  # Assume first element is the largest initially
    for num in l:
        if num > largest:
            largest = num
    return largest

l = [1, 2, 89, 45]
print(find_largest_num_loop(l))

