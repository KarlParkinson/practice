import binTree

def boundaryTraversal(tree):
    boundary = []
    printLeftBoundary(tree, boundary)
    printLeafNodes(tree.getLeftChild(), boundary)
    printLeafNodes(tree.getRightChild(), boundary)
    printRightBoundary(tree.getRightChild(), boundary)


def printLeftBoundary(tree, boundary):
    if (tree == None):
        return
    else:
        print tree.getRootVal()
        boundary.append(tree)
        printLeftBoundary(tree.getLeftChild(), boundary)

def printRightBoundary(tree, boundary):
    if (tree == None):
        return
    else:
        printRightBoundary(tree.getRightChild(), boundary)
        if (tree not in boundary):
            print tree.getRootVal()

def printLeafNodes(tree, boundary):
    if (tree == None):
        return
    if (tree.getLeftChild() == None and tree.getRightChild() == None and tree not in boundary):
        print tree.getRootVal()
        boundary.append(tree)
    else:
        printLeafNodes(tree.getLeftChild(), boundary)
        printLeafNodes(tree.getRightChild(), boundary)


tree = binTree.BinaryTree(20)
tree.insertLeft(8)
tree.insertRight(22)
tree.getLeftChild().insertLeft(4)
tree.getRightChild().insertRight(25)
tree.getLeftChild().insertRight(12)
tree.getLeftChild().getRightChild().insertLeft(10)
tree.getLeftChild().getRightChild().insertRight(14)
tree.getLeftChild().getLeftChild().insertRight(2)
boundaryTraversal(tree)
