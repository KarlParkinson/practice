class TwoStacks:

    def __init__(self):
        self.growFactor = 10
        self.length = 10
        self.items = [None] * self.length
        self.p1 = 0
        self.p2 = 1

    def push1(self, item):
        self.p1 += 2
        self.__grow()
        self.items[self.p1] = item
        
    def push2(self, item):
        self.p2 += 2
        self.__grow()
        self.items[self.p2] = item

    def pop1(self):
        item = self.items[self.p1]
        self.p1 -= 2
        return item

    def pop2(self):
        item = self.items[self.p2]
        self.p2 -= 2
        return item

    def isEmpty1(self):
        return self.p1 == 0

    def isEmpty2(self):
        return self.p2 == 1

    def size1(self):
        return self.p1 // 2

    def size2(self):
        return self.p2 // 2
        

    def __grow(self):
        if (self.p1 >= self.length or self.p2 >= self.length):
            self.items = self.items + [None] * self.growFactor
            self.length += self.growFactor



s = TwoStacks()
s.push1(1)
s.push1(2)
s.push2("a")
s.push2("b")
s.push2("c")

print s.size1()
print s.size2()

print ""
while (not s.isEmpty1()):
    print s.pop1()
while (not s.isEmpty2()):
    print s.pop2()
        
