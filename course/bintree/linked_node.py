class LinkedNode:
    """
    结点链接法实现的二叉树，树和树节点使用同一个类
    """
    def __init__(self, rootObj, \
            left=None, right=None):
        self.key = rootObj
        self.leftChild = left
        self.rightChild = right

    def insertLeft(self, newNode):
        self.leftChild = LinkedNode(newNode, \
                left=self.leftChild)

    def insertRight(self, newNode):
        self.rightChild = LinkedNode(newNode, \
                right = self.rightChild)

    def getRightChild(self):
        return self.rightChild;

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def _print(self, is_left, offset, depth, buf, label):
        b = "{:^5}".format(label(self))
        width = 5
        while len(buf)<2*depth+1:                #让后面的buf[2*depth]访问有效
            buf.append([])
        left  = self.leftChild._print(True, offset,                depth + 1, buf, label) if self.leftChild else 0;
        right = self.rightChild._print(False, offset + left + width, depth + 1, buf, label) if self.rightChild else 0;

        enlarge = offset+left+width+right-len(buf[2*depth])
        buf[2*depth].extend([' ']*enlarge)
        for i, c in enumerate(b):               #输出子树根节点的内容
            buf[2*depth][offset+left+i] = c


        if depth > 0:                          #输出子树与其父节点的连线
            if is_left:
                enlarge = offset+left+2*width+right-len(buf[2*depth-1])
                buf[2*depth-1].extend([' ']*enlarge)
                for i in range(width+right):
                    buf[2 * depth - 1][offset + left + width//2 + i] = '-'
                buf[2 * depth - 1][offset + left + width//2] = '+';
                buf[2 * depth - 1][offset + left + width//2 + right + width] = '+';
            else:
                enlarge = offset+left+width+right-len(buf[2*depth-1])
                buf[2*depth-1].extend([' ']*enlarge)
                for i in range(left+width):
                    buf[2 * depth - 1][offset - width//2 + i] = '-';
                buf[2 * depth - 1][offset + left + width//2] = '+';
                buf[2 * depth - 1][offset - width//2 - 1] = '+';
        return left + width + right;

    def print(self, label=lambda x:x.key):
        """
        在命令行下打印树。
        树结构需要采用节点链接法来实现。
        用label来选择用来代表节点的内容。
        """
        buf = []
        self._print(True, 0, 0, buf, label)
        for l in buf:
            print(''.join(l))

if __name__=="__main__" :
    BinaryTree = LinkedNode
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getRightChild().setRootVal('hello')
    r.getLeftChild().insertRight('d')
    r.print()
