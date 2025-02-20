from pythonds.graphs import Graph, Vertex
import os

class XGraph(Graph):
    def __init__(self, other = None):
        super().__init__()
        if other:
            for v in other:
                for u in v.getConnections():
                    self.addEdge(v.getId(), u.getId())

    def T(self):
        """
        获取有向图的转置图
        """
        ng = XGraph()
        for v in self:
            for u in v.getConnections():
                ng.addEdge(u.getId(), v.getId())
        return ng

    def __str__(self):
        s = ''
        for v in self:
            s = s+str(v.getId())+' :'
            for u in v.getConnections():
                s = s + ' ' + str(u.getId())
            s = s + os.linesep
        return s

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = XVertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def delVertex(self, key):
        self.numVertices -= 1
        if key in self.vertices:
            v = self.vertices[key]
            del(self.vertices[key])
            for vert in self:
                vert.delNeighbor(v)

    def addEdge(self,f,t,cost=0):
            if f not in self.vertices:
                nv = self.addVertex(f)
            if t not in self.vertices:
                nv = self.addVertex(t)
            self.vertices[f].addNeighbor(self.vertices[t],cost)
    

class XVertex(Vertex):
    def __init__(self, num):
        super().__init__(num)
        self.inDegree = self.outDegree = 0

    def addNeighbor(self,nbr,weight=0):
        if nbr not in self.connectedTo:
            self.outDegree += 1
            nbr.inDegree += 1
        self.connectedTo[nbr] = weight

    def delNeighbor(self, nbr):
        if nbr in self.connectedTo:
            self.outDegree -= 1
            nbr.inDegree -= 1
            del(self.connectedTo[nbr])
