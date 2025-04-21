import graph
import queue

def dijkstra(aGraph, start):
    pq = queue.PriorityQueue()

    start.setDistance(0)                   #起始点的dist为0
    #对所有顶点建堆，形成优先队列
    for v in g:
        pq.add_task(v, v.getDistance())
    while not pq.isEmpty():
        try :
            curr = pq.pop_task()    #优先队列出队
        except KeyError:
            break
        for nbr in curr.getConnections():
            newDist = curr.getDistance() \
                    + curr.getWeight(nbr)
            if newDist < nbr.getDistance():
                #更新邻居结点
                nbr.setDistance(newDist)
                nbr.setPred(curr)
                pq.add_task(nbr, newDist)

if __name__ == "__main__":
    def addEdge(g, u, v, weight):
        g.addEdge(u, v, weight)
        g.addEdge(v, u, weight)

    g = graph.Graph(graph.Vertex)
    addEdge(g, 'u', 'v', 2)
    addEdge(g, 'w', 'v', 3)
    addEdge(g, 'u', 'w', 5)
    addEdge(g, 'u', 'x', 1)
    addEdge(g, 'x', 'v', 2)
    addEdge(g, 'x', 'w', 3)
    addEdge(g, 'y', 'w', 1)
    addEdge(g, 'y', 'x', 1)
    addEdge(g, 'y', 'z', 1)
    addEdge(g, 'w', 'z', 5)

    dijkstra(g, g.getVertex('u'))
    for v in g:
        print(f'{v.id} : {v.distance}')
