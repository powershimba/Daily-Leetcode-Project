"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative
# Time Complexity: O(n) / 12ms(91.51%)
# Space Complextity: O(1) / 15.20MB(80.29%)
class Solution(object):
    def reverseList(self, head):
        node = head
        prev = None
        while node:
            next = node.next
            node.next = prev
            
            prev = node
            node = next

        return prev 

# Recursive
# Time Complexity: O(n) / 20 ms(43.78%)
# Space Complexity: O(1) / 19.3 MB(5.73%)
class Solution(object):
    def reverseList(self, head):
        def reverse(node, prev=None):
            if not node:
                return prev
            next = node.next
            node.next = prev
            return reverse(next, node)
        
        return reverse(head)
