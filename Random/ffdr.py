# Define a list
my_list = [int(x) for x in input("enter list element: ")]

# Print the original list
print("Original list:", my_list)

# Swap the first and last elements
if len(my_list) > 1:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]

# Print the swapped list
print("Swapped list:", my_list)
