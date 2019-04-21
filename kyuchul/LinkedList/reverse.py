class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def reverse(self):
        prev = None
        curr = self.head
        next_ = None
        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        self.head = prev

    def reverse_recur(self):

        def reverse_util(curr, prev):

            # If last node, mark it head
            if curr.next is None:
                self.head = curr

                # update next to prev node
                curr.next = prev
                return
            # Save curr.next node for recursive call
            next_ = curr.next

            # And update next
            curr.next = prev

            reverse_util(next_, curr)
        if self.head is None:
            return
        reverse_util(self.head, None)

    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList() 
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(85) 
    
    print("Given Linked List")
    llist.print_list() 
    llist.reverse_recur() 
    print("Reversed Linked List")
    llist.print_list() 
