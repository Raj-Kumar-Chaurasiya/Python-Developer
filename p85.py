# Write a program to reverse the list itself.

l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter Values:"))
    l.append(l)
i=0
j=size-1
while(i<j):
    t=l[i]
    l[i]=l[j]
    l[j]=t
    i=i+1
    j=j+1
print("List after reverse :")
for i in range(size):
    print(l[i])