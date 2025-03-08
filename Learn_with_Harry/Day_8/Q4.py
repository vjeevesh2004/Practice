# n! = (n-1)! *n 
# sum(n) = sum(n-1) + n 

def rec(n):
    if n==0 or n==1:
        return 1
    return (n+rec(n-1))

n = int(input("Enter your number: "))
print(rec(n))

