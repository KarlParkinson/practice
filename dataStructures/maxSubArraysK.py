def maxSubArrays(k, arr):
    for i in xrange(len(arr)-(k-1)):
        maxVal = arr[i]
        for j in xrange(i, i+k):
            maxVal = max(maxVal, arr[j])
        print maxVal



maxSubArrays(3, [1,2,3,1,4,5,2,3,6])
print ""
maxSubArrays(4, [8,5,10,7,9,4,15,12,90,13])
