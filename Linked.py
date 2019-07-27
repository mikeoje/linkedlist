class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        return
    

    def hasValue(self,value):
        if self.data == value:
            return True
        else:
            return False

node1 = ListNode(15)
node2 = ListNode(8.2)
node3 = ListNode("Berlin")


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add_list_item(self,item):
        if not isinstance(item,ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        
        else:
            self.tail.next = item

        self.tail = item

        return

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count = count + 1 

            current_node = current_node.next

        return count

    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            current_node = current_node.next
        return


node1 = ListNode(15)  
node2 = ListNode(8.2)  
item3 = "Berlin"  
node4 = ListNode(15)

track = SingleLinkedList()  
print("track length: %i" % track.list_length())

for current_item in [node1, node2, item3, node4]:  
    track.add_list_item(current_item)
    print("track length: %i" % track.list_length())
    track.output_list()