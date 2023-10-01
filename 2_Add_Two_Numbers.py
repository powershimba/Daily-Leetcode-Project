"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Iteration
#Time Complexity: O(n) / 43ms(64.20%)
#Space Complexity: O(n) / 13.28MB(80.24%) 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        new = ListNode()
        head = ListNode()
        head.next = new
        save = 0

        while l1 or l2 or save:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            
            total = l1_val + l2_val + save
            
            if total < 10:
                new.val = total
                save = 0
            else:
                new.val = total - 10
                save = 1

            if l1 or l2 or save:
                next = ListNode()
                new.next = next
                new = new.next

        return head.next

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        