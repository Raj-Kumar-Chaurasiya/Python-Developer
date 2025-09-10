# write a program find the total number of even and odd element.

# Write a program to enter the element in list.

l=[]
size=int(input("Enter size:"))
for i in range(size):
    val=int(input("Enter Values:"))
    l.append(l)
print("Lists=",l)
even=0
odd=0
for i in range(size):
    if(l[i]%2==0):
        even=even+1
    else:
        odd=odd+1
print("Total Even = ",even)
print("Total odd = ",odd)