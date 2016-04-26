def popCount(x):
    s = 0
    while (x > 0):
        if (x&1 == 1):
            s += 1
        x = x >> 1
    return s


def countTotalSetBits(n):
    s = 0
    for i in range(1,(n+1)):
        s += popCount(i)
    return s


#print countTotalSetBits(7)
popCount(65535)
