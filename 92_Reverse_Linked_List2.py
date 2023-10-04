"""
Medium
92. Reverse Linked List II
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n) / 19ms(21.37%)
# Space: O(1) / 13.31MB(90.45%)
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        
        if left == 1:
            left_node = head
        else:
            prev_node = head
            cnt = 2
            while cnt < left:
                prev_node = prev_node.next
                cnt += 1
            left_node = prev_node.next

        ptr1, ptr2, ptr3 = left_node, left_node.next, left_node.next.next 
        if left == right-1:
            ptr2.next = ptr1
        else:
            cycles = right - left
            for i in range(cycles-1):
                ptr2.next = ptr1
                ptr1, ptr2, ptr3 = ptr2, ptr3, ptr3.next 
            ptr2.next = ptr1 
        right_node = ptr2

        if ptr3:
            left_node.next = ptr3
        else:
            left_node.next = None

        if left == 1:
            return right_node
        else:
            prev_node.next = right_node
            return head

        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        