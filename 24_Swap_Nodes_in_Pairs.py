"""
Medium
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive
# Time Complexity: O(n) / 14ms(65.15%)
# Memory Complexity: O(1) / 13.13MB(91.06%)
class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            n = head.next
            head.next = self.swapPairs(n.next)
            n.next = head
            return n
        return head

# Iterately Swap with Dummy Node for indicating first node
# Time Complexity: O(n) / 16ms(44.63%)
# Memory Complexity: O(1) / 13.48MB(11.76%)
class Solution(object):
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            ptr = head.next
            ptr.next, head.next, prev.next = head, ptr.next, ptr
            head, prev = head.next, prev.next.next

        return root.next


# Iterately Swap with Switch for indicating first node
# Time Complexity: O(n) / 17ms(40.74%)
# Memory Complexity: O(1) / 13.08MB(97.78%)
class Solution(object):
    def swapPairs(self, head):
        node = prev = head
        next = root = ListNode()
        root.next = node
        swap = 0
        
        #when swap
        while node and node.next:
            node = node.next

            if swap == 0:
                root.next = node
                swap = 1
            node.next, prev.next = prev, node.next

            if prev.next:
                next = prev.next
                if next.next:
                    prev.next = next.next
                else:
                    break                

                prev = node = next
            
        return root.next
