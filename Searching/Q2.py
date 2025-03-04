'''Write a Python program for binary search of an ordered list.
Test Data :
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3) -> True
Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17) -> False
'''

def binary_search(arr,target):
    left = 0
    high = len(arr) - 1

    while (left <= high):
        mid = (left + high) //2

        if (arr[mid] == target):
            return True
        elif (arr[mid] > target):
            high = mid -1
        else:
            left = mid + 1
    return False

print(binary_search([0,1,3,8,14,18,19, 34, 52],3))