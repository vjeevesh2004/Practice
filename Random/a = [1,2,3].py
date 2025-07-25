#a = [1,2,3]
#b = a[:]
#b[0] = 5#print(a)

#import math
#print(math.factorial(24))

#import numpy as np 
#x = np.array([[1,2,3],[8,9,19]],np.int32)
#print(type(x))
#print(x.shape)
#print(x.dtype)

#rows = 5
#for i in range(1,5):
 #   for j in range(1,5):
  #      if j>=i:
   #         print("*",end='')
     #   else:
    #        print(" ",end='')
    #print()

#import math
#def circle(r):
 #   area = 4 * math.pi*r*r
  #  circumference = 2*math.pi*r
   # return area, circumference

#a,c = circle(3)
#print("The area is: ", a )
#print("The circumference is: ", c)

#n= int(input("Enter number: "))
#cube = lambda x : x**3
#print("The cube of the number is: ", cube(n))

def max_of_two(x, y):
    # Check if x is greater than y
    if x > y:
        # If x is greater, return x
        return x
    # If y is greater or equal to x, return y
    return y
