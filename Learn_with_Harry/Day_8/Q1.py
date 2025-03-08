# greatest between three number 
def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

# smallest between three number

def min(num1, num2, num3):
    if(num1<num2):
        if(num1<num3):
            return num1 
        else:
            return num3
    
    if (num2<num3):
        return num2
    else:
        return num3
    


m  = maximum(3,5,2)
# n = minimum(3,45,89000)
print("the value of maximum is" + str(m))
# print("the value of minimkum is" + str(n))