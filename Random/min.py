a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
min = a
if a<b and a<c:
    print("a is min")
elif b<a and b<c:
    print("b is min")
else:
    print("c is min")