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
        
    def delete_node(self, position):

        if self.head == None:
            return
        
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        # Find previous node of the node to be deleted
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                # if next node is None (is last of the LinkedList)
                # where position is more than number of nodes
                break
        
        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        next_ = temp.next.next
        
        # Unlink the node from linked list
        temp.next = None

        # Link prev node and next node
        temp.next = next_

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.push(8)

    print("Created Linked List")
    llist.print_list()
    llist.delete_node(4)
    print("Linked List after Deletion at position 4")
    llist.print_list()