def sel(lst):
    n=len(lst)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if lst[j] < lst[mini]:
                mini=j
                lst[i],lst[mini]=lst[mini],lst[i]

lst=[23,45,34,23,12]
sel(lst)
print("Insertion:",lst)