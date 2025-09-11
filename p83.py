# Write a program to find maximum value in list.

l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter Values:"))
    l.append(l)
max=l[0]
for i in range(size):
    if(l[i]>max):
        max=l[i]

print("Maximum values",max)