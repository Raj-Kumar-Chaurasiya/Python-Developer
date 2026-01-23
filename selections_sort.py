def sel(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min] , arr[i]
    return arr

arr= [ 34,65,23,12,3]
print(sel(arr))