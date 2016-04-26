def sumDigits(n):
    digSums = [0 for i in range(n+1)]
    for i in range(n+1):
        digSums[i] = i%10 + digSums[i/10]
    return sum(digSums)


print sumDigits(12345678)
