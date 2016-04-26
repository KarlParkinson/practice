def LIS(arr):
    maxSub = [1]*len(arr)
    for i in xrange(len(arr)):
        maxVal = 1
        for j in xrange(0,i):
            if (arr[j] < arr[i]):
                maxVal = max(maxSub[j] + 1, maxVal)
        maxSub[i] = maxVal
    return max(maxSub)




a = [10,22,9,33,21,50,41,60,80]
print LIS(a)
