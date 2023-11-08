# Sliding windows with dictionary
# Time: O(n) / 99.48%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create hash map: (key, value) = (tail value, tail index)
        h = {}
        
        # Sliding window with two pointers
        head = maxlen = 0

        for tail, v in enumerate(s):
            # if tail value is already in window: move head ptr after the duplicated index(h[v])
            if v in h and h[v] >= head:
                head = h[v] + 1
            # else: renew the maxlen
            else:
                maxlen = max(tail - head + 1, maxlen)
            # before move tail ptr, add tail to hash map
            h[s[tail]] = tail
        
        return maxlen
                

# Two pointers with dictionary
# Time : O(n) / 72.51%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Exception
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        cur_substring = {}
        cur_substring[s[0]] = None

        head, tail = 0, 1
        maxlen = 1

        while tail < len(s):
            if tail == head:
                cur_substring[s[tail]] = None
                tail += 1
            else:
                if s[tail] in cur_substring:
                    curlen = tail - head
                    if curlen > maxlen: 
                        maxlen = curlen
                    cur_substring.pop(s[head]) 
                    head += 1
                else:
                    if tail == len(s)-1:
                        curlen = tail - head + 1
                    else:
                        curlen = tail - head
                    if curlen > maxlen: 
                        maxlen = curlen
                    cur_substring[s[tail]] = None
                    tail += 1
       
        return maxlen

# Iterate
# Time: O(n2) / 20.18%
class Solution(object):
    def substring(self, s):
        output = {}
        for i in s:
            if i in output:
                return len(output.keys())
            else:
                output[i] = None
        return len(output.keys())

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        for i in range(len(s)):
            curlen = self.substring(s[i:])
            if curlen > maxlen:
                maxlen = curlen
        return maxlen


        