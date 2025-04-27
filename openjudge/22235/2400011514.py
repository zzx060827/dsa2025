class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    def addLeft(self, tree):
        self.left = tree
    def addRight(self, tree):
        self.right = tree
    def preorderTravel(self, op):
        op(self.data)
        if self.left:
            self.left.preorderTravel(op)
        if self.right:
            self.right.preorderTravel(op)
    def inorderTravel(self, op):
        if self.left:
            self.left.inorderTravel(op)
        op(self.data)
        if self.right:
            self.right.inorderTravel(op)
    def postorderTravel(self, op):
        if self.left:
            self.left.postorderTravel(op)
        if self.right:
            self.right.postorderTravel(op)
        op(self.data)

nodes = []
#nodes内容形如：[(0, 'A'), (1, 'B'), (2, 'E')......]
nodesPtr = 0    #表示看到nodes里的第几行

def buildTreeInBinary(level):
#要求此函数返回一个BinaryTree对象
#在此处补充你的代码
    global nodesPtr
    if nodesPtr >= len(nodes) or nodes[nodesPtr][0] != level:
        return None
    current_node = BinaryTree(nodes[nodesPtr][1])
    nodesPtr += 1
    current_node.addLeft(buildTreeInBinary(level + 1))
    current_node.addRight(buildTreeInBinary(level))
    return current_node
#在此处结束你补充的代码

while True:
    try:
        s = input().rstrip()
        nodes.append((len(s)-1, s.strip()))
    except:
        break

tree = buildTreeInBinary(0)
tree.preorderTravel(lambda x: print(x, end=""))
print()
tree.inorderTravel(lambda x: print(x, end=""))