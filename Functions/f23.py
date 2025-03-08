''' Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]'''

def num_even(l):
    # if l % 2 == 0:
    return [num for num in l if num %2 == 0]
    # else:
      #  return "non-prime"
list = [2,3,1]
new_list = num_even(list)        
print(new_list)