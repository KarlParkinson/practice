def missingNum(arr):
    n = len(arr) + 1
    s = sum(arr)
    y = (n*(n+1))/2
    return y - s


print missingNum([1,2,4,5,6])
