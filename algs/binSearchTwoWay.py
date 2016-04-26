import pdb

def binSearch(arr, l, r, k):
#    print(l)
#    print(r)
#    pdb.set_trace()
    if (l <= r):
#        pdb.set_trace()
        if (l == r):
            if (arr[l] == k):
#                pdb.set_trace()
                return l
            else:
                return false
        else:
#            pdb.set_trace()
            m = (r+l)//2
#            pdb.set_trace()
            if (arr[m] <= k):
#                pdb.set_trace()
                if (arr[m] == k):
                    return m
                else:
 #                   pdb.set_trace()
                    l = m+1
                    return binSearch(arr, l, r, k)
            else:
 #               pdb.set_trace()
                r = m-1
                return  binSearch(arr, l, r, k)
    else:
 #       pdb.set_trace()
        return false


a = [1,2,3,4,5]
print(binSearch(a, 0, len(a)-1, 1))
