def restoreY(A):
    for j in xrange(len(A)):
        y = A[j]
        firstHalf = performAnding(A, 0, j-1)
        secondHalf = performAnding(A, j+1, len(A)-1)
        if (j == 0):
            firstHalf = secondHalf
        if (j == len(A)-1):
            secondHalf = firstHalf
        if (y == firstHalf & secondHalf):
            return y
    return -1
    

def performAnding(arr, l, r):
    if (l < 0 or l > len(arr)-1):
        return
    val = arr[l]
    for j in xrange(l+1, r+1):
        val = val & arr[j]
    return val


print restoreY([1,3,5])
print restoreY([31,7])
print restoreY([31,7,7])
print restoreY([2,3,7,19])
print restoreY([1362,1066,1659,2010,1912,1720,1851,1593,1799,1805,1139,1493,1141,1163,1211])
print restoreY([1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1])
print restoreY([def restoreY(A):
    for j in xrange(len(A)):
        y = A[j]
        firstHalf = performAnding(A, 0, j-1)
        secondHalf = performAnding(A, j+1, len(A)-1)
        if (j == 0):
            firstHalf = secondHalf
        if (j == len(A)-1):
            secondHalf = firstHalf
        if (y == firstHalf & secondHalf):
            return y
    return -1191411,256951,191411,191411,191411,256951,195507,191411,192435,191411, 191411,195511,191419,191411,256947,191415,191475,195579,191415,191411, 191483,191411,191419,191475,256947,191411,191411,191411,191419,256947, 191411,191411,191411])
