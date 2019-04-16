'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
class ListNode:  
    def __init__(self, data):
        "constructor to initiate this object"

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

l1 = [2,4,3]
l2 = [5,6,4]
head = n = ListNode(0)
carry = 0
while l1 or l2 or carry:
    val = carry
    if l1:
        val = val + l1.data
        l1 = l1.next
    if l2:
        val = val + l2.data
        l2 = l2.next
    
    n.next = ListNode(val%10)
    n = n.next

print(head)
