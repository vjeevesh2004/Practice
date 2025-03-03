'''an array is there of n distinct elements sorted in ascending order, 
then find a fixed point in the array. Fixed point is an index[i] such that arr[i] equals i. 
if no fixed point then returns -1.'''

def linearSearch(arr,n):
    for i in range(n):
        if arr[i] is i:
            return i
    return -1

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(linearSearch(arr,n)))