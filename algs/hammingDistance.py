def hd(s1,s2):
    count = 0
    for j in xrange(len(s1)):
        if (s1[j] != s2[j]):
            count += 1
    return count


def minD(c):
    for j in xrange(len(c)):
        for i in xrange(j+1, len(c)):
            print hd(c[j], c[i])



C = ['000', '011', '022', '101', '112', '120', '202', '210', '221']
minD(C)
