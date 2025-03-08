# Write a function that checks if a string is a palindrome.
def check_palindrome(a):
    temp = n
    rev = 0
    while n >0:
        dig = n%10
        rev = rev%10 +dig
        n=n//10
    return temp == rev
num = input("Enter a number: ")
# Check if the number is a palindrome
if check_palindrome(num):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")