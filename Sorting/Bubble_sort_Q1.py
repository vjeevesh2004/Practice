def bubble_sort(element,key):
    size = len(element)

    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if element[j][key] > element[j+1][key]:
                element[j], element[j+1] =  element[j+1], element[j]
                swapped = True

        if not swapped:
            break
if __name__ == "__main__":
    element = [
        {'name': 'mona', 'transaction_amount' : 1000, 'device' : 'iphone 10'},
        {'name': 'dhaval', 'transaction_amount' : 400, 'device' : 'google pixel'},
        {'name': 'kathy', 'transaction_amount' : 200, 'device' : 'vivo'},
        {'name': 'aamir', 'transaction_amount' : 900, 'device' : 'iphone 8'}
    ]
    # element = [5,9,2,1,67,34,88]3
    # bubble_sort(element, key = "transaction_amount")
    bubble_sort(element, key = "name")

    print(element)

