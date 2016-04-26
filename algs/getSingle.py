def getSingle(arr):
    bitLength  = 32
    result = 0
    for i in range(0, bitLength+1):
        s = 0
        bitMask = 1 << i
        for j in arr:
            if (j & bitMask > 0):
                s += 1
        if (s%3 > 0):
            result |= bitMask
    return result



print getSingle([12,1,12,3,12,1,1,2,3,3])




