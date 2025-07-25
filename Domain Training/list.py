numbers = [1,2,3,4,5]
mixed = [1,"Hello", 3.14, True]
empty_list = []
nested_list = [1, [1,2], [4,5]]

numbers = [10, 20, 30, 40, 50]
print(numbers[1]) # output: 20

''' list methods 
1. append(): to only one element  add at last
2. extend() : to add multiple elements in the list 
3. insert() : to add element at a specific location 
4. remove() : remove the first occurence of that specified element
5. pop() : remove and return the element at that index
6. count() : to count the occurence of element
7. reverse() : reverse the order of list 
8. copy() : return a copy that list 
9. clear() : remove all elements present in the list 
'''

l = [1,2,3,4,5]
l.append(90)
print(l)

l.remove(3)
print(l)

l.reverse()
print(l)

l.clear()
print(l)




