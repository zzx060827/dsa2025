from bintree.linked_node import LinkedNode

BinaryTree = LinkedNode

def buildParseTree(fpexp):                 #full parentheses
    """
    把全括号形式的表达式转成二叉树结构
    """
    fplist = fpexp.split()                 #分解单词：输入表达式中单词需用空格分开
    pStack = []                            #python list是多面手，可以把它当栈用。
    currentTree = eTree = BinaryTree('')   #创建一棵树空树
    #pStack.append(currentTree)             #这是在干什么？？？？
    for i in fplist[:-1]:                   #最外面的闭括号其实是没用的，丢掉。
                                            #或者在前面把根多压一次栈。
        if i=="(":                         #子表达式开始
            currentTree.insertLeft('')
            pStack.append(currentTree)     #入栈左下降
            currentTree = currentTree.getLeftChild()
        elif i in ['+', '-', '*', '/']:    #操作符
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.append(currentTree)     #入栈右下降
            currentTree = currentTree.getRightChild()
        elif i == ')':                     #子表达式结束
            currentTree = pStack.pop()
        elif ord('0')<= ord(i)<= ord('9'): #操作数
            currentTree.setRootVal(int(i))
            currentTree = pStack.pop()     #出栈上升
        else:
            raise ValueError
    return eTree

import operator
def evaluate(parseTree):                   #递归法实现
    opers = {'+':operator.add, '-':operator.sub,
            '*':operator.mul, '/':operator.truediv}
    leftC = parseTree.getLeftChild()       #取子树，缩小规模
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC)          #递归调用
                  , evaluate(rightC))
    else:
        return parseTree.getRootVal()      #基本结束条件


if __name__ == "__main__":
    # expr = input("Please input:")
    tree = buildParseTree("( 5 + ( 9 * 2 ) )")
    tree.print()
    print(evaluate(tree))
    # help(tree.print)
