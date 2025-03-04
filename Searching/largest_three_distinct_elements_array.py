'''
Given an array arr[], 
the task is to find the 
top three largest distinct
integers present in the array.
'''

def findthreelargest(arr,n):

    if len(arr) < 3:
        print("Invalid Input")
        return 
    
    third = first = second = float('-inf')
    # third = first = second = -1/0 both will work
    for i in range(n):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]

        elif arr[i] > third and arr[i] != second and arr[i]!=  first:
            third = arr[i]

    print("The three larget element are", first, second, third)

arr = [10, 89, 8, 30, 45]
n  = len(arr)
print(findthreelargest(arr,n))

'''
working:
arr = [10, 89, 8, 30, 45]
10>-inf, update, first = 10, second = -inf, third = inf
89 >10, update, first = 89, second = 89, three = inf
8 >-inf, update, first = 10, second = 89, three = 8
30 > 10, update, second = 30, third = 10
45 > 30, update, second = 45, third = 30
'''