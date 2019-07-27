class Nodes:
    def __init__(self,data):
        self.data = None
        self.next = None
        return

    def hasValue(self,value):
        if self.data == value:
            return True
        else:
            return False

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def addNewItem(self.item):
        if not isinstance(item,Nodes):
            item = Nodes(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
