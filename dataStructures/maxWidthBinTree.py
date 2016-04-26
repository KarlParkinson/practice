import binTree
import queue


def maxWidth(tree):
    q = queue.Queue()
    q.enqueue(tree)
    count = q.size()
    mw = 0
    width = 0
    while (not q.isEmpty()):
        if (count == 0):
            count = q.size()
            mw = max(mw, width)
            width = 0
        currentNode = q.dequeue()
        width += 1
        count -= 1
        if (currentNode.getLeftChild()):
            q.enqueue(currentNode.getLeftChild())
        if (currentNode.getRightChild()):
            q.enqueue(currentNode.getRightChild())
    return mw


tree = binTree.BinaryTree(1)
tree.insertLeft(2)
tree.insertRight(3)
tree.getLeftChild().insertLeft(4)
tree.getLeftChild().insertRight(5)
tree.getRightChild().insertRight(8)
tree.getRightChild().getRightChild().insertLeft(6)
tree.getRightChild().getRightChild().insertRight(7)
print maxWidth(tree)
