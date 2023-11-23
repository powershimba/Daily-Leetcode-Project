"""
77. Combinations
Medium
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(curr, m):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for i in range(m, n+1):
                curr.append(i)
                dfs(curr, i+1)
                curr.pop()

        ans = []
        dfs([], 1)
        return ans


