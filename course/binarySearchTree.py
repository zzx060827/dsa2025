from bintree.linked_node import LinkedNode
class TreeNode(LinkedNode):
    def __init__(self, key, val, left=None,
                right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent     #增加了对parent的指回，在findSuccessor中需要

    def hasLeftChild(self):              #这个函数实际没必要，只是为了代码的讲解更加口语化。
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild is self

    def isRightChild(self):
        return self.parent and self.parent.rightChild is self

    def isRoot(self):
        return self.parent is None

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def isLeaf(self):
        return not self.hasAnyChildren()

    def flat(self):
        flat = lambda x: flat(x.leftChild)+[x.key]+flat(x.rightChild) if x else []
        return flat(self)

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():           #让左右子节点指回父节点
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        if self.hasRightChild():   #在remove()中的唯一可能
            return self.rightChild.findMin()
        elif self.isRoot():
            return None
        elif self.isLeftChild():   #是左子树且无右子女
            return self.parent
        else : #是右子树且无右子女，处在parent子树中的末位
            self.parent.rightChild = None #暂时移除自己
            succ = self.parent.findSuccessor()
            self.parent.rightChild = self #恢复自己
            return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():     #往左下角
            current = current.leftChild
        return current

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:              #函数太多了，增加了“树”类来管理与之有关的部分
    TreeNode = TreeNode
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):               #供len(bst)调用
        return self.size
    def __iter__(self):
        return self.root.__iter__()

    def display(self):
        if self.root:
            self.root.print()
        else:
            print("[]")

    def put(self,key,val=0):
        #调用递归形式的_put
        self.root = self._put(key, val, self.root)

    def _put(self, key, val, curr):
        """
        按照二叉搜索树的规则，采用递归的方式在子树中插入新结点。
        返回子树的根
        """
        if curr is None:
            self.size += 1
            return self.TreeNode(key, val)
        if key < curr.key:           #递归左子树
            curr.leftChild = self._put(key, val, curr.leftChild)
            curr.leftChild.parent = curr
        elif key > curr.key:         #递归右子树
            curr.rightChild = self._put(key, val, curr.rightChild)
            curr.rightChild.parent = curr
        else: #key == curr.key
            curr.payload = val       #更新结点，无新增
        return curr

    def __setitem__(self, k, v):
        self.put(k,v)

    def get(self, key):
        if res := self._get(key, self.root):
            return res.payload
        else:
            return None

    def _get(self, key, curr):
        """
        返回匹配key的结点
        """
        if not curr:
            return None
        elif curr.key == key:
            return curr
        elif curr.key > key:
            return self._get(key, curr.leftChild)
        else: #curr.key < key
            return self._get(key, curr.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        nodeToRemove = self._get(key, self.root)
        if nodeToRemove:
            self.remove(nodeToRemove)
            self.size -= 1
        else:
            raise KeyError("'{}' notFound.".format(key))

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, curr):
        """
        返回实际remove结点的直接父结点。
        """
        if curr.isLeaf():   #作为叶节点的最简单情况
            #移除叶节点只需要在它的父节点中把它移除
            p = curr.parent
            if curr.isLeftChild():
                p.leftChild = None
            elif curr.isRightChild():
                p.rightChild = None
            else:                     #删除唯一结点
                self.root = None
            return p
        elif curr.hasBothChildren():    #有左右两个子节点的复杂情况
            succ = curr.findSuccessor() #前驱、后继肯定都有
            curr.key = succ.key
            curr.payload = succ.payload
            return self.remove(succ)    #succ没有左子节点，为什么？
                                        #不会出现第二层递归
        else:                           #只有一个子节点的情况
            # 取得唯一子节点，不关心左右
            child = curr.leftChild \
                    if curr.hasLeftChild() \
                    else curr.rightChild  #可以砍掉一半的源代码
            p = child.parent = curr.parent
            if curr.isLeftChild():   #在子、父结点之间跳过当前节点
                p.leftChild = child
            elif curr.isRightChild():
                p.rightChild = child
            else :             #当前节点是根节点，直接替换成子节点
                self.root = child
            return p

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(70)
    bst.put(31)
    bst.put(93)
    bst.put(94)
    bst.put(14)
    bst.put(23)
    bst.put(73)
    print(bst.root.flat())
    print([x for x in bst])
    bst.display()
    bst.delete(70)
    bst.display()
    bst.delete(31)
    bst.display()
    bst.delete(93)
    bst.display()
    bst.delete(94)
    bst.display()
    bst.delete(14)
    bst.display()
    bst.delete(73)
    bst.display()
    bst.delete(23)
    bst.display()
