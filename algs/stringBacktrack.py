import copy

def strPerms(string):
    _strPerms(list(string), 0)


def _strPerms(s, n):
    if (n == len(s) - 1):
        print "".join(s)
    for i in range(n, len(s)):
        c = copy.copy(s)
        temp = c[i]
        c[i] = c[n]
        c[n] = temp
        _strPerms(c, n+1)


strPerms("ABCDEFGHIJ")
        
        
        
