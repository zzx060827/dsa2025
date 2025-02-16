class HashTable:
    def __init__(self, size=11):
        self.size = size 
        self.slots =  [None] * self.size
        self.data = [None] * self.size
