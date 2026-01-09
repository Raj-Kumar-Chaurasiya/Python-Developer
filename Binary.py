lst = [20,30,40,10,50]
key = int(input("Enter the number : "))

low = 0
high = len(lst) - 1
found = False

while low <= high :
    mid = (low+high) // 2
    if lst[mid] == key:
        print("Found ", mid)
        found = True
        break
    elif key <lst[mid]:
        high = mid-1
    else:
        low = mid+1

if not found:
    print("Not found")