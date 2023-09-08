import re

class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        print(s)
        s = s.lower()
        print(s)
        if s == s[::-1]:
            return True
        else:
            return False

        """
        :type s: str
        :rtype: bool
        """
        