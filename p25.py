# Program to calculate sum of series : 1 + 1/2 + 1/3 +......+ 1/n.
n= int(input("Enter the limit :"))
sum = 0
for i in range(1, n+1):
    sum = sum +1/i
print("Sum of Series =" + str(sum))