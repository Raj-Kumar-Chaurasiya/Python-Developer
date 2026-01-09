# Program to check whether the given number is prime or not.
n = int(input("Enter a number : "))
c = 0
for i in range(1,n+1):
    if n%i==0:
        c=c+i
if c==2:
    print(n + "is a prime number.")
elif n==1:
    print(n +"is neither prime nor composite.")
else:
    print(n + "is not a prime number.")