class Graph:

    def __init__(self):
        self.order = 0
        self.vertList = {}

    def addVertex(self, vertKey):
        self.order += 1
        vertex = Vertex(vertKey)
        self.vertList[vertKey] = vertex

    def addEdge(self, srcKey, dstKey):
        src = self.vertList[srcKey]
        dst = self.vertList[dstKey]
        if (not src.hasNeighbour(dst)):
            src.addNeighbour(dst)
            dst.addNeighbour(src) # remove to make a digraph

    def getVertex(self, vertKey):
        if (vertKey in self.vertList):
            return self.vertList[vertKey]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()

    def __contains__(self, key):
        return key in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def printGraph(self):
        for key in self.vertList:
            print(self.vertList[key])


class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbours = {}
        self.visited = False

    def addNeighbour(self, nbr, weight=0):
        self.neighbours[nbr] = weight

    def getNeighbours(self):
        return self.neighbours

    def hasNeighbour(self, vert):
        return vert in self.neighbours.keys()

    def __str__(self):
        edges = ""
        for nbr in self.neighbours:
            edges += "(" + str(self.key) + "," + str(nbr.key) + ") "
        return edges



def isWord(string, dic):
    return string in dic

def boggleToGraph(boggle):
    g = Graph()
    for row in boggle:
        for letter in row:
            g.addVertex(letter)
    n = len(boggle)
    for i in range(n):
        for j in range(n):
            if (j+1 < n): g.addEdge(boggle[i][j], boggle[i][j+1])
            if (j-1 >= 0): g.addEdge(boggle[i][j], boggle[i][j-1])
            if (i+1 < n): g.addEdge(boggle[i][j], boggle[i+1][j])
            if (i-1 >= 0): g.addEdge(boggle[i][j], boggle[i-1][j])
            if (i-1 >= 0 and j-1 >= 0): g.addEdge(boggle[i][j], boggle[i-1][j-1])
            if (i-1 >= 0 and j+1 < n): g.addEdge(boggle[i][j], boggle[i-1][j+1])
            if (i+1 < n and j-1 >= 0): g.addEdge(boggle[i][j], boggle[i+1][j-1])
            if (i+1 < n and j+1 < n): g.addEdge(boggle[i][j], boggle[i+1][j+1])

    return g


def boggleWords(boggle, dic):
    g = boggleToGraph(boggle)
    for v in g:
        for j in g:
            j.visited = False
        findWords(v, dic, "")

def findWords(start, dic, path):
    newWord = path + start.key
#    print newWord
    if (isWord(newWord, dic)):
        print newWord
    start.visited = True
    for vert in start.getNeighbours():
        if (not vert.visited):
            findWords(vert, dic, newWord)

    start.visited = False

dic = ["geaks", "for", "quiz", "go"]
boggle = [["g", "i", "z"],["u", "e", "k"],["q", "s", "a"]]
boggleWords(boggle, dic)
