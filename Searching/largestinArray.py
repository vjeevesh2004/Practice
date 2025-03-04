'''
Given an array arr. 
The task is to find the 
largest element in the given array. 
'''

def largest(arr,n):
    mx = arr[0]

    for i in range(1,n):
        if arr[i] > mx:
            mx = arr[i]
    return mx

arr = [10, 324, 45, 90, 9808]
n =len(arr)

ans = largest(arr,n)
print(ans)

''' working 
for the arr = [10, 324, 45, 90, 9808]

here in start, mx = 10
now iterate through the array, 
324 > 10 so mx = 324
45  > 324, no update, mx = 324
90 > 324, no update, mx = 324
9808> 324, update, mx = 9808
maxm element = 9808. 


'''