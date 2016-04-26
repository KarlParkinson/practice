def bitonic(arr):
    maxLength = [1] * len(arr)
    for i in range(len(arr)):
        maxj = 0
        decrease = False
        print maxLength
        for j in range(i):
            Bj = 0
            if (j > 0 and arr[j] < arr[j-1]):
                decrease = True
            if (j > 0 and arr[j] > arr[j-1]):
                decrease = False
            if (arr[j] < arr[i] and not decrease):
                Bj = maxLength[j]
            if (arr[j] > arr[i]):
                Bj = maxLength[j]
                decrease = True
            maxj = max(Bj, maxj)
        maxLength[i] = maxj + 1
        
    print maxLength
    return max(maxLength)


arr = [11,1,2,10,4,5,2,1]
print bitonic(arr)
arr = [12,11,10,13,40,5,3,1]
print bitonic(arr)
arr = [80,60,30,40,20,10]
print bitonic(arr)
arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print bitonic(arr)
            
