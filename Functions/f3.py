def product_list(num):
    result = 1  
    for num in num:
        result *= num  
    return result

x=(8, 2, 3, -1, 7)
print(product_list(x))
