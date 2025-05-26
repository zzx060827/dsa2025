import math
def readCoord():
    l = list(map(int, input().split()))
    return [(l[i], l[i+1]) for i in range(0, len(l), 2)]

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

class Point:
    def __init__(self, coord, minute=float("inf")):
        self.coord = coord
        self.minute = float(minute)
        self.connTo = {}

def buildGraph(home, school, subway):
    graph = {home:Point(home), school:Point(school)}
    def addEdge(a, b, v):
        if a is b:
            return
        if a not in graph:
            graph[a] = Point(a)
        if b not in graph:
            graph[b] = Point(b)
        """
        单位换算：m / (km/h) = m / (1000*m/60min) = 0.06min
        """
        minute = dist(a, b) / v * 0.06      
        if graph[a] in graph[b].connTo:
            minute = min(minute, graph[b].connTo[graph[a]])
        graph[a].connTo[graph[b]] = graph[b].connTo[graph[a]] = minute

    v0, v1 = 10, 40
    addEdge(home, school, v0)
    for line in subway:
        for i in range(len(line)-1):
            addEdge(line[i], line[i+1], v1)
        for stop in line:
            for vert in graph:
                if stop is not vert:
                    addEdge(stop, vert, v0)
    return graph

import heapq
def dijkstra(graph, home, school):
    graph[home].minute = float(0)
    pq = [(graph[home].minute, home)]
    while pq:
        minute, curr = heapq.heappop(pq)
        if curr == school:
            return
        if minute > graph[curr].minute:
            continue
        for nbr in graph[curr].connTo:
            new_minute = minute + graph[curr].connTo[nbr]
            if new_minute < nbr.minute:
                nbr.minute = new_minute
                heapq.heappush(pq, (new_minute, nbr.coord))
        
if __name__ == "__main__":
    home, school = readCoord()
    subway = []
    while True:
        try:
            subway.append(readCoord()[:-1])
        except EOFError: 
            break
    graph = buildGraph(home, school, subway)
    dijkstra(graph, home, school)
    print(round(graph[school].minute))
