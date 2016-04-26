import pdb
import binTree

#def rootLeafPaths(t, path):
#    pdb.set_trace()
#    if (t == None):
#        pdb.set_trace()
#        print path
#    else:
#        pdb.set_trace()
#        path.append(t.getRootVal())
#        pdb.set_trace()
#        rootLeafPaths(t.getLeftChild(), path)
#        pdb.set_trace()
#        rootLeafPaths(t.getRightChild(), path)

def rootLeafPaths(t, path):
    if (t != None):
        path.append(t.getRootVal())
        left = t.getLeftChild()
        right = t.getRightChild()
        if (left == None and right == None):
            print (path)
            path.pop()
            return
        else:
            if (left):
                rootLeafPaths(left, path)
            if (right):
                rootLeafPaths(right, path)
        path.pop()

t = binTree.BinaryTree(1)
t.insertLeft(2)
t.insertRight(3)
t.getLeftChild().insertLeft(4)
t.getLeftChild().insertRight(5)

rootLeafPaths(t, [])
