import binTree

def equalTrees(t1, t2):
    if (t1 == None or t2 == None):
        return compNoneTrees(t1,t2)
    else:
        if (t1.getRootVal() != t2.getRootVal()):
            return False
        else:
            return equalTrees(t1.getLeftChild(), t2.getLeftChild()) and equalTrees(t1.getRightChild(), t2.getRightChild())

def compNoneTrees(t1,t2):
    return (t1 == None and t2 == None)


t1 = binTree.BinaryTree(1)
t1.insertLeft(2)
t1.insertRight(3)
t1.getLeftChild().insertLeft(4)
t1.getLeftChild().insertRight(5)

t2 = binTree.BinaryTree(1)
t2.insertLeft(2)
t2.getLeftChild().insertLeft(4)
t2.getLeftChild().insertRight(5)

print equalTrees(t1,t2)
