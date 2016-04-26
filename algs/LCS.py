def LCS(s1, s2):
    if (s1 == "" or s2 == ""):
        return 0
    else:
        if (s1[-1] == s2[-1]):
            return LCS(s1[:-1], s2[:-1]) + 1
        else:
            return max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))


def LCS2(s1, s2):
    l = [[0]*(len(s1)+1) for j in xrange(len(s2)+1)]
    for i in xrange(1, len(s2)+1):
        for j in xrange(1, len(s1)+1):
            if (s2[i-1] == s1[j-1]):
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    return l[len(s2)][len(s1)]



print LCS2("ABCDGH", "AEDFHR")
print LCS2("AGGTAB", "GXTXAYB")
