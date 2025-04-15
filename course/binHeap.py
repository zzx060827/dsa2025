class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        pass

    def insert(self, k):
        self.heaplist.append(k)
        self.percUp(self.size())

    def findMin(self):
        return self.heaplist[1]

    def delMin(self):
        m = self.heaplist[1]
        t = self.heaplist.pop()
        if self.size() >= 1:
            self.heaplist[1] = t
            self.percDown(1)
        return m

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.heaplist)-1

    def buildHeap(self, l):
        self.heaplist = [0] + l
        for i in range(self.size() // 2, 0, -1):
            self.percDown(i)

    def percUp(self, i):
        while i // 2 > 0 and self.heaplist[i] < self.heaplist[i//2] :
            self.heaplist[i], self.heaplist[i//2] = self.heaplist[i//2], self.heaplist[i]
            i //= 2

    def percDown(self, i):
        mc = self.minChild(i)
        while mc and self.at(mc) < self.at(i):
            self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i, mc = mc, self.minChild(mc)

    def minChild(self, i):
        return None if self.at(2*i) == None \
                else 2*i if self.at(2*i+1) == None \
                else 2*i+1 if self.at(2*i+1) < self.at(2*i) \
                else 2*i

    def at(self, i):
        return self.heaplist[i] if i<=self.size() else None

if __name__ == "__main__":
    bh = BinaryHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())

    print('*********')
    bh.buildHeap([3, 3, 5, 9, 1, 11])
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
