"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""

#Solution 1
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        s.reverse()

#Solution 2
#Time Complexity: O(n), Space Complexity: O(1)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        i = 0
        j = len(s) - 1

        while(i<j):
            tem = s[i]
            s[i] = s[j]
            s[j] = tem
            i += 1
            j -= 1
        
    

