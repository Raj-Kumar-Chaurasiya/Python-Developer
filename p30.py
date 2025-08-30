# Program to find GCD of two number.
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if n1%i==0 and n2%2==0:
            gcd=i
print(str(gcd) + "is the greatest common divisor of " + str(n1) + " & " + str(n2))