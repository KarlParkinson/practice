import queue
import stack

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

    def printGraph(self):
        for key in self.vertList:
            print(self.vertList[key])


class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbours = {}

    def addNeighbour(self, nbr, weight=0):
        self.neighbours[nbr] = weight

    def getNeighbours(self):
        return self.neighbours

    def __str__(self):
        edges = ""
        for nbr in self.neighbours:
            edges += "(" + str(self.key) + "," + str(nbr.key) + ") "
        return edges

class DiGraph(Graph):

    def addEdge(self, srcKey, dstKey):
        src = self.vertList[srcKey]
        dst = self.vertList[dstKey]
        src.addNeighbour(dst)        


class AdjMatrixGraph:

    def __init__(self):
        self.order = 0
        self.matrix = []

    def addVertex(self):
        self.order += 1
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0]*self.order)

    def addEdge(self, src, dst):
        self.matrix[src][dst] = 1
        self.matrix[dst][src] = 1

    def printGraph(self):
        for i in range(0,len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if (self.matrix[i][j]):
                    print "(" + str(i) + "," + str(j) + ")"

        


# Breadth first search of graph using Adj list representation
# Will start at vertex with key startKey in graph
def bfs(graph, startKey):
    start = graph.getVertex(startKey)
    visited = {vert: False for vert in graph.vertList.values()}
    q = queue.Queue()
    
    q.enqueue(start)
    while (q.size() > 0):
        v = q.dequeue()
        if (not visited[v]):
            print v.key
            visited[v] = True
            nbrs = v.getNeighbours()
            for nbr in nbrs:
                q.enqueue(nbr)

#        for nbr in v.getNeighbours():
#            if (not visited[nbr]):
#                visited[nbr] = True
#                q.enqueue(nbr)



def dfs(graph, startKey):
  startVertex = graph.getVertex(startKey)
  visited = {vert: False for vert in graph.vertList.values()}
  _dfs(startVertex, visited)

def _dfs(startVertex, visited):
    visited[startVertex] = True
    for vert in startVertex.getNeighbours():
        if (not visited[vert]):
            print str(startVertex.key) + "->" + str(vert.key)
            _dfs(vert, visited)

def dfsNonRecursive(graph, startKey):
    startVertex = graph.getVertex(startKey)
    visited = {vert: False for vert in graph.vertList.values()}
    s = stack.Stack()

    s.push(startVertex)
    while (s.size() > 0):
        v = s.pop()
        if (not visited[v]):
            visited[v] = True
            print v.key
            for vert in v.getNeighbours():
                s.push(vert)

def hasCycleDirected(graph):
    for vertex in graph.vertList.values():
        visited = {vert: False for vert in graph.vertList.values()}
        if (cycleDetectDirected(vertex, visited)):
            return True
    return False

def cycleDetectDirected(startVertex, visited):
    visited[startVertex] = True
    for vertex in startVertex.getNeighbours():
        if (visited[vertex]):
            return True
        elif (cycleDetectDirected(vertex, visited)):
            return True
    return False

def hasCycleUndirected(graph):
    for vertex in graph.vertList.values():
        visited = {vert: False for vert in graph.vertList.values()}
        if (cycleDetectUndirected(vertex, visited, None)):
            return True
    return False

def cycleDetectUndirected(startVertex, visited, parent):
    visited[startVertex] = True
    for vertex in startVertex.getNeighbours():
        if (not visited[vertex]):
            if (cycleDetectUndirected(vertex, visited, startVertex)):
                return True
        elif (vertex != parent):
            return True
    return False

# prims algorithm to find MST of a graph
# 0 -> unseen
# 1 -> fringe
# 2 -> intree
def prims(graph):
    start = graph.getRandomVertex()
    pq = PriorityQueue()
    
    pq.enqueue(start, 0)
    while(not pq.isEmpty()):
        minVertex = pg.dequeue()
        minVertex.setStatus(2)
        for neighbour in minVertex.getNeighbours():
            if (neighbour.getStatus() == 0):
                # found new vertex, add to fringe, and add to pq
                neighbour.setStatus(1)
                neighbourWeight = neighbour.neighbours[minVertex]
                pq.enqueue(neighbour, neighbourWeight)
            elif (neighbour.getStatus() == 1):
                # found new potential edge to fringe vertex, check if need to update
                currentWeight = pq.get(neighbour)
                newWeight = neighbour.neighbours[minVertex]
                if (newWeight < currentWeight):
                    pq.updatePriority(neighbour, newWeight)


# dijkstra's algorithm to find all pairs shortest path from source vertex
def dijkstras(graph, start):
    pq = PriorityQueue()
    for vertex in graph.getVertices():
        vertex.distance = float("inf")
        vertex.parent = None
        pq.enqueue(vertex, vertex.distance)

    pathTree = Graph()
    start.setDistance(0)
    pq.updatePriority(start, start.distance)
    for i in range(0, graph.order()):
        foundVertex = pq.dequeue()
        pathTree.addVertex(foundVertex)
        pathTree.addEdge(foundVertex, foundVertex.parent)
        for neighbour in foundVertex.getNeighbours():
            if (neighbour not in pathTree):
                oldDistance = neighbour.distance
                newDistance = foundVertex.distance + neighbour.neighbours[foundVertex]
                if (newDistance < oldDistance):
                    neighbour.setDistance(oldDistance)
                    neighbour.setParent(foundVertex)
                    pq.updatePriority(neighbour, neighbour.distance)
    return pathTree


def walksKEdges(graph, u, v, k):
    numWalks = [[None]*(k+1) for i in xrange(len(graph))]
    for i in xrange(len(graph)):
        numWalks[i][0] = 0
    numWalks[v][0] = 1
    walksEdgesUtil(graph, u, v, k, numWalks)
    print numWalks
    return numWalks[u][k]


def walksEdgesUtil(graph, u, v, k, numWalks):
    if (numWalks[u][k] == None):
        row = graph[u]
        count = 0
        for j in xrange(len(row)):
            if (row[j] == 1):
                count += walksEdgesUtil(graph, j, v, k-1, numWalks)
        numWalks[u][k] = count
        return count
    else:
        return numWalks[u][k]
    

graph = [[0,1,1,1], [0,0,0,0], [0,0,0,1], [0,0,0,0]]
print walksKEdges(graph, 0, 3, 2)
