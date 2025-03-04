''' Write a Python program for binary search.
Binary Search : In computer science, 
a binary search or half-interval search 
algorithm finds the position of a target 
value within a sorted array. 
The binary search algorithm can be 
classified as a dichotomies 
divide-and-conquer search algorithm and 
executes in logarithmic time.
Test Data :
binary_search([1,2,3,5,8], 6) -> False
binary_search([1,2,3,5,8], 5) -> True '''

def binary_search(arr, target):
    left, right = 0, len(arr) -1
    
    while (left <= right):
        mid = (left + right)//2

        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return False

print(binary_search([1,2,3,4,5,8],6))
