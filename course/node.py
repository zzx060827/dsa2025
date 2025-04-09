class Node:
    """
    最简单的单链表结点
    属性data和next直接访问
    """
    def __init__(self, dt=None, nxt=None):
        self.data = dt
        self.next = nxt

if __name__ == "__main__":
    header = None
    for i in range(5):
        header = Node(i, header)
    while header is not None:
        print(header.data)
        header = header.next

