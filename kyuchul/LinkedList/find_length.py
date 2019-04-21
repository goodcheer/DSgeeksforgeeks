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
    
    @property
    def length(self):
        cnt = 0
        temp = self.head
        while temp is not None:
            cnt += 1
            temp = temp.next
        return cnt
    
    @property
    def legnth_(self):
        return self.length_recur(self.head)

    def length_recur(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.length_recur(node.next)

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)

    print('Count of nodes is:', llist.length, llist.legnth_)