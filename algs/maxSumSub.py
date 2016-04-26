def maxSumSub(arr):
    maxSums = [0]*len(arr)
    for i in range(len(arr)):
        Si = arr[i]
        maxS = Si
        for j in range(0,i):
            if (arr[j] < arr[i]):
                s = maxSums[j] + arr[i]
                if (s > maxS):
                    maxS = s
        maxSums[i] = maxS
    return max(maxSums)



arr = [1,101,2,3,100,4,5]
print maxSumSub(arr)
arr = [3,4,5,10]
print maxSumSub(arr)
arr = [10,5,4,3]
print maxSumSub(arr)
