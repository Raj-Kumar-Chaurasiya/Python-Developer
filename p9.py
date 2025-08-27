# program to find simple interest.
p = float(input("Enter principle amount:"))
r = float(input("Enter rate of interest:"))
n = float(input("Enter no. of year:"))
si = (p*r*n)/100
print("Simple Interest = " + str(si))