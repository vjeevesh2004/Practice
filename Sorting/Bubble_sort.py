def bubble_sort(element):
    size = len(element)

    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if element[i] > element[i+1]:
                element[i], element[i+1] =  element[i+1], element[i]
                swapped = True

        if not swapped:
            break
if __name__ == "__main__":
    element = [5,9,2,1,67,34,88]
    bubble_sort(element)
    print(element)

