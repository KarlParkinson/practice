import binTree

def sumTree(tree):
    if (tree == None):
        return 0
    oldVal = tree.getRootVal()
    newVal = sumTree(tree.getLeftChild()) + sumTree(tree.getRightChild())
    tree.setRootVal(newVal)
    return oldVal + newVal

def bstSumGreaterConvert(tree, accum):
    if (tree == None):
        return
    bstSumGreaterConvert(tree.getRightChild(), accum)
    accum += tree.getRootVal()
    tree.setRootVal(newVal)
    bstSumGreaterConvert(tree.getLeftChild(), accum)
    
    


t = binTree.BinaryTree(10)
t.insertLeft(-2)
t.insertRight(6)
t.getLeftChild().insertLeft(8)
t.getLeftChild().insertRight(-4)
t.getRightChild().insertLeft(7)
t.getRightChild().insertRight(5)
t.inorder()
print ""
sumTree(t)
t.inorder()

