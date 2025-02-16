class TreeNode:
    def __init__(self, key, val, left=None, \
            right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = self.connectChild(left)
        self.rightChild = self.connectChild(right)
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def connectChild(self, child):
        if child:
            child.parent = self
        return child

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and \
                self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and \
                self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.hasAnyChildren()

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = val
        self.leftChild = self.connectChild(lc)
        self.rightChild = self.connectChild(rc)

    def findSuccessor(self):
        if self.hasRightChild():
            return self.rightChild.findMin()
        else: # not hasRightChild()
            #在BinarySearchTree::remove()中hasBothChildren()条件下到不了这里
            if self.parent:
                if self.isLeftChild():
                    return self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
                    return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        """
        splice: 捻接
        """
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            elif self.isRightChild():
                self.parent.rightChild = None
        elif self.hasLeftChild():

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    __len__ = length

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root :
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = \
                        TreeNode(key, val, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = \
                        TreeNode(key, val, parent=currentNode)
        else: # key == currentNode.key
            currentNode.payload = val

    def __setitem__(self, k, v):
        self.put(k, v)
   
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            return self._get(key, currentNode.rightChild)
        else: # key == currentNode.key
            return currentNode

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError("Error, key not in tree")

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            elif currentNode.isRightChild():
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # currentNode has Just 1 child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = \
                            currentNode.parent.connectChild(currentNode.leftChild)
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = \
                            currentNode.parent.connectChild(currentNode.leftChild)
                else: #currentNode is root
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                            currentNode.leftChild.payload,
                            currentNode.leftChild.leftChild,
                            currentNode.leftChild.rightChild)
            else : #currentNode.hasRightChild()
                if currentNode.isLeftChild():
                    currentNode.parent.leftChild = \
                            currentNode.parent.connectChild(currentNode.rightChild)
                elif currentNode.isRightChild():
                    currentNode.parent.rightChild = \
                            currentNode.parent.connectChild(currentNode.rightChild)
                else: #currentNode is root
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                            currentNode.rightChild.payload,
                            currentNode.rightChild.leftChild,
                            currentNode.rightChild.rightChild)


