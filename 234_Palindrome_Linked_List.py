"""
234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

:type head: ListNode
:rtype: bool
"""

# use fast, slow pointers -> create reverse direction of node chains half end of the list -> Compare from each end
# Time Complexity: O(n) / 676ms(68.75%)
# Space complexity: O(1) / 66.84MB(83.39%)
class Solution(object):
    def isPalindrome(self, head):
        slow, fast = head, head
        # Move fast pointer twice further than slow to move slow at the center(odd), center+1(even)
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        prev, slow, prev.next = slow, slow.next, None

        # Create reverse direction of chains at the half end of the list
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # Initiate fast to the front, slow to the end
        fast, slow = head, prev
        
        # Compare from each end
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True
        

# Move to list -> reverse using slicing
# Time Complexity: O(n) / 807ms(18.67%)
# Space complexity: O(n) / 84.95MB(32.51%)

class Solution(object):
    def isPalindrome(self, head):
        new_list = []
        while head:
            new_list.append(head.val)
            head = head.next

        if len(new_list) == 1:
            return True
        
        return new_list == new_list[::-1]

# Move to list -> Two Pointers from the ends of the list
# Time Complexity: O(n) / 782ms(26.81%)
# Space complexity: O(n) / 84.64MB(37.79%)
class Solution(object):
    def isPalindrome(self, head):
        new_list = []
        while head:
            new_list.append(head.val)
            head = head.next

        if len(new_list) == 1:
            return True

        if len(new_list) == 2 and new_list[0] == new_list[1]:
            return True

        l = 0
        r = len(new_list)-1

        while l < r:
            if new_list[l] == new_list[r]:
                l += 1
                r -= 1
            else:
                return False
        
        if l == r or r == l-1:
            return True

                

# Move to list -> Iterate from the front of the list
# Time Complexity: O(n2) / 968ms(8.43%)
# Space complexity: O(n) / 86.88MB(6.25%)
class Solution(object):
    def isPalindrome(self, head):
        new_list = []
        while head:
            new_list.append(head.val)
            head = head.next

        if len(new_list) == 1:
            return True

        for i in range(len(new_list)-1):
            # start from btw nums
            l = i
            r = i+1
            
            while l>0 and r<len(new_list)-1:
                if new_list[l] == new_list[r]:
                    l -= 1
                    r += 1
                else:
                    break
            
            if new_list[l] == new_list[r] and l == 0 and r == len(new_list)-1:
                return True
            
            # start from the num
            if i>0:
                l = i-1
                r = i+1
                
                while l>0 and r<len(new_list)-1:
                    if new_list[l] == new_list[r]:
                        l -= 1
                        r += 1
                    else:
                        break

                if new_list[l] == new_list[r] and l == 0 and r == len(new_list)-1:
                    return True
        
        return False