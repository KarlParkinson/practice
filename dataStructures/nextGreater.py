import stack

def nge(arr):
    for i in xrange(len(arr)):
        e = arr[i]
        greater = False
        for j in xrange(i+1, len(arr)):
            if (arr[j] > e):
                print str(e) + "->" + str(arr[j])
                greater = True
                break
        if (not greater):
            print str(e) + "->" + str(-1)


def nge2(arr):
    s = stack.Stack()
    for e in arr:
        greater = False
        while (not s.isEmpty() and not greater):
            k = s.pop()
            if (k >= e):
                s.push(k)
                greater = True
            else:
                print str(k) + " -> " + str(e)
        s.push(e)
    while (not s.isEmpty()):
        print str(s.pop()) + " -> " + str(-1)
    



nge2([4,5,2,25])
print ""
nge2([13,7,6,12])
print ""
nge2([13,12,11,10])
print ""
nge2([1,2,3,4])

