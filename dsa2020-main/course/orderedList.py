from unOrderedList import UnorderedList

class OrderedList(UnorderedList):
    def search(self, item):
        current = self.head
        
        while current != None:
            if current.getData() == item:
                return True
            elif current.getData() > item:
                return False
            current = current.getNext()

        return False

    def add(self, item):
        current = self.head
        previous = None
        
        while current != None:
            if current.getData() > item:
                #发现了插入位置，在current之前
                break
            previous = current
            current = current.getNext()

        temp = Node(item)
        if previous == None:
            #插在表头
            temp.setNext(self.head)
            self.head = temp
        else:
            #插在表中
            temp.setNext(current)
            previous.setNext(temp)
