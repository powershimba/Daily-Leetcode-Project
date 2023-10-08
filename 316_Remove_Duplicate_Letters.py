"""
Medium
316. Remove Duplicate Letters
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # sort s as set
        for char in sorted(set(s)):
            # seperate if set of suffix(include char) set is same as entire set
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''                        