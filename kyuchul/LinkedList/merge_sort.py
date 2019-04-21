from merge_two_sorted import LinkedList, sorted_merge


def get_middle(head):
    if head is None:
        return head
    fast_ptr = head.next  # head + 1
    slow_ptr = head
    while fast_ptr is not None:
        fast_ptr = fast_ptr.next  # head + 2
        if fast_ptr is not None:
            slow_ptr = slow_ptr.next  # head + 1
            fast_ptr = slow_ptr.next  # head + 3, which is slow + 2
            # to sum up, the iteration becomes
            # n for slow
            # 2n+1 for fast
            # therefore, if fast reaches the last node, so the length is 2n+1,
            # thus the middle point is n, where slow points.
    return slow_ptr

def merge_sort(head):

    # base case: if lenght == 0 or 1
    if (head is None) or (head.next is None):
        return head
    
    middle = get_middle(head)
    next_of_middle = middle.next

    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_of_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(15)
    llist.push(10)
    llist.push(5)
    llist.push(20)
    llist.push(3)
    llist.push(2)

    print('Before merge sort')
    llist.print_list()
    llist.head = merge_sort(llist.head)
    print('After merge sort')
    llist.print_list()
