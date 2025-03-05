'''
Modify such that it can sort the following list of 
athletes as per the time taken by them in the 
marathon.
elements = [
        { 'name' : 'vedanth', 'age':17, 'time_hours':1},
        { 'name' : 'rajab', 'age':12, 'time_hours':3},
        { 'name' : 'vignesh', 'age':21, 'time_hours':2.5},
        { 'name' : 'chinmay', 'age':24, 'time_hours':1.5},
]
'''
def merge_sorrt(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sorrt(left)
    merge_sorrt(right)

    merge_two_sorted_list(left,right,arr)

def merge_two_sorted_list(a,b,arr):
    aa = len(a)
    bb = len(b)
    i = j = k = 0

    while i < aa and j < bb:
        if a[i]['time_hours'] <= b[j]['time_hours']:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
    while i < aa:
        arr[k] = a[i]
        i+=1
        k+=1
    while j < aa:
        arr[k] = b[j]
        j+=1
        k+=1

elements = [
        { 'name' : 'vedanth', 'age':17, 'time_hours':1},
        { 'name' : 'rajab', 'age':12, 'time_hours':3},
        { 'name' : 'vignesh', 'age':21, 'time_hours':2.5},
        { 'name' : 'chinmay', 'age':24, 'time_hours':1.5},
]

sorrted = merge_sorrt(elements)
for athlete  in sorrted:
    print(athlete)