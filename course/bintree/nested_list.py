def BinaryTree(r, left=[], right=[]):
    """
    嵌套列表法实现的二叉树
    """
    return [r, left, right]

def insertLeft(root, newBranch):
    root[1] = BinaryTree(newBranch, \
            left=getLeftChild(root))
    return root

def insertRight(root, newBranch):
    root[2] = BinaryTree(newBranch, \
            right=getRightChild(root))
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__=="__main__" :
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    l = getLeftChild(r)
    print(l)

    setRootVal(l, 9)
    print(r)
    insertLeft(l, 11)
    print(r)
    print(getRightChild(getRightChild(r)))
