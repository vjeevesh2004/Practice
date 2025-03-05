def insertionsort(element):
    n = len(element)

    for i in range(1,n):
        anchor = element[i]
        j = i-1
        while j>=0 and anchor<element[j]:
            element[j+1] = element[j]
            j = j - 1
        element[j+1] = anchor

if __name__ == "__main__":
    tests = [
        [11,9,29,7,2,15,28],
        [3,7,9,11],
        [25,22,21,10],
        [29,15,28],
        [],
        [6]
    ]

for element in tests:
    insertionsort(element)
    print(element)

