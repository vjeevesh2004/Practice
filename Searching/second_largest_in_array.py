'''
Given an array of positive integers arr[] 
of size n, the task is to 
find second largest distinct element
in the array.
'''
def secondLargest(arr,n):
    # n=len(arr)
    largest = -1
    secondlargest = -1

    for i in range(0,n):

        if arr[i] > largest:
            secondlargest = largest
            largest = arr[i]
        
        elif arr[i] < largest and arr[i]> secondlargest:
            secondlargest = arr[i]

    return secondlargest

arr = [10, 12, 35, 1, 10, 30]
n= len(arr)
print(secondLargest(arr,n))
