from graph import Graph, Vertex
from binHeap import BinaryHeap
import itertools

def dijkstra(aGraph, start):
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count

    def add_task(task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in entry_finder:
            remove_task(task)
        entry = [priority, next(counter), task]
        entry_finder[task] = entry
        pq.insert(entry)

    def remove_task(task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task():
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while not pq.isEmpty():
            priority, count, task = pq.delMin()
            if task is not REMOVED:
                del entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    pq = BinaryHeap()

    start.setDistance(0)   #对所有顶点建堆，形成优先队列
    add_task(start, start.getDistance())
    while not pq.isEmpty():
        try :
            currentVert = pop_task()          #优先队列出队
        except KeyError:
            break
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
                   #修改出队顶点所邻顶点dist和前驱节点，
                   #                          并重排队列
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                add_task(nextVert, newDist)

if __name__ == "__main__":
    def addEdge(g, u, v, weight):
        g.addEdge(u, v, weight)
        g.addEdge(v, u, weight)

    g = Graph(Vertex)
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
