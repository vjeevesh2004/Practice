#def myfunc(parameter):
 #   return
    # may or may not return a value

def calculate(a,b):
    sum_result = a + b
    diffrence = a - b
    product = a * b
    return sum_result, diffrence, product

result = calculate(10,5)
print(result) # packing
print(type(result)) # it will return type of result that is tuple, which we don't require. 

#unpacking the tuple
sum_result, difference, product = result
print(f"jue: {sum_result}")
print(f"diffrence: {difference}")
print(f"product: {product}")
print(type(difference))

# whenever the function return multiple values, then python will store all them together it in tuple by default, this process is called pakcing. 
# for the required value, programmer have to unpack it, for the desired resuls


