from graph import Graph, Vertex
class DFSGraph(Graph):
    def __init__(self, other = None):
        super().__init__(Vertex, other)
        self.time = 0                # 不是物理时间，而是算法执行步数

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')   # 颜色初始化
            aVertex.setPred(None)
        for aVertex in self:           # 从每一个顶点开始遍历
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex) # 建立一个以aVertex为根的树
                                       # 如果有多棵树，则形成森林
    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1                 # 记录算法的步数
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)   #深度优先递归访问
            elif nextVertex.getColor() == 'gray':
                raise ValueError("Ring detected")

        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


def main():
    g = DFSGraph()
    #把做煎饼的步骤导入到图中
    g.addEdge("milk", "mix")
    g.addEdge("egg", "mix")
    g.addEdge("oil", "mix")
    g.addEdge("mix", "syrup")
    g.addEdge("mix", "pour")
    g.addEdge("griddle", "pour")
    g.addEdge("pour", "turn")
    g.addEdge("turn", "eat")
    g.addEdge("syrup", "eat")
    #g.addEdge("eat", "milk")

    print(g)
    print(g.T())

    g.dfs()
    vertices = [vert for vert in g]
    vertices.sort(key=lambda x:x.finish, \
            reverse=True)
    for vert in vertices:
        print(vert.getId())

if __name__ == "__main__":
    main()
