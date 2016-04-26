import binTree
import queue

def complete(tree):
    q = queue.Queue()
    nonFull = False
    q.enqueue(tree)

    while (not q.isEmpty()):
        t = q.dequeue()
        if (t.getLeftChild()):
            if (nonFull):
                return False
            q.enqueue(t.getLeftChild())
        if (t.getLeftChild() == None):
            nonFull = True
        if (t.getRightChild()):
            if (nonFull):
                return False
            q.enqueue(t.getRightChild())
        if (t.getRightChild() == None):
            nonFull = True

    return True
            


t = binTree.BinaryTree(1)
t.insertLeft(2)
t.insertRight(3)
t.getRightChild().insertLeft(5)
t.getRightChild().insertRight(6)
print complete(t)
