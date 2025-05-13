from binarySearchTree import TreeNode, BinarySearchTree
class AVLTreeNode(TreeNode):
    def __init__(self, key, val, parent=None):
        super().__init__(key, val, parent=parent)
        self.height = 1

    def renew_height(self):
        l = self.leftChild.height if self.leftChild else 0
        r = self.rightChild.height if self.rightChild else 0
        self.height = 1 + max(l, r)

    def balance(self):
        l = self.leftChild.height if self.leftChild else 0
        r = self.rightChild.height if self.rightChild else 0
        return l - r


class AVL(BinarySearchTree):
    TreeNode = AVLTreeNode

    def checkBalance(self, curr):
        """
        检查curr结点的平衡因子，并负责再平衡。
        返回平衡之后新子树的根结点，由caller维护父结点对他的指向
        """
        bal = curr.balance()
        if bal > 1: #L+
            if curr.leftChild and curr.leftChild.balance() == -1 : #L+R
                curr.leftChild = self.rotateLeft(curr.leftChild)
            curr = self.rotateRight(curr)
        elif bal < -1: #R+
            if curr.rightChild and curr.rightChild.balance() == 1: #R+L
                curr.rightChild = self.rotateRight(curr.rightChild)
            curr = self.rotateLeft(curr)
        else:      #没有发生旋转，子树的高度也需要重算
            curr.renew_height()
        return curr

    def _put(self, key, val, curr):
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
        return self.checkBalance(curr)

    def delete(self, key):
        nodeToRemove = self._get(key, self.root)
        if nodeToRemove:
            curr = self.remove(nodeToRemove) #得到remove结点的父结点
            self.size -= 1
            while curr : 
                if curr.isLeftChild():
                    curr = self.checkBalance(curr)
                    curr.parent.leftChild = curr
                elif curr.isRightChild():
                    curr = self.checkBalance(curr)
                    curr.parent.rightChild = curr
                else:                  #isRoot
                    curr = self.checkBalance(curr)
                    self.root = curr
                curr = curr.parent
        else:
            raise KeyError("'{}' notFound.".format(key))

    def rotateLeft(self, rotRoot):
        o, n = rotRoot, rotRoot.rightChild     #旧的和新的根结点
        tr   = n.leftChild                     #移植新根结点的左子结点

        n.parent = o.parent                    #新根上连
        n.leftChild, o.parent = o, n           #重建新旧根之间的联系
        o.rightChild = tr                      #-->到旧根的右子结点
        if tr : tr.parent = o
        
        #新/旧根的高度需要重算
        o.renew_height()
        n.renew_height()
        #返回新根结点
        return n;

    def rotateRight(self, rotRoot):
        o, n = rotRoot, rotRoot.leftChild      #旧的和新的根结点
        tr   = n.rightChild                    #移植新根结点的右子结点

        n.parent = o.parent                    #新根上连
        n.rightChild, o.parent = o, n          #重建新旧根之间的联系
        o.leftChild = tr                       #-->到旧根的左子结点
        if tr : tr.parent = o
        
        #新/旧根的高度需要重算
        o.renew_height()
        n.renew_height()
        #返回新根结点
        return n;

    def display(self):
        if self.root:
            self.root.print(label=lambda x:"{}:{}".format(x.key, x.balance()))
        else:
            print("[]")

if __name__ == "__main__":
    tree = AVL()

    tree.put(1)
    tree.display()
    tree.put(2)
    tree.put(30)
    tree.put(40)
    tree.display()
    tree.put(50)
    tree.display()
    tree.put(60)
    tree.put(70)
    tree.put(80)
    tree.put(0)
    tree.put(25)
    tree.put(35)
    tree.put(21)
    tree.display()
    #调用的是BinarySearchTree的删除方法，会破坏树的平衡。
    del tree[40]
    tree.display()
