# Program to reverse digits of the given number.
num = int(input("Enter a number : "))
n = num
rev = 0
while n>1:
    rem = int(n)%10
    rev = rev*10+rem
    n = int(n)/10
print("Reverse of : " + num + " = " + str(rev))