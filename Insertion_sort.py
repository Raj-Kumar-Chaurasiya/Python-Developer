def ins(lst):
    n=len(lst)
    for i in range(1,n):
        key=lst[i]
        j=i-1
        while j>=0 and lst[j] > key:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key

lst=[10,45,65,34,54]
ins(lst)
print("Sorting: ", lst)