class DNodes:
    def __init__(self,data):
        self.data = data
        self.next = None
        return




class linkedList1:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def addNewItem(self,item):
        if not isinstance(item,Nodes):
            item = DNodes(item)
        if self.head is None:
            self.head = item

        else:
            self.tail.next = item

        self.tail = item

        return

    def outputList(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)

            currentNode = currentNode.next

        return

def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1 

            current_node = current_node.next

        return count


class Nodes:
    def __init__(self,data):
        self.data = data
        self.next = None
        return



class linkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def addNewItem(self,item):
        if not isinstance(item,Nodes):
            item = Nodes(item)
        if self.head is None:
            self.head = item

        else:
            self.tail.next = item

        self.tail = item

        return

    def outputList(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)

            currentNode = currentNode.next

        return

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1 

            current_node = current_node.next

        return count

dnode1 = DNodes(4)
dnode2 = DNodes(9)
dnode3 = DNodes(10)
dnode4 = DNodes(24)


a = Nodes(4)
b = Nodes(5)
c = Nodes(6)
d = Nodes(7)

music = linkedList1()

for current_item in [dnode1, dnode2,dnode3,dnode4]:
    music.addNewItem(current_item)
track = linkedList2()

for current_item in [a, b, c, d]:
    track.addNewItem(current_item)

m = print(list(music.outputList()))