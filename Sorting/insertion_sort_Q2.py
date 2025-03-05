''' compute the running median 
of a sequence of numbers. That is, given a
stream of numbers, print out the median
of the list so far on each new element.

the median of an even numbered list is 
the average of the two middle numbers.

sequence = [2,1,5,7,2,0,5] '''

def insertionsort(element):
    n = len(element)
    for i in range(1,n):
        anchor = element[i]
        j = i - 1
        while j>=0 and anchor < element[j]:
            element[j + 1] = element[j]
            j = j - 1 
        element[j + 1] = anchor

def median(element):
    sorted_list = []

    for i in range(len(element)):
        sorted_list.append(element[i])
        insertionsort(sorted_list)

        if (i + 1) % 2 == 1:
            median = sorted_list[i//2]
        else:
            median = (sorted_list[i //2] + sorted_list[(i // 2) + 1]) / 2
        print(median)
   
if __name__ == "__main__":
    sequence = [2, 1, 5, 7, 2, 0, 5]
    median(sequence)
