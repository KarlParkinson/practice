class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0


#q = Queue()
#q.enqueue(1)
#q.enqueue("k")
#print(q.dequeue())
#print(q.dequeue())
