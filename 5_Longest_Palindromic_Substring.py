# Brutal Force Solution : O(n3)
# My Solution : O(n2)ls

class Solution(object):
    def longestPalindrome(self, s):
        def expand(i, j):
            while i>= 0 and j<len(s) and s[i] == s[j]:
                i = i-1
                j = j+1
            return s[i+1:j]
        
        final = ""
        for i in range(len(s)):
            pan1 = expand(i,i) # start from one letter
            if len(pan1) > len(final):
                final = pan1
            pan2 = expand(i, i+1) # start from the center between two letters
            if len(pan2) > len(final):
                final = pan2
        return final

        """
        :type s: str
        :rtype: str
        """
        