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


        