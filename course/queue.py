import binHeap
import itertools

class Queue_on_list:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item) #0为队尾
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class PriorityQueue:
    REMOVED = '<removed-task>'    # placeholder for a removed task
    def __init__(self):
        self.entry_finder = {}    # mapping of tasks to entries
        self.counter = itertools.count()   # unique sequence count
        self.heap = binHeap.BinaryHeap()

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        entry = [priority, next(self.counter), task]
        self.entry_finder[task] = entry
        self.heap.insert(entry)

    def isEmpty(self):
        while not self.heap.isEmpty():
            priority, count, task = self.heap.findMin()
            if task is not self.REMOVED:
                return False
            else:
                self.heap.delMin()

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while not self.heap.isEmpty():
            priority, count, task = self.heap.delMin()
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
