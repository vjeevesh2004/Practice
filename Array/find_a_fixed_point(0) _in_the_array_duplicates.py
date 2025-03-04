'''
Given an array of n integers sorted 
in ascending order, write a function 
that returns a Fixed Point in the array,
if there is any Fixed Point present in 
the array, else returns -1.
Fixed Point in an array is an index
such that arr[i] is equal to i. 
Note that integers in the array 
can be negative. 
'''

def findfixedPoint(arr):
    n=len(arr)
    for i in range(n):
        if arr[i] == i:
            return i
    return -1
arr = [-10, -5, 2,2,2,3,4,7,9,12,13]
fixedPoint = findfixedPoint(arr)
if fixedPoint == -1:
    print("No Magic Index")
else:
    print(f"Magic Index is : {fixedPoint}")