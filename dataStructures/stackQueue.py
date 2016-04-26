import stack

class StackQueue:

    def __init__(self):
        self.enqueueStack = stack.Stack()
        self.dequeueStack = stack.Stack()

    def enqueue(self, item):
        self.enqueueStack.push(item)

    def dequeue(self):
        if (self.dequeueStack.isEmpty()):
            while (not self.enqueueStack.isEmpty()):
                self.dequeueStack.push(self.enqueueStack.pop())
        return self.dequeueStack.pop()

    def isEmpty(self):
        return self.dequeueStack.isEmpty() and self.enqueueStack.isEmpty()

    def size(self):
        return self.dequeueStack.size() + self.enqueueStack.size()


class StackQueue2:

    def __init__(self):
        self.mainStack = stack.Stack()
        self.storageStack = stack.Stack()

    def enqueue(self, item):
        while (not self.mainStack.isEmpty()):
            self.storageStack.push(self.mainStack.pop())
        self.mainStack.push(item)
        while(not self.storageStack.isEmpty()):
            self.mainStack.push(self.storageStack.pop())

    def dequeue(self):
        return self.mainStack.pop()

    def isEmpty(self):
        return self.mainStack.isEmpty()

    def size(self):
        return self.mainStack.size()



q = StackQueue2()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print q.dequeue()
print q.dequeue()

q.enqueue(5)
q.enqueue(9)
q.enqueue(89)
while (not q.isEmpty()):
    print q.dequeue()
