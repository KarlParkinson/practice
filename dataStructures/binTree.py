class BinaryTree:

    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, val):
        currentLeft = self.getLeftChild()
        newLeft = BinaryTree(val)
        self.leftChild = newLeft
        newLeft.leftChild = currentLeft

    def insertRight(self, val):
        currentRight = self.getRightChild()
        newRight = BinaryTree(val)
        self.rightChild = newRight
        newRight.rightChild = currentRight

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, val):
        self.val = val

    def getRootVal(self):
        return self.val

    def inorder(self):
        if (self.leftChild):
            self.leftChild.inorder()
        print(self.val)
        if (self.rightChild):
            self.rightChild.inorder()

    def preorder(self):
        print(self.val)
        if (self.leftChild):
            self.leftChild.preorder()
        if (self.rightChild):
            self.rightChild.preorder()

    def postorder(self):
        if (self.leftChild):
            self.leftChild.postorder()
        if (self.rightChild):
            self.rightChild.postorder()
        print(self.val)


class BinarySearchTree(BinaryTree):

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent


    def insert(self, key, val):
        if (key == self.key):
            self.val = val
        elif (key > self.key):
            if (self.hasRightChild()):
                self.rightChild.insert(key, val)
            else:
                self.rightChild = BinarySearchTree(key, val, None, None, self)
        else:
            if (self.hasLeftChild()):
                self.leftChild.insert(key, val)
            else:
                self.leftChild = BinarySearchTree(key, val, None, None, self)

    def find(self, key):
        if (key == self.key):
            return self.val
        elif (key > self.key):
            if (self.hasRightChild()):
                return self.rightChild.find(key)
            else:
                return None
        else:
            if (self.hasLeftChild()):
                return self.leftChild.find(key)
            else:
                return None

    def delete(self, key):
        if (key == self.key):
            if (self.isLeaf()):
                self.deleteLeaf()
            elif (self.hasBothChildren()):
                self.deleteTwoChildTree()
            else:
                self.deleteOneChildTree()
        elif (key > self.key):
            if (self.hasRightChild()):
                self.rightChild.delete(key)
            else:
                return None
        else:
            if (self.hasLeftChild()):
                self.leftChild.delete(key)
            else:
                return None

    def deleteLeaf(self):
        if (self.isLeftChild()):
            self.parent.leftChild = None
        else:
            self.parent.rightChild = None

    def deleteOneChildTree(self):
        if (self.isLeftChild()):
            if (self.hasLeftChild()):
                self.parent.leftChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                self.parent.leftChild = self.rightChild
                self.rightChild.parent = self.parent
        elif (self.isRightChild()):
            if (self.hasLeftChild()):
                self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
        else:
            if (self.hasLeftChild()):
                self.replace(self.leftChild)
            else:
                self.replace(self.rightChild)

    
    def deleteTwoChildTree(self):
        successor = self.rightChild.findMin()
        successor.spliceOut()
        self.key = successor.key
        self.val = successor.val

    def spliceOut(self):
        if (self.isLeaf()):
            self.deleteLeaf()
        else:
            self.deleteOneChildTree()

    def replace(self, otherNode):
        self.key = otherNode.key
        self.val = otherNode.val
        self.leftChild = otherNode.leftChild
        self.rightChild = otherNod.rightChild
        if (self.hasLeftChild()):
            self.leftChild.parent = self
        if (self.hasRightChild()):
            self.rightChild.parent = self

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return (self.parent and self.parent == self)

    def isRightChild(self):
        return (self.parent and self.parent == self)

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasBothChildren(self):
        return (self.hasRightChild() and self.hasLeftChild())

    def findMin(self):
        if (self.hasLeftChild()):
            return self.leftChild.findMin()
        else:
            return self


