# Write a Program to find the second minimum values in lists.

l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter Values:"))
    l.append(l)
minval=min(l)
print("Minimum Values:",minval)
l.remove(minval)
smin=min(l)
print("Second Minimum: ",smin)