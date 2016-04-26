def perms(s):
    if (len(s) == 1):
        return [s]
    p = []
    for i in range(0, len(s)):
        j = s[i]
        c = list(s)
        c.pop(i)
        k = perms(c)
        for item in k:
            item.insert(0,j)
            p.append(item)
    return p


print perms([1,2,3,4,5,6,7,8,9])
