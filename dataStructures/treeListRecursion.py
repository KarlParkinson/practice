import binTree

def treeToList(tree):
    if (tree.getLeftChild() == None and tree.getRightChild() == None):
        tree.leftChild = tree
        tree.rightChild = tree
        return tree
    leftList = treeToList(tree.getLeftChild())
    rightList = treeToList(tree.getRightChild())
    return concatenate(leftList, rightList, tree)


def concatenate(left, right, middle):
    # concatenate two CDLL together with middle element in-between
    
    # find last node in left list
    rightLeft = left.leftChild
    # find last node right list
    rightRight = right.leftChild
    
    # add middle element
    middle.leftChild = rightLeft
    rightLeft.rightChild = middle
    middle.rightChild = right
    right.leftChild = middle
    
    # complete circle
    left.leftChild = rightRight
    rightRight.rightChild = left
    
    # return head
    return left

def traverse(head):
    current = head
    print current.getRootVal()
    current = current.rightChild
    while (current != head):
        print current.getRootVal()
        current = current.rightChild


tree = binTree.BinaryTree(10)
tree.insertLeft(9)
tree.insertRight(12)
tree.getLeftChild().insertLeft(15)
tree.getLeftChild().insertRight(6)
tree.getRightChild().insertLeft(16)
tree.getRightChild().insertRight(18)
l = treeToList(tree)
traverse(l)

