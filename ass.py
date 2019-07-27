def mergeLists(head1, head2):
    current1=head1
    current2=head2
    newList=SinglyLinkedList()
    while current1 or current2:
        if not current1:
            newList.insert_node(current2.data)
            current2=current2.next
            continue
        if not current2:
            newList.insert_node(current1.data)
            current1=current1.next
            continue

        if current1.data<current2.data:
            newList.insert_node(current1.data)
            current1=current1.next
        else:
            newList.insert_node(current2.data)
            current2=current2.next
    return newList.head




    



if __name__ == '__main__':
    class SinglyLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
            return

        def insert_node(self,item):
            # if not isinstance(item,ListNode):
            #     item = ListNode(item)

            if self.head is None:
                self.head = item
            
            else:
                self.tail = item

            # self.tail = item

            return
    
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)
        print(llist3)

    #     print_singly_linked_list(llist3, ' ', fptr)
    #     fptr.write('\n')

    # fptr.close()






