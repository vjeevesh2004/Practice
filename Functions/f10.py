# Define a function to calculate the sum of all numbers in a given list.

def sum_of_all_numbers(l):
    return sum(l)

l=[0,4.5,6]
print(sum_of_all_numbers(l))


def sum_of_numbers(l):
    total=0
    for num in l:
        total += num
    return total

l=[0,0.9]
print(sum_of_numbers(l))