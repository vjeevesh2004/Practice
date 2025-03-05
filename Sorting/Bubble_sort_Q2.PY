'''
Write a Python program to sort a list of 
elements using the bubble sort algorithm.
Note : According to Wikipedia "Bubble sort, 
sometimes referred to as sinking sort, 
is a simple sorting algorithm that repeatedly 
steps through the list to be sorted, compares 
each pair of adjacent items and swaps them 
if they are in the wrong order. 
The pass through the list is repeated until 
no swaps are needed, which indicates that the
list is sorted. The algorithm, which is a 
comparison sort, is named for the way smaller
Elements "bubble" to the top of the list.
Although the algorithm is simple, it is too 
slow and impractical for most problems even 
when compared to insertion sort. It can be 
practical if the input is usually in sort 
order but may occasionally have some 
out-of-order elements nearly in position."
Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]
'''

def bubblesort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

if __name__ == "__main__":
    arr = [14,46,43,27,57,41,45,21,70]
    bubblesort(arr)
    print(arr)
    