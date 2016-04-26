import binTree
import queue
import stack

def levelOrder(t):
    if (t == None):
        return
    q = queue.Queue()
    q.enqueue(t)
    while (not q.isEmpty()):
        currentNode = q.dequeue()
        print currentNode.getRootVal(),
        if (currentNode.getLeftChild()):
            q.enqueue(currentNode.getLeftChild())
        if (currentNode.getRightChild()):
            q.enqueue(currentNode.getRightChild())


def levelOrderLineByLine(t):
    if (t == None):
        return
    q = queue.Queue()
    q.enqueue(t)
    count = q.size()
    while (not q.isEmpty()):
        if (count == 0):
            count = q.size()
            print ''
        currentNode = q.dequeue()
        print currentNode.getRootVal(),
        if (currentNode.getLeftChild()):
            q.enqueue(currentNode.getLeftChild())
        if (currentNode.getRightChild()):
            q.enqueue(currentNode.getRightChild())
        count -= 1

def levelOrderReverse(t):
    if (t == None):
        return
    q =  queue.Queue()
    s = stack.Stack()
    q.enqueue(t)
    while (not q.isEmpty()):
        currentNode = q.dequeue()
        s.push(currentNode)
        if (currentNode.getRightChild()):
            q.enqueue(currentNode.getRightChild())
        if (currentNode.getLeftChild()):
            q.enqueue(currentNode.getLeftChild())

    while (not s.isEmpty()):
        print s.pop().getRootVal()



tree = binTree.BinaryTree(1)
tree.insertLeft(2)
tree.insertRight(3)
tree.getLeftChild().insertLeft(4)
tree.getLeftChild().insertRight(5)
levelOrder(tree)
print ""
levelOrderReverse(tree)
