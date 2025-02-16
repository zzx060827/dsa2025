from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(G,start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nbr in currentVert.getConnections():
        """   原来的distance表示顶点与起始顶点的距离
          newCost = currentVert.getWeight(nbr) \  
                  + currentVert.getDistance()
        """
        #现在的distance表示顶点与当前生成树的最小距离
          newCost = currentVert.getWeight(nbr)
          if nbr in pq and newCost<nbr.getDistance():
              nbr.setPred(currentVert)
              nbr.setDistance(newCost)
              pq.decreaseKey(nbr,newCost)
