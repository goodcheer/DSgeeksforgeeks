from delete_node import Node
from delete_node import LinkedList as LL

class LinkedList(LL):
    def __init__(self):
        self.head = None
    
    def rotate(self, k):
        if k == 0:
            return
        
        current = self.head

        # find kth node
        count = 1
        while count < k and current is not None:
            current = current.next
            count += 1
        if current is None:
            return
        kth_node = current

        # find last node
        while current.next is not None:
            current = current.next
        
        current.next = self.head
        self.head = kth_node.next
        kth_node.next = None

if __name__ == '__main__':
    llist = LinkedList() 
  
    # Create a list 10->20->30->40->50->60 
    for i in range(60, 0, -10): 
        llist.push(i)
    
    print("Given linked list")
    llist.print_list() 
    llist.rotate(4) 
    
    print("Rotated Linked list")
    llist.print_list() 