def pairSum(arr, x):
    arr.sort()
    l = 0
    r = len(arr)-1
    while (l < r):
        s = arr[l] + arr[r]
        if (s == x):
            return True
        elif (s > x):
            r -= 1
        elif (s < x):
            l += 1
    return False



a = [4,5,1,2,8]
x = 8
print pairSum(a,x)
