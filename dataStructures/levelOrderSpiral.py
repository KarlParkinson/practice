import binTree
#import queue
#import stack


def levelOrderTraversalSpiral(tree):
    l = []
    
    print tree.getRootVal()
    l.append(tree.getLeftChild())
    l.append(tree.getRightChild())
    level = 1

    while (l):
        numProcess = 2**level 
        if (level % 2 == 1):
            # odd level, pop front, push rear
            while (numProcess > 0 and l):
                t = l.pop(0)
                if (t):
                    print t.getRootVal()
                    l.append(t.getLeftChild())
                    l.append(t.getRightChild())
                numProcess -= 1
            level += 1
        else:
            # even level, pop rear, push front
            while (numProcess > 0 and l):
                t = l.pop()
                if (t):
                    print t.getRootVal()
                    l.insert(0, t.getRightChild())
                    l.insert(0, t.getLeftChild())
                numProcess -= 1
            level += 1




t = binTree.BinaryTree(1)
t.insertLeft(2)
t.insertRight(3)
#t.getLeftChild().insertLeft(7)
t.getLeftChild().insertRight(6)
t.getRightChild().insertLeft(5)
#t.getRightChild().insertRight(4)

levelOrderTraversalSpiral(t)
