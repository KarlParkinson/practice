def turnOff(n):
    mask = 1
    while((mask & n) != mask):
        mask = mask << 1
    mask = ~mask
    n = n & mask
    return n

print turnOff(7)
