# lambda funciton
# the function which is not defined by a name.
# it's a one line coded function
# it can be defined by the keyword lambda.

# lambda = argument(multiple):expression(only one)

#double = lambda x:x*2
#print(double(5))

#find greatest number
#max_funtion = lambda a,b:a if (a>b) else b 
#print(max_funtion(90,9))

# add 10 to the function
#x = lambda a : a + 10
#print(x(6))

# map and filter built in function 
numbers = [1,2,3,4,5]
evens = list(filter(lambda x: x%2==0,numbers)) # filter built in funtion is used to filter out the elements after the conditoion. 

doubles = list(map(lambda x:x*2,numbers)) #map built- in function is used to store the modify elements by the lambda function.

print(evens)
print(doubles)