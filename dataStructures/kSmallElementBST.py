import binTree
import stack

def kthSmallestElement(bst, k):
    s = stack.Stack()
    _kthSmallestElement(bst, k, s)
    

def _kthSmallestElement(bst, k, s):
    if (bst == None):
        return
    else:
        _kthSmallestElement(bst.leftChild, k, s)
        s.push(bst.key)
        if (s.size() == k):
            t = s.pop()
            print t
            s.push(t)
            return
        else:
            _kthSmallestElement(bst.rightChild, k, s)



bst = binTree.BinarySearchTree(20,2)
bst.insert(8,5)
bst.insert(4,'k')
bst.insert(12,'l')
bst.insert(10,'h')
bst.insert(14,12)
bst.insert(22,'p')
kthSmallestElement(bst,3)
