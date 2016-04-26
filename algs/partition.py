def partition(arr):
    p = arr[0]
    s = 0
    for i in range(1, len(arr)):
        if (arr[i] < p):
            s += 1
            temp = arr[s]
            arr[s] = arr[i]
            arr[i] = temp
    temp = arr[s]
    arr[s] = arr[0]
    arr[0] = temp
    return arr,s


print(partition([4,7,2,1,3,8,9]))
    
