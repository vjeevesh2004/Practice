'''Modify the Insertion Sort algorithm 
to sort a list in descending order.
arr = [8, 4, 3, 7, 6, 5, 2] '''

def sorrt(element):
    n = len(element)

    for i in range(1,n):
        anchor = element[i]
        j = i -1
        while j >= 0 and anchor > element[j]:
            element[j+1] = element[j]
            j=j-1
        element[j + 1]=anchor

if __name__ == "__main__":
    element = [8,4,3,7,6,5,2]
    sorrt(element)
    print(element)
        