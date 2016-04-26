import binTree


def sumLeftLeaves(tree):
    if (tree == None):
        return 0
    if (isLeaf(tree.getLeftChild())):
        return tree.getLeftChild().getRootVal() + sumLeftLeaves(tree.getRightChild())
    else:
        return sumLeftLeaves(tree.getLeftChild()) + sumLeftLeaves(tree.getRightChild())


def isLeaf(tree):
    if (tree == None):
        return False
    return (tree.getLeftChild() == None and tree.getRightChild() == None)
    


tree = binTree.BinaryTree(20)
tree.insertLeft(9)
tree.getLeftChild().insertLeft(5)
tree.getLeftChild().insertRight(12)
tree.getLeftChild().getRightChild().insertRight(15)
tree.insertRight(49)
tree.getRightChild().insertLeft(23)
tree.getRightChild().insertRight(52)
tree.getRightChild().getRightChild().insertLeft(50)

print sumLeftLeaves(tree)
