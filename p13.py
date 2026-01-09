# Program to calculate gross salary.
bsal = float(input("Enter basic salary: "))
print("Dearness Allowance is 10%")
print("House Rent Allowance is 12%")
da = (10*bsal)/100
hra = (12*bsal)/100
print("Dearness Allowance = " + str(da))
print("House Rent Allowance = " + str(hra))
grs = bsal + da + hra
print("Gross Salary = " + str(grs))
