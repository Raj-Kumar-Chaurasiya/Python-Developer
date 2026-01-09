lst = [20,40,30,50,10]
key = int(input("Enter the number: "))

found = False
for i in range(len(lst)):
    if lst[i] == key:
        print("Found the position is : ",i)
        found = True
        break
if not found:
    print("Not Found")