# Program to print the following pattern.
# 1
# 12
# 123

for i in range(1,4):
    for j in range(1,i+1):
     print(j,end=" ")
    print("\r")