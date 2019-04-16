''' Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = None

temp = l1
while temp is not None and temp.next is not None:
    temp.val , temp.next.val = temp.next.val , temp.val
    temp = temp.next.next

temp = l1
while temp is not None:
    print(temp.val)
    temp = temp.next