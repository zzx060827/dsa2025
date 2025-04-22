class node:
    def __init__(self, dt):
        self.data = dt
    def __str__(self):
        return f"node({self.data})"

class Node(node):
    def __eq__(self, other):
        return self.data == other.data
    def __hash__(self):
        return hash(self.data)

if __name__ == "__main__":
    x = node('xzm')
    Y = Node(2)
    Z = Node(2)
    w = x

    'test class objects equal'
    print(f"Z==Y?{Z==Y}")
    print(f"w==x?{w==x}")

    print(hash(x))
    d = {x:0, Y:2}
    x.data = 1
    Y.data = 'xzm'
    for i in d:
        if i in d:
            print(i)
        else:
            raise KeyError(f'{i}:error key')
