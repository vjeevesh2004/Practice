 # n! = 1 * 2 * 3 * 4.....*n
# n! = [1 * 2 * 3 * 4....n-1]*n
# n! = n*(n-1)!
# n = 4
# product = 1
# for i in range(n):
#    product = product * (i+1)
# print(product)

def factorial_iter(n): # iter = iterative factorial method
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
f = factorial_iter(5)
print(f) 
                  # OR 

def factorial_recursive(n):
    if n == 1 or n == 0:    # base condition
        return 1
    return n * factorial_recursive(n-1)
f = factorial_recursive(4)
print(f) 



