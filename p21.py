# Program to print fibonacci series.

n=int(input("Enter the list: "))
a=0
b=1
sum=0
print("Fibonacci Series: " + str(a) + " " +str(b), end=" ")
while sum<n:
    sum = a+b
    if sum>=n:
        break
    else:
        print(sum,end="")
    a=b
    b=sum