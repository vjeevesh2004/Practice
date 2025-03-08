def percent(marks): # here marks is optional  
    return((sum(marks)/400)*100)

marks1 = [45, 78, 86, 77]
# percentage1 = (sum(marks1)/400)*100 # sum function is used for addition 
percentage1 = percent(marks1)

marks2 = [75,98,88,78]
# percentage2 = (sum(marks2)/400)*100
percentage2 = percent(marks2)
print(percentage1, percentage2)


def mySum(num1, num2):
    return num1 + num2

s = mySum(6, 32)
print(s) 