'''
Given an array arr[] of size n-1 
with distinct integers in the range 
of [1, n]. This array represents a
permutation of the integers from 1 
to n with one element missing. 
Find the missing element in the array.
'''

def missingelement(arr):
    n=len(arr) + 1

    totalsum = sum(arr)

    expectedsum = (n*(n+1))//2

    return expectedsum - totalsum

arr = [1,2,3,5]
print(missingelement(arr))