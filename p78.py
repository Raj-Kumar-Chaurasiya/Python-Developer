# write a program to using the list method.

l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter Values:"))
    l.append(l)
print("Lists=",l)
print("Maximum=",max(l))
print("Minimum=",min(l))
y=l.count(3)
print("Count=",y)
x=l.insert("mohan")
print("Insert=",x)
m=l.index(4)
print("Index=",m)
n=l.remove(2)
print("Remove",n)
h=l.reverse()
print("Reverse= ",h)
d=l.pop()
print(l)