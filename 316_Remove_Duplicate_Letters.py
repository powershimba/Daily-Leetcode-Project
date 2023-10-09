"""
Medium
316. Remove Duplicate Letters
"""
# Iteration with Stack
# Time: O(n) / 19ms(52.93%)
# Space: O(n) / 13.51MB(38.60%)

import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        # create counts
        counters = collections.Counter(s)
        
        # result as a stack
        result = []

        # check only used once
        visited = set()

        for char in s:
            counters[char] -= 1
            if char in visited:
                continue
            while result and result[-1] > char and counters[result[-1]] > 0:
                visited.remove(result.pop())
            result.append(char)
            visited.add(char)                

        return ''.join(result)


# Recursion
# Time: O(n) / 47 ms(5.59%)
# Space: O(n) / 13.5 MB(56.77%)
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