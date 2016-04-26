import pdb

def powset(s):
#    pdb.set_trace()
    if (s):
#        pdb.set_trace()
        S = set()
        for i in s:
 #           pdb.set_trace()
            temp = {i}
 #           pdb.set_trace()
            S = S.union(powset(s.difference(temp))).union(temp)
 #           pdb.set_trace()
            print(S)
 #       pdb.set_trace()
        return S.union(s)
    else:
 #       pdb.set_trace()
        return set()

s = {1,2,3}
#print(type(s))
print(powset(s))
