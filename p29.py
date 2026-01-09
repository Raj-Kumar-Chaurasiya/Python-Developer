# Program to find perfect number.
def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum = sum + i
    return sum
num = int(input("Enter a number : "))
if perfect(num)==num:
    print(str(num) + " is a perfect number .")
else:
    print(str(num) + " is not a perfect number . ")