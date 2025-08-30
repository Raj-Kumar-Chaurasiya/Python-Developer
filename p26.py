# Program to find greatest of three number.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a==b and b==c:
    print(str(a) + " " + str(b) + " " + str(c) + "are equal.")
    print("Enter different numbers:")
elif a>b:
    if a>c:
        print(str(a) + "is greatest")
    else:
        print(str(b) + "is greatest")
else:
    if b>c:
        print(str(b) + "is greatest")
    else:
        print(str(c) + "is greatest")
