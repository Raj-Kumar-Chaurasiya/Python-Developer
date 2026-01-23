def merge_s(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) //2
    lift = merge_s (arr[:mid])
    right = merge_s (arr[mid:])

    return merge(lift,right)

def merge(lift,right):
    result = []
    i = j = 0
    while i < len(lift) and j < len(right):
        if lift[i] <= right[j]:
            result.append(lift[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(lift[i:])
    result.extend(right[j:])

    return result

arr=[23,54,32,3,45]
sort=merge_s(arr)
print(sort)