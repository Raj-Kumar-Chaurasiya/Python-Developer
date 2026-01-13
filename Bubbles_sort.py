def bubble(lst):
    n= len(lst)
    for i in range(n):
        swapp=False
        for j in range(0,n-i-1):
            if lst[j]> lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swapp=True
        if not swapp:
            break
lst=[45,34,23,43]
bubble(lst)
print("Sorted:",lst)