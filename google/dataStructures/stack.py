class Stack:

    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



class MinStack(Stack):

    def __init__(self):
        #super().__init__(self)
        Stack.__init__(self)
        self.minVal = None

    def getMinimum(self):
        return self.minVal

    def push(self, i):
        if (i < self.minVal or self.minVal == None):
            self.minVal = i
        self.items.append(i)

    def pop(self):
        i = self.items.pop()
        if (i == self.minVal):
            self.minVal = min(self.items)
        return i



s = MinStack()
s.push(5)
s.push(9)
s.push(3)
print(s.getMinimum()) # should be 3
s.pop()
print(s.getMinimum()) # should be 5
