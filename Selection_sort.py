lst = [20,10,40,30,50,40,45]

for i in range(len(lst)):
    mid = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[mid]:
            mid = j
    lst[i], lst[mid] = lst[mid], lst[i]
print("Sorted :" ,lst)