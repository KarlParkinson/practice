class Subset:

    def __init__(self, element):
        self.parent = None
        self.element = element


class UnionFind:

    def __init__(self):
        self.subsets = {}

    def makeset(self, item):
        if item in self.subsets:
            return
        else:
            subset = Subset(item)
            self.subsets[item] = subset
    
    def find(self, item):
        if item in self.subsets:
            representative = self.subsets[item]
            parent = representative.parent
            while (parent != None):
                representative = parent
                parent = representative.parent
            return representative
        else:
            return False

    def union(self, x, y):
        self.subsets[y].parent = self.subsets[x]



uf = UnionFind()
uf.makeset(1)
uf.makeset(2)
uf.makeset(3)
uf.makeset(4)
uf.makeset(5)

print uf.find(5)
uf.union(4,5)
uf.union(5,3)
print uf.find(3)
print uf.find(4)
print uf.find(5)
        
        
