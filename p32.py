# Program to check entered string is palindrome or not without function.
s1 = input("Enter a string: ")
s2 = s1[::-1]
if s1==s2:
    print(s1 + "is a palindrome string. ")
else:
    print(s2 + "is not a palindrome string. ")