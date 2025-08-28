# Program to check whether entered year is leap year or not .
year = int(input("Enter a year: "))
if year%400==00:
    print(str(year) + "is leap year")
elif year%4==00 and year%100!=0:
    print(str(year) + "is a leap year.")
else:
    print(str(year) + "is not leap year.")