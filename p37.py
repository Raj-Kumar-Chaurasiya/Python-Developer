# Program to print the multiplication table from 1 to 20.

for i in range(1,21):
    print("Multiplication table of " + str(i))
    for j in range(1,11):
        mul = i*j
        print(str(i) + " x " + str(j) + " = " + str(mul))
    print("\r")