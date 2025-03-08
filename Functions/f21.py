''' Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_list(lts):
    return list(set(lts))

l = [1,2,3,4,5,5]
new_list = unique_list(l)
print(new_list)