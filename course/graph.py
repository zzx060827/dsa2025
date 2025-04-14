class VertBase:
    """
    有向带权图的顶点
    当自定义类的对象用作字典的键值时，缺省使用系统hash()函数，它基于id()函数实现，
    也就是说，一个对象的哈希值在它的生命周期期间是固定的。
    """
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.inDegree = self.outDegree = 0

    def addNeighbor(self, nbr, weight=1):
        """
        添加从当前节点到nbr节点的有向边
        添加重复边会更新其权值，不影响节点的出/入度。
        """
        if nbr not in self.connectedTo:
            self.outDegree += 1
            nbr.inDegree += 1
        self.connectedTo[nbr] = weight

    def delNeighbor(self, nbr):
        """
        删除有向边
        """
        if nbr in self.connectedTo:
            self.outDegree -= 1
            nbr.inDegree -= 1
            del(self.connectedTo[nbr])

    def __str__(self):
        return f"{self.id}({self.inDegree}:{self.outDegree})-->{[x.id for x in self.connectedTo]}"

    __repr__ = __str__

    def getConnections(self):
        """
        取得所有指向的节点
        """
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        """
        取得指向某节点边的权重
        """
        return self.connectedTo[nbr]

import os

class Graph:
    """
    有向带权图，不支持重复边
    """
    def __init__(self, Vert=VertBase, other=None):
        """
        Vert: 顶点类型，需要继承基础顶点Vertex
        other: 复制other中所有的顶点和边
        """
        assert issubclass(Vert, VertBase)
        self.Vertex = Vert
        self.vertList = {}    #其实是一个字典
        if other:
            for v in other:
                self.addVertex(v.getId())
                for u in v.getConnections():
                    self.addEdge(v.getId(), u.getId(),
                            v.getWeight(u))

    def T(self):
        """
        获取有向图的转置图
        """
        ng = Graph()
        for v in self:
            ng.addVertex(v.getId())
            for u in v.getConnections():
                ng.addEdge(u.getId(), v.getId())
        return ng

    def addVertex(self, key):
        if key not in self:
            self.vertList[key] = Vertex(key)
        return self.vertList[key]

    def getVertex(self, key):
        try:
            return self.vertList[key]
        except KeyError:
            return None

    def delVertex(self, key):
        """
        删除一个顶点，先删掉它所有的入边、出边，再删本身
        """
        if key in self:
            v = self.getVertex(key)
            for f in self:
                f.delNeighbor(v)
            for t in [t for t in v.getConnections()]:
                v.delNeighbor(t)
            del(self.vertList[key])

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self:
            self.addVertex(f)
        if t not in self:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        """
        返回所有顶点的key
        """
        return self.vertList.keys()

    def __iter__(self):
        """
        返回所有顶点本身
        """
        return iter(self.vertList.values())

    def __len__(self):
        return len(self.vertList)

    def __str__(self):
        """
        每个顶点各占一行。
        """
        s = ""
        for v in self:
            nbrs = " ".join([str(u.getId()) for u in v.getConnections()])
            s += f"{v}: {nbrs}{os.linesep}"
        return s

#对VertBase进行扩充，
#增加了distance, color, pred
#和discovery, finish属性,
#从而对BFS/DFS搜索算法进行支持。
import sys
class Vertex(VertBase):
    def __init__(self, key):
        super().__init__(key)
        self.color = 'white'
        self.distance = sys.maxsize
        self.pred = None
        """
        self.pred = []
        前驱可能有多个值，用一个列表来存放。
        这样可以通过BFS算法找出所有的最短路径。
        """
        self.discovery = None
        self.finish = None

    def setDiscovery(self, t):
        self.discovery = t

    def setFinish(self, t):
        self.finish = t

    def getDistance(self):
        return self.distance

    def setDistance(self, dist):
        self.distance = dist

    def setPred(self, pred):
        self.pred = pred

    def getPred(self):
        return self.pred

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

if __name__=="__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(1,4)
    g.addEdge(1,4)
    g.addEdge(6,1)
    g.addEdge(6,4)
    for v in g:
        print(v)
