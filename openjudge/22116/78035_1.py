'''
用一段简单的代码，解释循环单链表的插入删除操作。
可以把代码复制到pythontutor.com上运行，得到可视化的演示
对于理解python中链表的操作很有好处
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def push_front(tail, value):
    '''
    tail是一个环形链表的尾结点，新加的元素放在链表的首位置
    返回新的tail值
    '''
    new_node = Node(value)
    if tail is None:
        tail = new_node
        tail.next = tail
    else:
        new_node.next = tail.next
        tail.next = new_node
    return tail

def makeRing(lst):
    '''
    从lst中读取元素创建一个环形链表，
    返回链表的尾指针
    '''
    tail = None
    for value in lst:
        tail = push_front(tail, value)
    return tail

def remove(tail, value):
    '''
    从环形链表中删除第一个value
    '''
    if tail is None:
        raise ValueError(f"{value} not found")
    prev, curr = tail, tail.next     #从第一个元素开始查找value
    while True:
        if curr.value == value:
            if prev is curr:         #链表中唯一元素
                tail = None
            else:
                prev.next = curr.next
                if tail is curr:
                    tail = prev
            break
        else:
            prev, curr = curr, curr.next
            if curr is tail.next:    #找了一圈都没有
                raise ValueError(f"{value} not found")
    return tail

if __name__ == "__main__":
    tail = makeRing([1, 2, 3])
    tail = remove(tail, 2)
    tail = remove(tail, 1)
    tail = remove(tail, 3)
    tail = remove(tail, 3)

