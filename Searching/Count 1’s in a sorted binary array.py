def countones(arr,n):
    low = 0
    high = n-1
    while(low <= high):
        mid = (low+high)//2

        if (arr[mid] < 1):
            high = mid-1

        elif (arr[mid] > 1):
            high = mid+1

        else:

            if([mid] == n-1 or arr[mid + 1] != 1):
                return mid + 1
            else:
                low = mid + 1

    return 0

arr = [1,1,1,0,0]
n = len(arr)
print("The number of 1's in array", countones(arr,n))