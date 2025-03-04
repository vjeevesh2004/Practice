def dupLastElement(arr, n):
    if (arr == None or n<0):
        return
    
    for i in range(n-1,0,-1):

        if(arr[i] == arr[i-1]):
            print(i,arr[i])
            return
    print("no duplicate found")

arr = [1,2,3,3,4,4,5]
n = len(arr)
dupLastElement(arr,n)