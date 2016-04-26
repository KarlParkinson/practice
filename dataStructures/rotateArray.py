def rotate(arr, d):
    if (d > len(arr)-1):
        return
    temp = []
    for i in xrange(d, len(arr)):
        temp.append(arr[i])
    for i in xrange(0, d):
        temp.append(arr[i])
    for i in xrange(len(temp)):
        arr[i] = temp[i]
    


a = [1,2,3,4,5,6,7]
rotate(a,8)
print a
