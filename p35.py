# Program to print the following pattern.
#    *
#  *   *
# *  *   *
 
for i in range(1,4):
    for j in range(i,4):
        print(end=" ")
    for k in range(1,i+1):
        print("* ",end="")
    print("\r")