class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):

        # 1. alloc the Node and put the data
        new_node = Node(new_data)
        # 2. Make next of new Node as head
        new_node.next = self.head
        # 3. Move the head to poin to new Node
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    
    def swap_nodes(self, x, y):

        # Nothing to do if x and y are same
        if x == y:
            return
        
        # Search for x (keep track of prevX and CurrX)
        prev_x = None
        curr_x = self.head
        while (curr_x is not None) and (curr_x.data != x):
            prev_x = curr_x
            curr_x = curr_x.next
        
        prev_y = None
        curr_y = self.head
        while (curr_y is not None) and (curr_y.data != y):
            prev_y = curr_y
            curr_y = curr_y.next

        # If either x or y is not present. nothing to do
        if (curr_x is None) or (curr_y is None):
            return
        
        # If both presents, do SWAP

        # if x is not head of linked list
        if prev_x is not None:
            prev_x.next = curr_y
        else:
            self.head = curr_y

        if prev_y is not None:
            prev_y.next = curr_x
        else:
            self.head = curr_x
        
        # Swap next pointers
        temp = curr_x.next
        curr_x.next = curr_y.next
        curr_y.next = temp


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7) 
    llist.push(6) 
    llist.push(5) 
    llist.push(4) 
    llist.push(3) 
    llist.push(2) 
    llist.push(1) 
    print("Linked list before calling swapNodes() ")
    llist.print_list() 
    llist.swap_nodes(4, 3) 
    print("Linked list after calling swapNodes() ")
    llist.print_list() 