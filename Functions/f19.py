'''Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

def count_upper_and_lower(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
    
s = input("Enter the String")

upper_count, lower_count = count_upper_and_lower(s)

print(f"Number of upper count: {upper_count} and Number of Lower count: {lower_count}")