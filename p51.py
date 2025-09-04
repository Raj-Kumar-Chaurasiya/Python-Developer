# Write a program to explain the Armstrong number.

n = int(input("Enter number: "))
sum = 0
temp = n 
while temp>0:
    digit=temp%10
    sum = sum + digit **3
    temp = temp//10
if sum==n:
    print("Armstrong number")
else:
    print("Not Armstrong")