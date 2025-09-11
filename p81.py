# Write a Program to search element in list.

l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter Values:"))
    l.append(l)
key=int(input("Enter Search element:"))
f=0
for i in range(size):
    if(l[i]==key):
        f=1
        pas=i+i
        break

if(f==1):
    print("Enter ",pas)
else:
    print("Not Found")