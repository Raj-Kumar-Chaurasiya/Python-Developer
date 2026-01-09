l=[12,34,56,78,98,45]
target=78

low=0
high=len(l)-1
found=False

while low <= high:
    mid=(low+high)//2
    if l[mid]==target:
        print("found",mid)
        found=True
        break
    elif target<l[mid]:
        high=mid-1
    else:
        low=mid+1
if not found:
    print("Not found")