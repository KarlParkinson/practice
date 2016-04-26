import copy

def countSets(N, W, H):
    stamps = [2**i for i in xrange(N)]
    countSetsUtil(N, W, H, [], stamps, 0)


def countSetsUtil(N, W, H, s, stamps, spot):
    print W,
    print H
#    if (covered(W, H)):
#        print s
    for i in xrange(spot, len(stamps)):
        s.append(stamps[i])
        countSetsUtil(N-1, W-stamps[i], H-stamps[i], s, stamps, i+1)
        s.pop()
        i -= 1

def covered(W, H):
    return (W <= 0) and (H <= 0)


countSets(3, 3, 5)
