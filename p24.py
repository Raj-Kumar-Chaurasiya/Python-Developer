# Program to print prime number between 1 to 100.
c = 0
print("Prime number from 1-100 ")
print("1 is neither prime nor composite. ")
for i in range(1,100):
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if(c==2):
        print(i,end=" ")
    c=0