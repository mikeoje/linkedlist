def findMergeNode(head1, head2): 
      curA,curB = head1, head2           
      while curA != curB: 
              if curA.next is None:      
                    curA = head2 
              else: curA=curA.next 
             if curB.next is None:
                   curB = head1 
             else: curB = curB.next
     return curA.data