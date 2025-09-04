# Write a program to explain the Armstrong number.

n = int(input("Enter number: "))
sum = 0
temp = n 
while temp>0:
    digit=temp%10
    sum = sum*10 + digit
    temp = temp//10
if sum==n:
    print("Palindrome number")
else:
    print("Not Palindrome")