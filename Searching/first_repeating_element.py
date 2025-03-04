'''
Given an array of integers 
arr[], The task is to find
the index of first repeating 
element in it i.e. 
the element that occurs
more than once and whose
index of the first 
occurrence is the smallest. 
'''
def firstRepeatingElement(arr, n):
   for i in range(n):
    for j in range(i+1, n):
      if arr[i] == arr[j]:
        return i
      
    return -1
 
arr = [10, 5, 3, 4, 3, 5, 6]
n = len(arr)
  
index = firstRepeatingElement(arr, n)
print(index)
  
# if index == -1:
#  print("No repeating element found!")
# else:
#  print("First repeating element is", arr[index])
