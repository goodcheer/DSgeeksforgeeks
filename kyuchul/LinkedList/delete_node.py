class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        """
        push a new node to the front
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_node(self, key):
        temp = self.head
        
        # if head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change `prev.next`
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        # if key was not present in linked list
        if temp == None:
            return
        
        # Unlin the node form the list
        prev.next = temp.next
        temp = None
    
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

    print('Created List: ', end='')
    llist.print_list()
    llist.delete_node(1)
    print('Linked List after Deletion of 1: ', end='')
    llist.print_list()
    
