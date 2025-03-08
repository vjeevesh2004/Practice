''' Write a function to calculate the GCD of two numbers.
'''

def gcd(a,b):
    while b!= 0:
        a,b = b,a%b
    return a 

num_1 = 56 ; num_2 = 98 
print(f"the gcd of{num_1} and {num_2} is {gcd(num_1, num_2)}")