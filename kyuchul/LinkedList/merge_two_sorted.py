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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    

def sorted_merge(head_a, head_b):
    dummy_node = Node(0)

    tail = dummy_node

    while True:
        # If either list runs out, use the other list
        if head_a is None:
            tail.next = head_b
            break
        if head_b is None:
            tail.next = head_a
            break
    
        # Compare the data of the two lists whichever lists' data is smaller,
        # append it into tail and advance the head to the next Node
        if head_a.data <= head_b.data:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next
    
        tail = tail.next
    return dummy_node.next



if __name__ == '__main__':
    llist_a = LinkedList()
    llist_b = LinkedList()

    llist_a.push(15)
    llist_a.push(10)
    llist_a.push(5)

    llist_b.push(20)
    llist_b.push(3)
    llist_b.push(2)

    llist_a.print_list()
    llist_b.print_list()

    llist_a.head = sorted_merge(llist_a.head, llist_b.head)
    llist_a.print_list()