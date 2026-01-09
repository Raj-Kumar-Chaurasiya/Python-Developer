# Write a program to count vowel and consonents of string.

a = input("Enter values:")
vow = 0
cons = 0
for i in range(0,len(a)):
    if (a[i]!=''):
        if(a[i]=='a' or a[i]=='A' or a[i]=='e' or a[i]=='E' or a[i]=='i' or a[i]=='I' or a[i]=='o' 
           or a[i]=='O' or a[i]=='u' or a[i]=='U'  ):
          vow=vow+1
        else:
           cons=cons+1
print("Total Vowel=",vow)
print("Total Consonents=",cons)