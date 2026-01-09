# Write a program to check a string is palindrom or not.

a = input("Enter Values:")
b = a[-1::-1]
if(a==b):
    print("Palindrom")
else:
    print("Not Palindrom")