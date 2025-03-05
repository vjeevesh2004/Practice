def merge_sor(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr)//2
    right = arr[mid:]
    left = arr[:mid]

    merge_sor(left)
    merge_sor(right)

    merge_two_sorted_list(left, right,arr)

    
def merge_two_sorted_list(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1 

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1
        
if __name__ == "__main__":
    test_Cases = [
        [10,3,15,7,8,23,98,29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
    for arr in test_Cases:
        merge_sor(arr)
        print(arr)
