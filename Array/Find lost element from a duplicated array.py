# Find lost element from a duplicated array
''' 
Given two arrays that are duplicates 
of each other except one element, that is one 
element from one of the array is missing, we need 
to find that missing element.

arr1[] = {1,4,5,7,9}
arr2[] = {4,5,7,9}
output = 1
1 is missing form second array
'''
# this is only for two arrays

def lostElement(arr1,arr2,M,N):
    element = 0
    for i in range(M):
        element = element^arr1[i]
    for i in range(N):
        element = element^arr2[i]
    
    print(f"the lost element in the array : {element}")

arr1 = [4,11,5,6,0,7]
arr2 = [5,6,7,4,0]
M = len(arr1)
N = len(arr2)
lostElement(arr1, arr2, M, N)

# this method is for more than two arrays(multiple) arrays
def find_missing_multiple(arrays):
    xor_result = 0
    for arr in arrays:
        for num in arr:
            xor_result ^= num
    return xor_result

# Example arrays
arr1 = [4, 1, 5, 9, 7]
arr2 = [4, 1, 9, 7]
arr3 = [4, 1, 9, 7]

# Find the missing element
arrays = [arr1, arr2, arr3]
print(find_missing_multiple(arrays)) 