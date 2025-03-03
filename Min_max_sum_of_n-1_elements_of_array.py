# Find the minimum and maximum sum of N-1 elements of the array
def miniMaxSum(arr,n):
    minElement = 0
    maxElement = 0
    sum = 0

    minElement = arr[0]
    maxElement = minElement
    sum = minElement

    for i in range(1,n):
        sum += arr[i]
        
        if (arr[i] < minElement):
            minElement = arr[i]
        if (arr[i] > maxElement):
            maxElement = arr[i]

    print(sum - maxElement, sum - minElement)

a1 = [13, 5, 11, 9, 7]
n = len(a1)
miniMaxSum(a1, n)
