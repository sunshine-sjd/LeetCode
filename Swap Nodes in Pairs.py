'''
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
        current.next = next_two
        next_two.next = next_one
        next_one.next = next_three
        current = current.next.next
    return dummy.next
