"""
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

"My Solution"

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        if length & 1 == 0:
            index = length * 0.5
        else:
            index = length * 0.5 - 0.5
        index = int(index)
        current = head
        for i in range(index):
            current = current.next
        return current

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
"""Other Solution: Using 2 pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        middle = ListNode()
        end = ListNode()

        middle = end = head

        while end and end.next:
            middle = middle.next
            end = end.next.next
        
        return middle            