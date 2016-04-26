def bitStrings(n):
    if (n == 1):
        return['0', '1']
    else:
        L1 = bitStrings(n-1)
        L2 = []
        for string in L1:
            s = list(string)
            s.insert(0,'0')
            L2.append(''.join(s))
            s.pop(0)
            s.insert(0,'1')
            L2.append(''.join(s))
        return L2


print(bitStrings(3))
