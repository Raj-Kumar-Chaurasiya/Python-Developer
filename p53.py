# Write a program in tribonacci series.

n = int(input("Enter number of terms: "))

a, b, c = 0, 1, 1

if n >= 1:
    print(a, end=' ')
if n >= 2:
    print(b, end=' ')
if n >= 3:
    print(c, end=' ')

for i in range(3, n):
    d = a + b + c
    print(d, end=' ')
    a, b, c = b, c, d
