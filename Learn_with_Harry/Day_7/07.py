n = 3
for i in range(3): # it depicts row number
    print(" " * (n-1-i), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))