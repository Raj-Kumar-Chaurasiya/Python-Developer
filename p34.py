# Program to print the following pattern.
# 1
# 23
# 456

n = 1
for i in range(1,4):
    for j in range(1,i+1):
        print(n,end = " ")
        n = n + 1
    print("\r")