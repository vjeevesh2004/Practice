try:
    a = int(input("enter a number"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value")
    print(e)

except ZeroDivisionError as e:
    print("make sure you are not dividing by 0")
    print(e)

print("Thanks for using this code!")