"""
328. Odd Even Linked List
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Iterative
# Time: O(n) / 20ms(82.80%)
# Memory: O(1) / 16.73MB(53.15%)
class Solution(object):
    def oddEvenList(self, head):
        root_odd = head
        root_even = ListNode(None)
        if head and head.next:
            root_even = head.next

        while head and head.next and head.next.next:
            head_even = head.next
            head.next = head.next.next
            head = head.next
            if head.next:
                head_even.next = head.next
            else:
                head_even.next = None

        if head and root_even.val is not None:
            head.next = root_even

        return root_odd            


        """
        :type head: ListNode
        :rtype: ListNode
        """
        