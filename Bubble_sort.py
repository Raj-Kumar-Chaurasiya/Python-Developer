lst = [20,30,40,50,60,50,10]

for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] =lst[j+1], lst[j]
print("Sorted :",lst)