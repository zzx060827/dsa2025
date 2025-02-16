from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        
        while current != None:
            if current.getData() == item:
                return True
            current = current.getNext()

        return False

    def remove(self, item):
        current = self.head
        previous = None
        
        while current != None:
            if current.getData() == item:
                break
            previous = current
            current = current.getNext()
        else:
            return

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

if __name__ == "__main__":
    mylist = UnorderedList()
    print(mylist.head)
    mylist.add(12)
    print(mylist.size())
    print(mylist.search(12))
    print(mylist.search(11))
    mylist.remove(11)
    print(mylist.size())
    mylist.remove(12)
    print(mylist.size())
