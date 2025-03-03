'''Program to find the minimum 
(or maximum) element of an array
'''

def getmin(arr,n):
    res = arr[0]
    for i in range(1,n):
        res = min(res, arr[i])
    return res
def getmax(arr,n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    return res

arr = [12, 1234, 45, 67, 1]
n = len(arr)
print("Minimum element of array:", getmin(arr,n))
print("Maximum element of array:", getmax(arr,n))
