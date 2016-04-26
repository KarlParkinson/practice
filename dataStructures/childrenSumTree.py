import binTree

def hasChildSumProperty(tree):
    if (tree == None):
        return True
    else:
        if (tree.getLeftChild() or tree.getRightChild()):
            leftHas = hasChildSumProperty(tree.getLeftChild())
            rightHas = hasChildSumProperty(tree.getRightChild())
            leftVal = 0
            rightVal = 0
            if (tree.getLeftChild()):
                leftVal = tree.getLeftChild().getRootVal()
            if (tree.getRightChild()):
                rightVal = tree.getRightChild().getRootVal()
            hasProperty = tree.getRootVal() == (leftVal + rightVal)
            return (leftHas and rightHas and hasProperty)
        else:
            return True


tree = binTree.BinaryTree(10)
tree.insertLeft(8)
tree.insertRight(2)
tree.getLeftChild().insertLeft(4)
tree.getLeftChild().insertRight(5)
tree.getRightChild().insertLeft(2)
print hasChildSumProperty(tree)
