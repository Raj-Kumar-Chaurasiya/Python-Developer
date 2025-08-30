# Program to print multiplication table of the given number.
n = int(input("Enter a number : "))
print("Multiplication table of " + n)
for i in range(1,11):
    mul = n*i
    print(n + "x" + str(i) + "i" + str(mul))