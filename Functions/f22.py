''' Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
'''

def prime_num(num):
    if num<=1:
        return "non - prime"
    for i in range(2, int(num**0.5) + 1):
        if num%i==0:
            return "non - prime"
    return "prime"
print(prime_num(2))