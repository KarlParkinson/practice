class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.nextNode = node

class DoublyLinkedNode(Node):

    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.previousNode = None

    def getPrevious(self):
        return self.previousNode

    def setPrevious(self, node):
        self.previousNode = node


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = DoublyLinkedNode(item)
        if (self.head != None):
#            print "here"
            self.head.setPrevious(temp)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        found = False
        current = self.head
        
        while (current != None and not found):
            if (current.getData() == item):
                found = True
            else:
                current = current.getNext()

        if (current.previous == None):
            # deleting first item from list
            self.head = current.getNext()
            if (self.head != None):
                self.head.previous = None
        elif (current == None):
            # item not found, return false
            return False
        else:
            previous = current.getPrevious()
            following = current.getNext()
            previous.setNext(following)
            if (following != None):
                following.setPrevious(previous)

    def search(self, item):
        current = self.head
        found = False

        while (current != None and not found):
            if (current.getData() == item):
                found = True
            else:
                current = current.getNext()

        return found

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0

        while (current != None):
            count += 1
            current = current.getNext()

        return count

    def append(self, item):
        current = self.head
        previous = None

        while (current != None):
            previous = current
            current = current.getNext()

        if (previous == None):
            # appending to empty list
            self.add(item)
        else:
            temp = DoublyLinkedNode(item)
            previous.setNext(temp)
            temp.setPrevious(previous)

    def index(self, item):
        current = self.head
        pos = 0
        found = False

        while (current != None and not found):
            if (current.getData() == item):
                found = True
            else:
                pos += 1
                current= current.getNext()

        if (found):
            return pos
        else:
            return False

    def insert(self, pos, item):
        current = self.head
        currentPos = 0

        while (current != None and currentPos != pos):
            current = current.getNext()
            currentPos += 1

        if (current == None):
            return False

        previous = current.getPrevious()
        temp = DoublyLinkedNode(item)
        previous.setNext(temp)
        temp.setNext(current)
        temp.setPrevious(previous)
        current.setPrevious(temp)

    def pop(self, pos=None):
        if (pos == None):
            pos = self.length()-1

        current = self.head
        currentPos = 0

        while (current != None and currentPos != pos):
            current = current.getNext()
            currentPos += 1

        if (current == None):
            # ran off end of list, position not in list
            return False

        # found position
        previous = current.getPrevious()
        if (previous == None):
            # popping first item from list
            self.head = current.getNext()
            if (self.head != None):
                self.head.setPrevious(None)
        else:
            following = current.getNext()
            previous.setNext(following)
            if (following != None):
                following.setPrevious(previous)
        return current.getData()
    


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def traverse(self):
        current = self.head
        while (current):
            print "->" + str(current.getData()),
            current = current.getNext()

    def remove(self, item):
        found = False
        current = self.head
        previous = None

        while (current != None and not found):
            if (current.getData() == item):
                found = False
            else:
                previous = current
                current = current.getNext()

        if (previous == None):
            # must delete first item
            self.head = current.getNext()
        elif (current == None):
            return False
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        found = False
        current = self.head

        while (current != None and not found):
            if (current.getData() == item):
                found = True
            else:
                current = current.getNext()

        if (found):
            return True
        else:
            return False

    def isEmpty(self):
        return self.head == None

    def length(self):
        current = self.head
        count = 0

        while (current != None):
            count += 1
            current = current.getNext()

        return count

    def append(self, item):
        if (self.isEmpty()):
            self.add(item)
            return

        current = self.head
        previous = None
        
        while (current != None):
            previous = current
            current = current.getNext()

        temp = Node(item)
        previous.setNext(temp)

    def index(self, item):
        current = self.head
        pos = 0
        found = False

        while (current != None and not found):
            if (current.getData() == item):
                found = True
            else:
                pos += 1
                current = current.getNext()

        if (found):
            return pos
        else:
            return False

    def insert(self, pos, item):
        if (pos == 0):
            self.add(item)

        current = self.head
        previous = None
        currentPos = 0

        while (currentPos != pos):
            currentPos += 1
            previous = current
            current = current.getNext()
            
        temp = Node(item)
        previous.setNext(temp)
        temp.setNext(current)
        
    def pop(self, pos=None):
        if (pos == None):
            pos = self.length() - 1

        current = self.head
        previous = None
        currentPos = 0

        while (currentPos != pos):
            previous = current
            current = current.getNext()
            currentPos += 1

        if (previous == None):
            # popping first element from list
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return current.getData()
        




def swap(LL, x, y):
    xNode = None
    yNode = None
    prevx = None
    prevy = None
    xafter = None
    yafter = None

    foundx = False
    foundy = False
    current = LL.head
    previous = None

    while (not foundx or not foundy):
        if (current.getData() == x):
            foundx = True
            xNode = current
            prevx = previous
            xafter = current.getNext()
        if (current.getData() == y):
            foundy = True
            yNode = current
            prevy = previous
            yafter = current.getNext()
        previous = current
        current = current.getNext()

    if (prevy == xNode):
        # nodes adjacent
        prevx.setNext(yNode)
        xNode.setNext(yafter)
        yNode.setNext(xNode)
    elif (prevx == yNode):
        # nodes adjacent
        prevy.setNext(xNode)
        yNode.setNext(xafter)
        xNode.setNext(yNode)
    elif (prevx == None):
        # x is head node
        xNode.setNext(yafter)
        yNode.setNext(xafter)
        prevy.setNext(xNode)
        LL.head = yNode
    elif (prevy == None):
        # y is head node
        xNode.setNext(yafter)
        yNode.setNext(xafter)
        prevx.setNext(yNode)
        LL.head = xNode
    else:
        prevx.setNext(yNode)
        xNode.setNext(yafter)
        yNode.setNext(xafter)
        prevy.setNext(xNode)

def printReverse(LL):
    if (LL == None):
        return
    printReverse(LL.getNext())
    print LL.getData()

def deleteDupsSorted(LL):
    current = LL.head.getNext()
    previous = LL.head
    while (current != None):
        if (previous.getData() == current.getData()):
            # delete current
            previous.setNext(current.getNext())
            current.setNext(None)
            current = previous.getNext()
        else:
            previous = current
            current = current.getNext()
    
    
        


l = SinglyLinkedList()
l.add(11)
#l.add(11)
#l.add(11)
#l.append(21)
#l.append(43)
#l.append(43)
#l.append(60)
l.traverse()
print ""
deleteDupsSorted(l)
l.traverse()

